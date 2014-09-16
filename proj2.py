# -*- coding: utf-8 -*-
"""
Created on Sun Sep 14 23:57:30 2014

@author: Eric
"""

from collections import deque as coll

def bfs_visited(ugraph, start_node):
    "returns the set of connected nodes containing start_node"
    que = coll()
    visited = {start_node}
    que.append(start_node)
    while (len(que) > 0):
        que_head = que.popleft()
        for each_node in ugraph[que_head]:
            if each_node not in visited:
                visited.add(each_node)
                que.append(each_node)
    return visited
        

def cc_visited(ugraph):
    "returns a list of connected components as sets"
    remaining_nodes = ugraph.keys()
    component_list = []
    while (len(remaining_nodes)>0):
        start_node = remaining_nodes[0]
        component = bfs_visited(ugraph, start_node)
        component_list.append(component)
        for node in component:
            remaining_nodes.remove(node)
    return component_list
    

def largest_cc_size(ugraph):
    "returns cardinality of largest connected component"
    graph_components = cc_visited(ugraph)
    cardinality = 0
    for component in graph_components:
        com_len = len(component)
        if com_len > cardinality:
            cardinality = com_len
    return cardinality


def compute_resilience(ugraph, attack_order):
    "returns a list of largers CC after removal of nodes in attack order"
    resilience = [largest_cc_size(ugraph)]
    for node in attack_order:
        popped = ugraph.pop(node)
        for edge in popped:
            ugraph[edge].discard(node)            
        resilience.append(largest_cc_size(ugraph))
    return resilience