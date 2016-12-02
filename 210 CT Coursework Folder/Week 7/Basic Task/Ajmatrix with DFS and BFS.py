class AMatrix: 
    
    def __init__(self):
        import numpy
        self.ajMatrix = numpy.zeros(shape=(10,10  ))

        self.nodes = []
        while len(self.nodes) <= 10:
            self.nodes.append(None)



    def addNode(self,node):
        self.n = 0
        while self.nodes[self.n] != None:
            self.n = self.n + 1
            if (self.nodes[self.n] == node):
                print("ERROR; Duplicate node")
                return 
        if ((self.n != 9) and (self.nodes[self.n] == None)):
            self.nodes[self.n] = node
        else:
            print("ERROR; No free nodes")
            return 
        return

    def addEdge(self,node1,node2,weight):
        self.x = 0
        while self.nodes[self.x] != node1:
            self.x = self.x + 1
        self.y = 0
        while self.nodes[self.y] != node2:
            self.y = self.y + 1

        self.ajMatrix[self.x,self.y] = weight
        

        return

    def depthFirstSearch(self):
        self.S = list(self.nodes)
        self.visited = []
        while (self.S != []):
            self.u = self.S.pop()
            if (self.u not in self.visited):
                self.visited.append(self.u)
                
                self.S = self.S + self.ajacencyFind(self.u)

        return self.visited

    def breadthFirstSearch(self):
        self.Q = list(self.nodes)
        self.visited = []
        while (self.Q != []):
            self.u = self.Q.pop(0)
            
            if (self.u not in self.visited):
                self.visited.append(self.u)
                
                self.Q = self.Q + self.ajacencyFind(self.u)

        return self.visited


    def ajacencyFind(self, node):
        self.pos = 0
        
        while self.nodes[self.pos] != node:
            self.pos = self.pos + 1
        self.n = 0
        self.edges= []
        while self.n < 10:
            if self.ajMatrix[self.pos,self.n] == True :
                self.edges.append(self.nodes[self.n])

            self.n = self.n + 1  

        return self.edges

    def dijkstraSearch(self, start, end)

    
class dNode(AMatrix):
     def __init__(self,weight,visited):
         self.weight = weight
         self.visitied = visited
        
robot = AMatrix()
robot.addNode("Legs")
robot.addNode("Body")
robot.addNode("Arms")
robot.addNode("Head")
robot.addNode("Eyes")
robot.addNode("Fingers")
robot.addNode("Hand")

robot.addEdge("Legs","Body")
robot.addEdge("Arms","Body")
robot.addEdge("Head","Body")
robot.addEdge("Eyes","Head")
robot.addEdge("Fingers","Hand")
robot.addEdge("Hand","Arms")


print(robot.depthFirstSearch())
print(robot.breadthFirstSearch())
