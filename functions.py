import pandas
import numpy

# Data file parcing
def import_data(file_name):

    data = pandas.read_table(file_name,header=None)
    data = data.to_numpy()

    # Get ant number
    ant_nb = int(str(data[0][0]).split('=')[-1])

    # Get node number
    for cell in data:

        if '-' in str(cell):

            node_nb = int(numpy.where(data==cell)[0]) - 1 + 2
            break


    # Get node list with names
    node_list = ['Sv']

    for i in range(1, node_nb - 1):
        node_list.append(data[i][0])  
    
    node_list.append('Sd')

    # Get edge number
    edge_nb = data.shape[0] - node_nb - 1 + 2

    # Get edge list with names and ' - ' separator
    edge_list = []

    for i in range(1 + node_nb - 2, data.shape[0]):
        edge = data[i][0].split(' - ')
        edge = (edge[0], edge[1])
        edge_list .append(edge)

    return(ant_nb, node_nb, node_list, edge_nb, edge_list)