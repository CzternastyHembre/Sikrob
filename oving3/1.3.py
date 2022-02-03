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


//////

# Bus
print("## Closesness centrality for StarGraph: \n")
print("$$\\text{The formula for closesness centrality for a node is:}$$\n")

print("$$\\frac{\\text{Amount of nodes - 1}}{\\text{Total distance form that node to every other}}$$\n")


graph = StarGraph(8)

# Creating a dictionary for each node and setting the start value to 0
totalDist = {}
for node in graph:
    totalDist[node] = []

for start_node in graph:
    for end_node in graph:
        # Doesn't count the dist from itself (even though it's 0)
        if start_node == end_node:
            continue

        # The distance from a node to another is
        # The length of the shortest path - 1 (because you don't count with the starting node)
        d = len(graph.get_shortest_path(start_node, end_node)) - 1

        # Adding the distance for that node to the dictionary to
        # eventually getting the sum of all distances for the node to another
        totalDist[start_node].append(
            graph.get_shortest_path(start_node, end_node)[1:])


for node, total_distt in totalDist.items():

    total_dist = 0
    for l in total_distt:
        total_dist += len(l)
    closeness_centrality = (len(graph) - 1) / total_dist
    node_str = "Node " + str(node) + ":"
    formula_str = "$$\\text{Closeness centrality} = \\frac{" + str(len(graph)) + "-1}{" + str(total_dist) + "} \\implies \\frac{" + str(
        len(graph)-1) + "}{" + str(total_dist) + "} \\implies " + str(round(closeness_centrality, 2)) + "$$"
    #print(node_str, "Closeness centrality =" , formula_str, "=>", closeness_centrality)

    node_str = "**Node " + str(node) + "**"

    print(node_str, ": Shortest path to each node:\n\n")
    for p in total_distt:
        print("Path from", node, "to", p[len(p)-1], "=", p, "=", len(p))
        print()

    print("Total length:", total_dist)
    print(formula_str)
