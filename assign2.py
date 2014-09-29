# -*- coding: utf-8 -*-
"""
Created on Sat Sep 20 01:46:20 2014

@author: Eric
"""

import provided_code2 as provided
import random
import time
import math
import matplotlib.pyplot as plt
import proj1
import proj2
NETWORK_URL = "http://storage.googleapis.com/codeskulptor-alg/alg_rf7.txt"


def make_random_ugraph(num_nodes, prob):
    """
    output: creates random undirected graph, no self loop
    input: num_nodes = # of nodes, prob = probability of edge
    """
    ran_ugraph = {}
    for key in range(num_nodes):
        ran_ugraph[key]=set([])
    for row in range(num_nodes):
        for col in range(row):
            rand = random.random()
            if rand < prob:
                 ran_ugraph[row] = ran_ugraph[row].union([col])
                 ran_ugraph[col] = ran_ugraph[col].union([row])
    return ran_ugraph


def make_upa_graph(num_nodes, mstart):
    """
    output: a random undirected graph created by adding nodes with random
    m edges to a completed graph
    input: num_nodes=total nodes of final graph, mstart=nodes of initial complete graph    
    """    
    V = range(mstart)
    E = proj1.make_complete_graph(mstart)
    
    "initialize pool of nodes to create edges with. Created by summing  in-degree"
    "nodes of all nodes of complete graph"
    population = V*len(V)
    
    "add new nodes from mstart+1 to num_nodes - randomly create up to mstart edges"
    for new_node in range(mstart,num_nodes):
        new_node_edges = []    
        for idx in range(mstart):
            new_node_edges.append(random.choice(population))
        new_node_edges = set(new_node_edges)
        population.append(new_node)
        population.extend(new_node_edges)
        V.append(new_node)
        E[new_node] = new_node_edges
        for edge in new_node_edges:
            E[edge] = E[edge].union([new_node])
    return E
    



computer_network = provided.load_graph(NETWORK_URL)
ER = make_random_ugraph(1347, 0.00343)
UPA = make_upa_graph(1347, 2)

attack_orderCN = range(1347)
random.shuffle(attack_orderCN)

attack_orderER = range(1347)
random.shuffle(attack_orderER)

attack_orderUPA = range(1347)
random.shuffle(attack_orderUPA)


comp_resile = proj2.compute_resilience(computer_network, attack_orderCN)
ER_resile = proj2.compute_resilience(ER, attack_orderER)
UPA_resile = proj2.compute_resilience(UPA, attack_orderUPA)


xvals = range(1348)


plt.plot(xvals, comp_resile, '-b', label='Computer Network')
plt.plot(xvals, ER_resile, '-r', label='ER graph, P=0.0343')
plt.plot(xvals, UPA_resile, '-g', label='UPA graph, m=2')
plt.legend(loc='upper right')
plt.title("Plot of Resilience")
plt.ylabel("Size of Largest Connected Component")
plt.xlabel("Nodes Removed")
plt.show()

