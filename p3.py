import math
import random
import time
from bokeh.plotting import figure, show
import networkx as netx
import matplotlib.pyplot as plt

 
random_values = [15,20,30,40,50]

lst_cost_of_initial_graph = []
lst_cost_of_alg1 = []
lst_cost_of_alg2= []
time_for_alg1 = []
time_for_alg2 = []

def calculate_cost(graph):
    cost_of_edge = {}
    total = 0
    for edge in graph.edges():
        node1 = edge[0]
        node2 = edge[1]
        a=(coordinates[node2][1]-coordinates[node1][1])
        a=a**2
        b=(coordinates[node2][0]-coordinates[node1][0])
        b=b**2
        to_take_sqroot=math.sqrt(a+b)
        cost_of_edge[edge] = round(to_take_sqroot,0)
        total+=cost_of_edge[edge]
    return cost_of_edge,total


def print_all_the_edge_cost(cost):
    print("Printing the edges and their respective cost")
    for edge,cost in cost.items():
        print(f"Edge: {edge} \t Cost: {cost}")


count=0

def initialize_cost(cost):
        for edge in cost:
            graph[edge[0]][edge[1]]['weight'] = cost[edge]
        costs = netx.get_edge_attributes(graph,'weight')
        return(costs)

cost1 = {}
total_cost1 = 0
def alg1_print_statements2(graph):
    # cost1 = {}
    # print(f"after algorithm 1 {len(graph_checking.edges)}")
    # total_cost1 = 0
    cost1,total_cost1 = calculate_cost(graph)
    print("\n\n\nAfter implementing algorithm 1 \n")
    print_all_the_edge_cost(cost1)
    lst_cost_of_alg1.append(total_cost1)
    print("Total cost of the network is", total_cost1)
    print("\n\n\n\n")

def alg1_print_statements(graph):
    degree = [d for (node,d) in graph.degree()]
    print("\n\n")
    print("Degree of each node after implementing Algorithm 1:", degree)
    print("No of edges after implementing Algorithm 1:",graph.number_of_edges())

# def alg2_innerloop(graph_alg2,lst_index_final,n):
#     for e in lst_index_final[n]:
#         if(e in graph_alg2.edges):
#             graph_alg2.remove_edge(*e)
#             if(netx.is_connected(graph_alg2)):
#                 diameter = netx.diameter(graph_alg2,e=None)
            
#                 if diameter<=4 and all(alg2_check_degree(graph_alg2)):
#                     continue                #continue removing the edge if the conditions are met
#                 else:
#                     graph_alg2.add_edge(*e)   #add back the edge if the conditions fail
#     return(graph_alg2)

def alg2_print_statements2(graph_alg2):
    cost2,total_cost2 = calculate_cost(graph_alg2)
    
    print_all_the_edge_cost(cost2)
    lst_cost_of_alg2.append(total_cost2)
    print("Total cost of the network is", total_cost2)
    # print("\n\n\n\n")


def alg2_print_statements(graph_alg2):
    degree = [d for (node,d) in graph_alg2.degree()]
    if(netx.is_connected(graph_alg2)):
        print("Degree of each node after implementing Algorithm 2:", degree)
        print("No of edges after implementing Algorithm 2:",graph_alg2.number_of_edges())

def initial_graph_creation(graph):
    return (d>2 for (n,d) in graph.degree())

def alg2_check_degree(graph):
    return (d>2 for (n,d) in graph.degree())

def alg1_check_degree(graph):
    return (d>2 for (n,d) in graph.degree())


def edge_checking_innerloop(n,graph):
    for edge in list(graph.edges([n])):
    # print(list(graph.edges([n])))  
        graph.remove_edge(*edge)
        if(netx.is_connected(graph)):
            diameter = netx.diameter(graph,e=None)
        
            if diameter<=4 and all(alg1_check_degree(graph)):
                continue  
            else:
                graph.add_edge(*edge)   
    return graph

def edge_checking(graph):
    for n,d in graph.degree():
# print(n,d)
        if d>3:
            graph=edge_checking_innerloop(n,graph)
    return graph
# print(count1)

def print_coordinates(coordinates):
    print("Printing node coordinates")
    for key,value in coordinates.items():
        x,y = value
        print(f"Vertex: {key} \t coordinates {x,y}")

