from models import Board



def checkVisited(node, visited):
    if node in visited:
        return True
    return False


def constructPath(node, src, goal, visited, type):
    path = []
    reverseNode = None
    for e in visited:
        if node.config == e.config:
            reverseNode = e
    if reverseNode is not None:
        path.append(node)
        if type == 1:
            temp = node
        elif type == 2:
            temp = reverseNode
        while temp.config != src.config:
            temp = temp.parent
            path.insert(0, temp)
        if type == 1:
            temp = reverseNode
        elif type == 2:
            temp = node
        while temp.config != goal.config:
            temp = temp.parent
            path.append(temp)
    return path


def biDirectionalBFS(src, goal,lens):
    print("Calculating...")
    visited = set()
    reverseVisited = set()
    queue = []
    reverseQ = []
    queue.append(src)
    reverseQ.append(goal)

    while queue and reverseQ:
        # forward step first
        poppedF = queue.pop(0)
        if checkVisited(poppedF, reverseVisited):
            # we got the connected node
            lens.append(len(visited))
            lens.append(len(reverseVisited))
            return constructPath(poppedF, src, goal, reverseVisited, 1)
        visited.add(poppedF)
        neighbours = poppedF.getNeighbours()
        for neighbour in neighbours:
            if not checkVisited(neighbour, visited):
                queue.append(neighbour)
                # this to avoid reading the nodes which are already in the queue
                visited.add(neighbour)
        # backward step
        poppedR = reverseQ.pop(0)
        if checkVisited(poppedR, visited):
            # got goal
            lens.append(len(visited))
            lens.append(len(reverseVisited))
            return constructPath(poppedR, src, goal, visited, 2)

        reverseVisited.add(poppedR)
        neighboursR = poppedR.getNeighbours()
        for neighbour in neighboursR:
            if not checkVisited(neighbour, reverseVisited):
                reverseQ.append(neighbour)
                reverseVisited.add(neighbour)
    print("This instance of the puzzle is unsolvable.")
    print("Visited {} states in the forward direction and {} states in the reverse direction".format(len(visited),len(reverseVisited)))
    print("but could not find a solution.")
    return []

def main():
    lens = []
    goalBoard = Board((("_", "1", "2"), ("3", "4", "5"), ("6", "7", "8")))
    print("The default goal board is:")
    goalBoard.print()
    print("Please enter the source board (space separated values), for blank use _ (an underscore)")
    print("For eg, one input could be 8 7 6 _ 4 3 2 1 5")
    inp = input().split()
    r1 = tuple(inp[0:3])
    r2 = tuple(inp[3:6])
    r3 = tuple(inp[6:9])
    srcBoard = Board((r1, r2, r3))
   
    path = biDirectionalBFS(srcBoard, goalBoard,lens)
    if path:
        print("Moves required to solve :" ,len(path)-1,"\n")
        print("The board states are as follows (move 0 is source board):\n ")
        i = 0
        for x in path:
            print("Move ",i,": ")
            x.print()
            i+=1
        print("Visited {} states in the forward direction and {} states in the reverse direction".format(lens[0],lens[1]))
        print("and found a solution")


if __name__ == "__main__":
    main()


# src config which yields results 4 6 1 _ 2 8 7 3 5