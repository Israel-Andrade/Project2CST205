#Salvador Hernandez
#Creates a network Map based on the user
import networkx as nx
import matplotlib.pyplot as plt
import os
import pydot # import pydot or you're not going to get anywhere my friend :D
from PIL import Image
import sys

def draw_graph(graph, labels=None, graph_layout='shell',
               node_size=1600, node_color='blue', node_alpha=0.3,
               node_text_size=12,
               edge_color='blue', edge_alpha=0.3, edge_tickness=1,
               edge_text_pos=0.3,
               text_font='sans-serif'):

    # create networkx graph
    G=nx.Graph()

    # add edges
    for edge in graph:
        G.add_edge(edge[0], edge[1])

    # these are different layouts for the network you may try
    # shell seems to work best
    if graph_layout == 'spring':
        graph_pos=nx.spring_layout(G)
    elif graph_layout == 'spectral':
        graph_pos=nx.spectral_layout(G)
    elif graph_layout == 'random':
        graph_pos=nx.random_layout(G)
    else:
        graph_pos=nx.shell_layout(G)

    nx.draw(G)
    #nx.draw_random(G)
    #nx.draw_spectral(G)
    # show graph

    newFolder = graphPath
    if not os.path.exists(newFolder):
        os.makedirs(newFolder)
    plt.savefig(newFolder+anchor+"Network.png")
    #plt.show()
    #nx.show()

#gets the value from the argument
inFile = sys.argv[1]
#removes gets the value befor the "."
anchor = inFile.split(".")[0]

#sets paths
currentDirectory = os.getcwd()+"/"

imgPath = currentDirectory+"data/images/"
myPath = currentDirectory+"data/users/"
graphPath = currentDirectory+"data/networks/"
twitter = "https://twitter.com/"
url = ""
file = myPath+inFile

arr = []
mArr = []
lArr = []
# let's add the relationship between the king and vassals
with open(file, "r") as f:
    for line in f:
        line= line[:-1]
        arr.append(line)
        # and we obviosuly need to add the edge to our graph
        mArr.append(anchor)
        lArr.append(line)

#for 2 levels
'''
arr2 = []
for element in arr:
    with open(myPath+element+".txt", "r") as f:
        for line in f:
            line= line[:-1]
            arr2.append(line)
            mArr.append(element)
            lArr.append(line)
'''
#for 3 levels
'''        
arr3 = []
for element in arr2:
    with open(myPath+element+".txt", "r") as f:
        for line in f:
            line= line[:-1]
            arr3.append(line)
            mArr.append(element)
            lArr.append(line)
'''            
graph = []
#adds the nodes to the graph
for i in range(0,len(mArr)):
    graph.append((mArr[i], lArr[i]))

# if edge labels is not specified, numeric labels (0, 1, 2...) will be used
draw_graph(graph)