# def alg2_traverse_lst_creation():
#     lst_temp=[]
#     lst_temp2=[]
#     # graph.remove_edge(*graph.edges([n][0]))
#     lst_calc=[]
#     lst_index=[]
#     for n,d in graph_alg2.degree():
#         if d>3:
#             d_temp=d
#         # print(graph.edges([n]))
#         for e in (graph_alg2.edges([n])):
#         #     print(e)
#             # graph.remove_edge(*e)
#             # break
#         # break
#             if(e in cost):
#                 i,j=e
#                 lst_temp.append(cost[e])
#                 lst_temp2.append(e)
#                 # print(e, cost[e])
#                 # print(cost[e])
        
#         lst_calc.append(lst_temp)
#         lst_temp=[]
#         lst_index.append(lst_temp2)
#         lst_temp2=[]
#             # else:
#             #     i,j=e
#             #     print(cost[(j,i)])
#     # print(graph.edges)
#     # if([] in lst_calc):
#     #     lst_calc.remove([])
#     # if([] in lst_index):
#     #     lst_index.remove([])
#     # print(lst_calc)
#     # print("\n\n")
#     # print(lst_index)
#     # print("\n\n")
#     return(lst_calc,lst_index)



flag=-1
for m in random_values:
    graph = netx.Graph()
    while(True):
        for n in range(m):
            
            graph.add_node(n,pos=(n+random.randint(n,100),n+random.randint(100,200)))

        if(m%2==0):
            for i in range(0,m-2,2):
                graph.add_edge(i,i+2)
            for i in range(1,m-3,2):
                graph.add_edge(i,i+2)
            graph.add_edge(1,m-1)
            graph.add_edge(0,m-2)
            graph.add_edge(0,m-2)
            graph.add_edge(1,m-1)
        if(m%2!=0):
            for i in range(0,m-3,2):
                graph.add_edge(i,i+2)
            for i in range(1,m-2,2):
                graph.add_edge(i,i+2)
            a=random.randrange(1, m, 2)
            b=random.randrange(0,m-1, 2)
            graph.add_edge(1,m-1)
            graph.add_edge(0,m-2)
            graph.add_edge(0,m-2)
            graph.add_edge(1,m-1)
            if(a!=b):
                graph.add_edge(a,b)
        for i in range(m-1):
            graph.add_edge(i,i+1)
        a=random.randint(0,m-1)
        b=random.randint(0,m-1)
        if(a!=b):
            graph.add_edge(a,b)
        a=random.randint(0,m-1)
        b=random.randint(0,m-1)
        if(a!=b):
            graph.add_edge(a,b)
        graph.add_edge(random.randint(0,m-1),random.randint(0,m-1))
        graph.add_edge(random.randint(0,m-1),random.randint(0,m-1))
        graph.add_edge(random.randint(0,m-1),random.randint(0,m-1))
        graph.add_edge(random.randint(0,m-1),random.randint(0,m-1))
        graph.add_edge(random.randint(0,m-1),random.randint(0,m-1))
        graph.add_edge(random.randint(0,m-1),random.randint(0,m-1))
        graph.add_edge(random.randint(0,m-1),random.randint(0,m-1))
        graph.add_edge(random.randint(0,m-1),random.randint(0,m-1))
        
        graph.add_edge(random.randint(0,m-1),random.randint(0,m-1))
        graph.add_edge(random.randint(0,m-1),random.randint(0,m-1))
        graph.add_edge(random.randint(0,m-1),random.randint(0,m-1))
        graph.add_edge(random.randint(0,m-1),random.randint(0,m-1))
        graph.add_edge(random.randint(0,m-1),random.randint(0,m-1))
        graph.add_edge(random.randint(0,m-1),random.randint(0,m-1))
        graph.add_edge(random.randint(0,m-1),random.randint(0,m-1))
        graph.add_edge(random.randint(0,m-1),random.randint(0,m-1))



        diameter = netx.diameter(graph, e=None)
        if(netx.is_connected(graph)):
            if diameter <= 4 and all(initial_graph_creation(graph)):
                # print("TRUE")
                flag=1
                count=0
                break
            count+=1
            if(count>50):
                graph.clear()

    print("Printing graph with ", m , "nodes")
    plt.figure(figsize = (12,12))
    coordinates = netx.get_node_attributes(graph,'pos')
    print_coordinates(coordinates)
    
    plt.title("Network topology")
    netx.draw_networkx_nodes(graph,coordinates)
    netx.draw_networkx_edges(graph,coordinates)
    netx.draw_networkx_labels(graph,coordinates)
    plt.show()


    
    cost,total_cost = calculate_cost(graph)     
    print_all_the_edge_cost(cost)
    lst_cost_of_initial_graph.append(total_cost)
    print(f"Total cost of the network is:- {total_cost}")
    

    #
    
    costs=initialize_cost(cost)

    #


    graph_alg2 = netx.Graph()
    graph_alg2 = graph.copy()
    graph_checking = netx.Graph()
    print(f"No of edges before implementing algorithm 1: {len(graph.edges)}")



    #algorithm 1

    count1=0
    start_time_for_alg1 = time.time()
    graph.remove_edges_from(netx.selfloop_edges(graph))
    graph_checking=edge_checking(graph)

    end_time_for_alg1 = time.time()
    time_for_alg1.append(end_time_for_alg1-start_time_for_alg1)
    costs = netx.get_edge_attributes(graph_checking,'weight')
    plt.figure(figsize = (12,12))
    coordinates = netx.get_node_attributes(graph_checking,'pos')

    #display graph

    plt.title("Network topology for Algorithm 1")
    netx.draw_networkx_nodes(graph_checking,coordinates)
    netx.draw_networkx_edges(graph_checking,coordinates)
    netx.draw_networkx_labels(graph_checking,coordinates)
    plt.show()

    alg1_print_statements(graph_checking)
    alg1_print_statements2(graph_checking)


    
    #algorithm 2



    # graph_alg2.remove_edges_from(netx.selfloop_edges(graph))
    # graph.remove_edge(1,0)

    # graph.remove_edge(2,0)
    # # graph.remove_edge(3,0)
    # graph.remove_edge(2,1)
    # graph.remove_edge(3,1)
    # graph.remove_edge(3,2)
    # graph.remove_edge(4,2)
    # graph.remove_edge(5,3)
    # graph.remove_edge(4,3)
    # graph.remove_edge(5,4)
    # graph.remove_edge(6,4)
    # graph.remove_edge(6,5)
    

    # print(graph.edges)
    lst_temp=[]
    lst_temp2=[]
    lst_calc=[]
    lst_index=[]

    # for n,d in graph_alg2.degree():
    #     if d>3:
    #         d_temp=d
    #     # print(graph.edges([n]))
    #     for e in (graph_alg2.edges([n])):
    #     #     print(e)
    #         # graph.remove_edge(*e)
    #         # break
    #     # break
    #         if(e in cost):
    #             i,j=e
    #             lst_temp.append(cost[e])
    #             lst_temp2.append(e)
    #             # print(e, cost[e])
    #             # print(cost[e])
        
    #     lst_calc.append(lst_temp)
    #     lst_temp=[]
    #     lst_index.append(lst_temp2)
    #     lst_temp2=[]
    #         # else:
    #         #     i,j=e
    #         #     print(cost[(j,i)])
    # # print(graph.edges)
    # # if([] in lst_calc):
    # #     lst_calc.remove([])
    # # if([] in lst_index):
    # #     lst_index.remove([])
    # # print(lst_calc)
    # # print("\n\n")
    # # print(lst_index)
    # # print("\n\n")

    # print(sorted(list(cost.items())))
    lst_index_temp_final=[]
    lst_index_final=[]
    new_lst=[]

    # lst_calc,lst_index=alg2_traverse_lst_creation
    for n,d in graph_alg2.degree():
        if d>3:
            d_temp=d
        # print(graph.edges([n]))
        for e in (graph_alg2.edges([n])):
        #     print(e)
            # graph.remove_edge(*e)
            # break
        # break
            if(e in cost):
                i,j=e
                lst_temp.append(cost[e])
                lst_temp2.append(e)
                # print(e, cost[e])
                # print(cost[e])
        
        lst_calc.append(lst_temp)
        lst_temp=[]
        lst_index.append(lst_temp2)
        lst_temp2=[]
            # else:
            #     i,j=e
            #     print(cost[(j,i)])
    # print(graph.edges)
    # if([] in lst_calc):
    #     lst_calc.remove([])
    # if([] in lst_index):
    #     lst_index.remove([])
    # print(lst_calc)
    # print("\n\n")
    # print(lst_index)
    # print("\n\n")

    # dict=cost
    # print(dict)
    for i in lst_calc:
        new_lst.append(sorted(i, reverse=True))

    # print(new_lst)
    # print("\n\n\n")
    for i in range(len(new_lst)):
        for j in range(len(new_lst[i])):
            # print(new_lst[i][j])
            for k in cost:
                a,b=k
                # print(cost)
                # print(a,b,k)
                # print(new_lst[i][j])
                # print(cost[k])
                # if(new_lst[i][j] in cost and a==i):
                if(new_lst[i][j]==cost[k] and a==i):
                    lst_index_temp_final.append(k)
                    # print("true")
                    break
                    # print(e)
        lst_index_final.append(lst_index_temp_final)
        lst_index_temp_final=[]
    # print(lst_index_final)
        
    # print(cost)
    # print("\n\n\n")



    start_time2 = time.time()
    for node,d in graph_alg2.degree():
        if d>3:
           for edge in lst_index_final[node]:
            if(edge in graph_alg2.edges):
                graph_alg2.remove_edge(*edge)
                if(netx.is_connected(graph_alg2)):
                    diameter = netx.diameter(graph_alg2,e=None)
                
                    if diameter<=4 and all(alg2_check_degree(graph_alg2)):
                        continue                
                    else:
                        graph_alg2.add_edge(*edge)   
        else:
            continue       

    
    end_time2 = time.time()
    time_for_alg2.append(end_time2-start_time2)

    # p1 = figure(title="Time Comparison", x_axis_label="no of nodes", y_axis_label="total cost")

    # p1.line(random_values, time_for_alg1, legend_label="Algorithm 1", color="blue", line_width=2)
    # p1.line(random_values, time_for_alg2, legend_label="Algorithm 2", color="red", line_width=2)
    # show(p1)

    plt.figure(figsize = (10,10))
    coordinates = netx.get_node_attributes(graph_alg2,'pos')
    
    

    #display graph for algorithm 2
    
    plt.title("Network topology for Algorithm 2")
    netx.draw_networkx_nodes(graph_alg2,coordinates)
    netx.draw_networkx_edges(graph_alg2,coordinates)
    netx.draw_networkx_labels(graph_alg2,coordinates)
    plt.show()

    alg2_print_statements(graph_alg2)
    alg2_print_statements2(graph_alg2)

