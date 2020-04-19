from collections import defaultdict

def timeRanges(timesInOut):

    timecount = defaultdict(int)

    for t in timesInOut:
        timeIn = t[0]
        timeOut = t[1]

        timecount[timeIn] += 1
        timecount[timeOut] -= 1 

    time_list = timecount.keys()
    time_list.sort()

    final_list = []
    cumulative = 0
    for k in time_list:
        cumulative += timecount[k]
        final_list.append((k, cumulative))
    
    return final_list

inp = [(3,7), (5,7), (7,14), (8,12), (14,20), (5,20)]
out = timeRanges(inp)
for p in out:
    print p[0], p[1]
