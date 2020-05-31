list_test = [1, 2, 3]

list_test.remove(list_test[0])

list_test += [list_test.pop(0)]

# exercise kata position

def queue(queuers,pos):
    friendWait = queuers[pos]
    # Divide the line into the front of the line (up to the friend)
    # and back of the line (behind the friend):
    frontOfLine = queuers[:pos+1]
    backOfLine = queuers[pos+1:]
    print(frontOfLine)
    print(backOfLine)
    # Convert the frontOfLine to the min of friendWait:
    frontOfLine = [min(x, friendWait) for x in frontOfLine]
    print(frontOfLine)
    # Convert the backOfLine to the min of friendWait-1:
    backOfLine = [min(x, friendWait-1) for x in backOfLine]
    print(backOfLine)
    # Return the result, which is the sum of both line parts:
    return sum(frontOfLine) + sum(backOfLine)

queue([1, 2, 3, 4, 5, 6], 3)