# if(z==1):
#     p1 = figure(title="Time Comparison", x_axis_label="no of nodes", y_axis_label="total cost")

#     p1.line(random_values, time_for_alg1, legend_label="Algorithm 1", color="blue", line_width=2)
#     p1.line(random_values, time_for_alg2, legend_label="Algorithm 2", color="red", line_width=2)
#     show(p1)
#     z+=1

import numpy as np
import matplotlib.pyplot as plt

X = random_values



X_axis = np.arange(len(X))

plt.bar(X_axis - 0.2, time_for_alg1, 0.4, label = 'alg1')
plt.bar(X_axis + 0.2, time_for_alg2, 0.4, label = 'alg2')

plt.xticks(X_axis, X)
plt.xlabel("nodes")
plt.ylabel("Time")
plt.title("Time Comparison")
plt.legend()
plt.show()

# print("\n\n")
# print(random_values)
# print("\n\n")
# print(lst_cost_of_initial_graph)
# print("\n\n")
# print(lst_cost_of_alg1)
# print("\n\n")
# print(lst_cost_of_alg2)


#display cost and time comparison

p = figure(title="Cost Comparison", x_axis_label="no of nodes", y_axis_label="total cost")

p.line(random_values, lst_cost_of_initial_graph, legend_label="Initial cost", color="blue", line_width=2)
p.line(random_values, lst_cost_of_alg1, legend_label="Algorithm 1", color="red", line_width=2)
p.line(random_values, lst_cost_of_alg2, legend_label="Algorithm 2", color="green", line_width=2)
show(p)


# p1 = figure(title="Time Comparison", x_axis_label="no of nodes", y_axis_label="total cost")

# p1.line(random_values, time_for_alg1, legend_label="Algorithm 1", color="blue", line_width=2)
# p1.line(random_values, time_for_alg2, legend_label="Algorithm 2", color="red", line_width=2)
# show(p1)


                    

