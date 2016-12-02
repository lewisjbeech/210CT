class graph:
    def __init__(self):
        self.vertexes = []

    def findVertex(self, value):
        for vertex in self.vertexes:
            if vertex.value == value:
                return vertex

    def addVertex(self,value):
        value = vertex(value)
        self.vertexes.append(value)

    def addEdge(self, start, end, weight):
        startvertex = self.findVertex(start)
        endvertex = self.findVertex(end)
        startvertex.vertexAddEdge(endvertex, weight)

class vertex(graph):
    def __init__(self, value):
        self.value = value
        self.previous = []
        self.tw = None
        self.edge = []

    def vertexAddEdge(self, end, weight):
        end = edge(end, weight)
        self.edge.append(end)

    def __str__(self):
        return("Vertext:" + str(self.value))
        

class edge(vertex):

    def __init__(self, end,weight):
        self.weight = weight
        self.end = end


def dijkstra(G,s,d):
    
    v = G.findVertex(s)
    z = G.findVertex(d)
    for i in G.vertexes:
        i.tw = 1000
    
    G.findVertex(s).tw = 0

    visited = []

    while (v != z):
        for i in v.edge:
            if (v.tw + i.weight) < (i.end.tw):
                #print(i.end.value,i.end.tw)
                i.end.tw = (v.tw + i.weight)
                i.end.previous.append(v)
        visited.append(v.value)
        minimum = 1001
        for i in v.edge:
            if (i.end not in visited) and (i.end.tw < minimum):
                v = i.end
                print(v.value)
                minimum = i.end.tw

    return visited,v.value
                
    






robot = graph()
robot.addVertex(1)
robot.addVertex(2)
robot.addVertex(3)
robot.addVertex(4)
robot.addVertex(5)
robot.addVertex(6)
robot.addEdge(1,2,5)
robot.addEdge(1,3,1)
robot.addEdge(3,2,2)
robot.addEdge(2,4,2)
robot.addEdge(3,5,6)
robot.addEdge(4,6,6)
robot.addEdge(4,5,1)
robot.addEdge(5,6,1)
print(dijkstra(robot,1,6))
