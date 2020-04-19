from collections import defaultdict
def top_freq(text, limit):

    words = text.split()
    word_count = defaultdict(0)
    freq_lst = [None]*len(words)
    for i in xrange(0, len(words)):
        freq_lst[i] = set()

    for w in words:
        word_count[w] += 1

    for w,c in word_count.iteritems():
        freq_arr[c].add(word)
    
    result = []
    num_returned = 0
    i = len(freq_lst)-1
    #limit = min(limit, len(word_count.keys()))
    while num_returned < limit and i > 0:
        if len(freq_lst[i]) == 0:
            i -= 1
        else:
            result.append(freq_lst[i].pop())
            num_returned += 1

    return result
        


