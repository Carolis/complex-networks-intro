#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 13 23:54:05 2025

@author: Carolina Ale
"""

import networkx as nx
import matplotlib.pyplot as plt

eNe = 10

# Creating a complete graph (all nodes connected)
G = nx.complete_graph(eNe)

# Drawing the graph
plt.figure(figsize=(8, 6))
nx.draw(G, with_labels=True, node_color='lightblue', edge_color='gray', node_size=700, font_size=12)
plt.title(f'Complete graph with {eNe} nodes')
plt.show()