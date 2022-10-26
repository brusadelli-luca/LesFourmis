import pandas
import numpy


def import_data(file_name):

    data = pandas.read_table(file_name,header=None)
    data = data.to_numpy()

    ant_nb = int(str(data[0][0]).split('=')[-1])

    for cell in data:

        if '-' in str(cell):

            node_nb = int(numpy.where(data==cell)[0]) - 1 + 2
            break

    node_list = ['Sv']

    for i in range(1, node_nb - 1):
        node_list.append(data[i][0])  
    
    node_list.append('Sd')

    edge_nb = data.shape[0] - node_nb - 1 + 2

    edge_list = []

    for i in range(1 + node_nb - 2, data.shape[0]):
        edge_list.append(data[i][0])  


    return(ant_nb, node_nb, node_list, edge_nb, edge_list)