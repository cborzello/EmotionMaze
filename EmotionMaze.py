#Must Install numpy package before runtime
#Must Install easyTinker before runtime
import random

class Square:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.left = True
        self.right = True
        self.top = True
        self.bottom = True
        self.visited = False

class Node:
    def __init__(self,squareOne,squareTwo):
        self.squareOne = squareOne
        self.squareTwo = squareTwo
        self.connectors = list()

tall = 10
wide = 10
maze = list()
visited = list()
nodes = list()
for x in range(0,tall):
    for y in range(0,wide):
        maze.append(Square(x,y))

startX = random.randint(0, tall)
startY = random.randint(0, wide)

def mazeCreate():
    if findneighbor(startX,startY) == 0 and not maze[startX - 1][startY].visited:
        createnode(startX, startY, 0)
    elif findneighbor(startX,startY) == 1 and not maze[startX][startY - 1].visited:
        createnode(startX, startY, 1)
    elif findneighbor(startX, startY) == 2 and not maze[startX + 1][startY].visited:
        createnode(startX, startY, 2)
    elif findneighbor(startX, startY) == 3 and not maze[startX][startY - 1].visited:
        createnode(startX, startY, 3)
    else:
        if not allTried():
            backup()
            mazeCreate()
        else:
            #implement graphics here
            temp = -1


def findneighbor(startX,startY):
    neighborWall = random.randint(0,4)
    if neighborWall == 0 and startX != 0:
        return 0
    elif neighborWall == 1 and startY != 0:
        return 1
    elif neighborWall == 2 and startX != 9:
        return 2
    elif neighborWall == 3 and startY != 9:
        return 3
    else:
        return -1



def createnode(startX, startY, int):
    startingIndex = (startX * 10 + startY)
    if(int == 0):
        nodes.append(Node(maze[startX][startY],maze[startX - 1][startY]))
        maze[startX - 1][startY].visited = True
        maze[startX][startY].left = False
        maze[startX - 1][startY].right = False
        visited.append(maze[startX - 1][startY])
        recenter(maze[startX - 1][startY])

    elif(int == 1):
        nodes.append(Node(maze[startX][startY], maze[startX][startY - 1]))
        maze[startX][startY - 1].visited = True
        maze.index((startingIndex)).top = False
        maze[startX][startY - 1].bottom = False
        visited.append(maze[startX][startY - 1])
        recenter(maze[startX][startY - 1])

    elif (int == 2):
        nodes.append(Node(maze[startX][startY], maze[startX + 1][startY]))
        maze[startX + 1][startY].visited = True
        maze[startX][startY].right = False
        maze[startX + 1][startY].left = False
        visited.append(maze[startX + 1][startY])
        recenter(maze[startX + 1][startY])

    elif (int == 3):
        nodes.append(Node(maze[startX][startY], maze[startX][startY + 1]))
        maze[startX][startY + 1].visited = True
        maze[startX][startY].bottom = False
        maze[startX][startY + 1].top = False
        visited.append(maze[startX][startY + 1])
        recenter(maze[startX][startY + 1])

def allTried():
    if len(maze) == len(visited):
        return True
    else:
        return False

def backup():
    temp = -1

def recenter(square):
    startX = square.x
    startY = square.y
