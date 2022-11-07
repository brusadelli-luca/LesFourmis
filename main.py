from functions import *
from graph import *

anthill = 3

anthills_names = {1 : '../Fourmilieres/fourmiliere_un.txt', \
                    2 : '../Fourmilieres/fourmiliere_deux.txt', \
                    3 : '../Fourmilieres/fourmiliere_trois.txt', \
                    4 : '../Fourmilieres/fourmiliere_quatre.txt', \
                    5 : '../Fourmilieres/fourmiliere_cinq.txt' \
                       }

file_name = anthills_names[anthill]

param = import_data(file_name)

ant_nb = param[0]
node_nb = param[1]
node_list = param[2]
edge_nb = param[3]
edge_list = param[4]

graph(ant_nb, node_list, edge_list)
