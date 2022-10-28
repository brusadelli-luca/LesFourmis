import networkx as nx
import matplotlib.pyplot as plt

#debut de la fonction graph et de la creation des fourmis
def graph(ant_nb, node_list, edge_list):
    chemin = nx.Graph()
    ants = []
    for index in range (ant_nb):
        f = "f",index
        ants.append(f)  
        
        #debut de la fourmiliere
    chemin.add_nodes_from(node_list)
    
    for i in node_list:
        if i == 'Sv' or i ==  'Sd':
            chemin.nodes[i]['fourmiliere'] = 10

            chemin.nodes[i]['fourmiliere'] = 10
        else:
            chemin.nodes[i]['fourmiliere'] = 1 

    """ chemin.nodes['Sv']['fourmis']= 10
    chemin.nodes['S1']['fourmis']= 1
    chemin.nodes['S2']['fourmis']= 1
    chemin.nodes['Sd']['fourmis']= 10"""
    
    print(chemin._node)

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

    #creation du fichier image
    nx.draw(chemin, with_labels=True, font_weight='bold')
    plt.show() 
    print(chemin)
    
    for c in chemin:
        
        print("----------------------------------")
        print("------------étape 0---------------")
        print("**********************************")
        print(ants[0]," passe par" , c)
        print("**********************************")
    
    