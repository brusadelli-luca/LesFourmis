import networkx as nx
import matplotlib.pyplot as plt

chemin = nx.Graph()

chemin.add_nodes_from([
    (1,{"salle":"vestibule"}),
    (2,{"salle":"s1"}),
    (3,{"salle":"s2"}),
    (4,{"salle":"dortoir"})
])

chemin.add_edges_from([(1,2),(2,3),(3,4)])

nx.draw(chemin, with_labels=True, font_weight='bold')

print(chemin)
plt.show() 