import networkx as nx
import matplotlib.pyplot as plt


def graph(node_list,edge_list):
    chemin = nx.Graph()
    
    
    if node_list is [0] and node_list[-1]:
        chemin.add_nodes_from(node_list, fourmis = 10)
    else :
        chemin.add_nodes_from(node_list, fourmis = 1)

    chemin.add_edges_from(edge_list)
    """
    chemin.add_nodes_from([
        (1,{"salle":"vestibule"}),
        (2,{"salle":"s1"}),
        (3,{"salle":"s2"}),
        (4,{"salle":"dortoir"})
    ])

    chemin.add_edges_from([(1,2),(2,3),(3,4)])
    """

    nx.draw(chemin, with_labels=True, font_weight='bold')
    plt.show() 
