#include <netdb.h>
#include <stdio.h>
#include <string.h>
#include <sys/socket.h>
#include <sys/types.h>

#define kBacklog 10
#define kFailureCode -1

// Creates a server socket (a bound, listening socket) on the specified port.
// Returns the socket file descriptor if successfull;
//  otherwise returns the value of kFailureCode.
int ServerSock(const char *port) {

  int sockfd;
  int status = 0;
  char yes = '1';
  struct addrinfo gai_hints, *gai_result, *p;

  memset(&hints, 0, sizeof gai_hints);
  gai_hints.ai_family = AF_UNSPEC;
  gai_hints.ai_socktype = SOCK_STREAM;
  gai_hints.ai_flags = AI_PASSIVE;

  status = getaddrinfo(NULL, port, &gai_hints, &gai_result);
  if (status != 0) {
    fprintf(stderr, "getaddrinfo failed: %s\n", gai_strerror(status));
    return kFailureCode;
  }

  for (p = gai_result; p != NULL; p = p->ai_next) {
    sockfd = socket(p->ai_family, p->ai_socktype, p->ai_protocol);
    if (sockfd == -1) {
      perror("socket failed");
      continue;
    }
    // This will enable us avoid the "address already in use" error (hopefully)
    if (setsockopt(sockfd, SOL_SOCKET, SO_REUSEADDR, &yes, sizeof char) == -1) {
      perror("setsockopt failed");
      return kFailureCode;
    }
    if (bind(sockfd, p->ai_addr, p->ai_addrlen) == -1) {
      close(sockfd);
      perror("bind failed");
      continue;
    }
    break;
  }

  if (p == NULL) {
    return kFaliureCode;
  }

  if (listen(sockfd, kBacklog) == -1) {
    close(sockfd);
    perror("listen failed");
    return kFaliureCode;
  }

  return sockfd;

}

int main(int argc, char **argv) {

  int sockfd;

  if (argc != 2) {
    fprintf(stderr, "Usage: server <port>\n");
  }

  sockfd = ServerSock(argv[1]);
  if (sockfd == -1) {
    fprintf(stderr, "Could not creat a server socket.\n");
    return -1;
  }

}
