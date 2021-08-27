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


def biDirectionalBFS(src, goal):
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
            return constructPath(poppedR, src, goal, visited, 2)

        reverseVisited.add(poppedR)
        neighboursR = poppedR.getNeighbours()
        for neighbour in neighboursR:
            if not checkVisited(neighbour, reverseVisited):
                reverseQ.append(neighbour)
                reverseVisited.add(neighbour)
    print("This instance of the puzzle is unsolvable.")
    return []

def main():
    srcBoard = Board((("4", "6", "1"), ("3", "2", "8"), ("7", "_", "5")))
    goalBoard = Board((("_", "1", "2"), ("3", "4", "5"), ("6", "7", "8")))
    path = biDirectionalBFS(srcBoard, goalBoard)
    if path:
        print("Moves required to solve :" ,len(path)-1,"\n")
        print("The board states are as follows (move 0 is source board):\n ")
        i = 0
        for x in path:
            print("Move ",i,": ")
            x.print()
            i+=1


if __name__ == "__main__":
    main()
