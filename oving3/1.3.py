# Bus
print("$$\\text{BussGraph: Formula for degree centrality for each node is:}$$\n")
print("$$\\frac{(\\text{amount of edges the node has})}{(\\text{amount of nodes in the graph - 1})}$$\n")

buss_graph = BussGraph(8)

node_count = len(buss_graph.nodes())
for node, degree in buss_graph.degree():

    centrality = degree / (node_count - 1)
    fa1 = str(degree)
    fa2 = str(node_count) + " - 1"
    fb1 = str(node_count-1)

    mrk1 = "\\frac{" + fa1 + "}{" + fa2 + "}"
    mrk2 = "\\frac{" + fa1 + "}{" + fb1 + "}"

    formula_str = "( " + str(degree) + " / " + str(node_count) + " - 1 )"
    formula_str2 = "( " + str(degree) + " / " + str(node_count - 1) + " )"

    node_str = "\\text{Node}_" + str(node)
    print("$$" + str(node_str), "=", mrk1, "\\implies", mrk2,
          "\\implies", str(round(centrality, 2)) + "$$\n")


//////


# Bus
print("## Betweenness centrality for StarGraph\n")
print("$$\\text{The formula for closesness centrality for a node is:}$$\n")
#print("(Amount of times the node is in a shortes path) / ((amount of nodes - 1)(amount of nodes - 2))  / 2 \n")

#print("$$\\text{BussGraph: Formula for degree centrality for each node is:}$$\n")
print("$$\\frac{\\text{Amount of times the node is in a shortes path}}{\\frac{\\text{(amount of nodes - 1)(amount of nodes - 2)}}{2}}$$\n")

graph = StarGraph(8)

# Creating a dictionary for each node and setting the start value to 0
interuptCount = {}
for node in graph:
    interuptCount[node] = []


for start_node in graph:
    for end_node in graph:
        # Doesn't count it if it't the same node (even though it doesn't matter)
        if start_node == end_node:
            continue

        # The stortest from a node to another is returned as an array
        shortest_path = graph.get_shortest_path(start_node, end_node)

        for node in shortest_path:
            if node == start_node or node == end_node:  # Doesn't count if if it it is the nodes at the "ends"
                continue

            # Increase the interupt count of the node by one, since the node is a part of the shortest path
            if (end_node, start_node) not in interuptCount[node]:
                interuptCount[node].append((start_node, end_node))


for node, interuptts in interuptCount.items():
    interupts = len(interuptts)
    standarization = (len(graph) - 1) * (len(graph) - 2)
    betweenness_centrality = interupts / standarization * 2

    node_str = "$$\\text{Node}_" + str(node) + ":$$"
    formula_str = str(interupts).rjust(
        2) + " / ( (" + str(len(graph)) + "-1)*(" + str(len(graph)) + "-2)" + " )"

    mathfrac = "\\frac{" + str(interupts) + "}{\\frac{(" + \
        str(len(graph)) + "-1)*(" + str(len(graph)) + "-2)}{2}}"
    mathfrac2 = "\\frac{" + str(interupts) + "*2}{" + \
        str(((len(graph) - 1)*(len(graph) - 2))) + "}"

    #print(node_str, "\nShortest paths the node is in:\n", interuptts,"=", len(interuptts) ,"\n\n", formula_str, "=>", betweenness_centrality, "\n")
    print(node_str, "\n$$\\text{Shortest paths the node is in:}$$\n\n$$", interuptts, "\\implies", len(
        interuptts), "$$", "\n\n$$", mathfrac, "\\implies", mathfrac2, "\\implies", round(betweenness_centrality, 2), "$$\n")

print("\n", graph.betweenness_centrality())


print("\n\n", interuptCount)


/////////


# Bus
print("## Betweenness centrality for BussGraph\n")
print("$$\\text{The formula for closesness centrality for a node is:}$$\n")
#print("(Amount of times the node is in a shortes path) / ((amount of nodes - 1)(amount of nodes - 2))  / 2 \n")

#print("$$\\text{BussGraph: Formula for degree centrality for each node is:}$$\n")
print("$$\\frac{\\text{Amount of times the node is in a shortes path}}{\\frac{\\text{(amount of nodes - 1)(amount of nodes - 2)}}{2}}$$\n")

graph = BussGraph(8)

# Creating a dictionary for each node and setting the start value to 0
interuptCount = {}
for node in graph:
    interuptCount[node] = []


for start_node in graph:
    for end_node in graph:
        # Doesn't count it if it't the same node (even though it doesn't matter)
        if start_node == end_node:
            continue

        # The stortest from a node to another is returned as an array
        shortest_path = graph.get_shortest_path(start_node, end_node)

        for node in shortest_path:
            if node == start_node or node == end_node:  # Doesn't count if if it it is the nodes at the "ends"
                continue

            # Increase the interupt count of the node by one, since the node is a part of the shortest path
            if (end_node, start_node) not in interuptCount[node]:
                interuptCount[node].append((start_node, end_node))


for node, interuptts in interuptCount.items():
    interupts = len(interuptts)
    standarization = (len(graph) - 1) * (len(graph) - 2)
    betweenness_centrality = interupts / standarization * 2

    node_str = "$$\\text{Node}_" + str(node) + ":$$"
    formula_str = str(interupts).rjust(
        2) + " / ( (" + str(len(graph)) + "-1)*(" + str(len(graph)) + "-2)" + " )"

    mathfrac = "\\frac{" + str(interupts) + "}{\\frac{(" + \
        str(len(graph)) + "-1)*(" + str(len(graph)) + "-2)}{2}}"
    mathfrac2 = "\\frac{" + str(interupts) + "*2}{" + \
        str(((len(graph) - 1)*(len(graph) - 2))) + "}"

    #print(node_str, "\nShortest paths the node is in:\n", interuptts,"=", len(interuptts) ,"\n\n", formula_str, "=>", betweenness_centrality, "\n")
    print(node_str, "\n$$\\text{Shortest paths the node is in:}$$\n\n$$", interuptts, "\\implies", len(
        interuptts), "$$", "\n\n$$", mathfrac, "\\implies", mathfrac2, "\\implies", round(betweenness_centrality, 2), "$$\n")

print("\n", graph.betweenness_centrality())


print("\n\n", interuptCount)
