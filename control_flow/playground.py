list_test = [1, 2, 3]

list_test.remove(list_test[0])

list_test += [list_test.pop(0)]

# exercise kata position qeueu for ticket

def queue(queuers,pos):
    friendWait = queuers[pos]
    frontOfLine = queuers[:pos+1]
    backOfLine = queuers[pos+1:]
    frontOfLine = [min(x, friendWait) for x in frontOfLine]
    print(frontOfLine)
    backOfLine = [min(x, friendWait-1) for x in backOfLine]
    print(backOfLine)
    return sum(frontOfLine) + sum(backOfLine)

queue([56, 2, 3, 4, 5, 6], 3)
