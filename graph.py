import networkx as nx
import matplotlib.pyplot as plt

#debut de la fonction graph et de la creation des fourmis
def graph(ant_nb, node_list, edge_list):
    class fourmis :
        def __init__(self, name):
            self.name = name
            self.position = self.position()
            self.taille = 1

        def position (self):
            position = 'Sv'
            return position
    
    chemin = nx.Graph()
    
    the_ants = []
    for index in range (ant_nb):
        f = "f",index
        # the_ants.append(f) 
        ant = fourmis(f)
        the_ants.append(ant)
        
        #debut de la fourmiliere
    chemin.add_nodes_from(node_list)
    
    for i in node_list:
        if i == 'Sv':
            chemin.nodes[i]['capacity'] =ant_nb
            chemin.nodes[i]['ants'] =ant_nb
            
        elif i == 'Sd':
            chemin.nodes[i]['capacity'] =ant_nb
            chemin.nodes[i]['ants'] = 0
            
        else:
            chemin.nodes[i]['capacity'] = 1
            chemin.nodes[i]['ants'] = 0

    #  chemin.nodes['Sv']['fourmis']= 10
    # chemin.nodes['S1']['fourmis']= 1
    # chemin.nodes['S2']['fourmis']= 1
    # chemin.nodes['Sd']['fourmis']= 10
    
    print(chemin._node)

    chemin.add_edges_from(edge_list)
   
    # chemin.add_nodes_from([
    #     (1,{"salle":"vestibule"}),
    #     (2,{"salle":"s1"}),
    #     (3,{"salle":"s2"}),
    #     (4,{"salle":"dortoir"})
    # ])

    # chemin.add_edges_from([(1,2),(2,3),(3,4)])

    #creation du fichier image
    nx.draw(chemin, with_labels=True, font_weight='bold')
    plt.show() 
    print(chemin)
    
    etape = 0
    route = []
    
#bloucle fourmis.
    etape = 0
    for ant in the_ants:
    
        etape = etape + 1
        
        print("----------------------------------")
        print("------------é","etape ",etape,"é---------------")
        print("----------------------------------------------")
        print("**********************************")
        
        for route in chemin:
            print(ant.name," arrive a" , route)