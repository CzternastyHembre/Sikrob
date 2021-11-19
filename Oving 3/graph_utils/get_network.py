import random as r

def get_network(seed = 42):
    r.seed(seed)
    with open("graph_utils/real_graph_alternatives.txt","r") as f:
        graphs = f.readlines()
        g = graphs[r.randint(0,len(graphs)-1)]
        g_name = g.split(".")[0]
        print(f"You will analyze the {g_name} network.")
        print(f"Your network graph file is http://www.topology-zoo.org/files/{g}")
        return f"http://www.topology-zoo.org/files/{g}".strip("\n")
