def makeArrayConsecutive2(statues):
    statues.sort()
    y = 0
    for i in range(0,len(statues)-1):
        y += statues[i+1] - statues[i] -1
        
    return y
            