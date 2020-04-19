#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <string>
#include <bitset>
#include <cstdio>
#include <limits>
#include <vector>
#include <climits>
#include <cstring>
#include <cstdlib>
#include <fstream>
#include <numeric>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <unordered_map>

using namespace std;

int number_needed(string a, string b) {
    sort(a.begin(), a.end());
    sort(b.begin(), b.end());

    cout << a << endl;
    cout << b << endl;
    
    char c;
    int i = 0, j = 0, k = 0, l = 0;
    int del = 0, result = 0;
    for (c = 'a'; c <= 'z'; c++) {
        while(a[i+k] == c) {
            k++;
        }
        while(b[j+l] == c) {
            l++;
        }
        if (k > l)
            del = k - l;
        else
            del = l - k;
        result += del;
        i += k; j += l;
        k = 0; l = 0;
    }
    return result;
}

int main(){
    string a;
    cin >> a;
    string b;
    cin >> b;
    cout << number_needed(a, b) << endl;
    return 0;
}