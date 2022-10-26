from functions import *
from graph import *

anthill = 4

anthills_names = {1 : '../Fourmilieres/fourmiliere_un.txt', \
                    2 : '../Fourmilieres/fourmiliere_deux.txt', \
                    3 : '../Fourmilieres/fourmiliere_trois.txt', \
                    4 : '../Fourmilieres/fourmiliere_quatre.txt', \
                    5 : '../Fourmilieres/fourmiliere_cinq.txt' \
                       }

file_name = anthills_names[anthill]

param = import_data(file_name)

node_list = [*range(4)]

edge_list = name_to_index(param[2],param[4])
print(param[2],edge_list)

graph( node_list,edge_list)
