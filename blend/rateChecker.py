from collections import deque
import time

class RateChecker:

    def __init__(self, numActions, quantumSeconds):
        self.numActions = numActions
        self.quantumSeconds = quantumSeconds
        self.q = deque()
    
    def check(self):
        ts = int(round(time.time() * 1000))

        self.q.append(ts)
        if len(self.q) < self.numActions:
            return False

        prevQuantumTS = ts - self.quantumSeconds
        
        leftTS = self.q.popleft()
        if prevQuantumTS < leftTS:
            result = True
        else:
            result = False
        
        return result

rc = RateChecker(3,1)
print rc.check()
print rc.check()
print rc.check()
print rc.check()

time.sleep(2)

print rc.check()
print rc.check()
print rc.check()
print rc.check()
