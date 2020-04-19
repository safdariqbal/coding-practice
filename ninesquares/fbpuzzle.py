wordlist = []
while True:
    try:
        wordlist.append(raw_input())
    except:
        break

for wi in wordlist:
    for wj in wordlist:
        if wj.startswith(wi[1]):
            for wk in wordlist:
                if wk.startswith(wi[2]):
                    diag1 = wi[0] + wj[1] + wk[2]
                    diag2 = wi[2] + wj[1] + wk[0]
                    v1 = wi[0] + wj[0] + wk[0]
                    v2 = wi[1] + wj[1] + wk[1]
                    v3 = wi[2] + wj[2] + wk[2]
                    if (diag1 in wordlist) and (diag2 in wordlist) and (v1 in
wordlist) and (v2 in wordlist) and (v3 in wordlist):
                            print wi
                            print wj
                            print wk
                            print

