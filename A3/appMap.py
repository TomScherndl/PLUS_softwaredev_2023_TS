#%%
import osmnx as ox
import folium
#from sklearn.neighbors import BallTree
import numpy as np
import pandas as pd

#%%
# return edge IDs that do not match passed list of hwys
def find_edges(G, hwys):
    edges = []  # initialize an empty list that is filled 
     
    for u, v, k, data in G.edges(keys = True, data = 'highway'):
        # there are 2 checks: 1) check1: 
        check1 = isinstance(data, str) and data not in hwys
        check2 = isinstance(data, list) and all([d not in hwys for d in data])
        # if either check1 or check2 is true, add the edge to our object for later plotting!
        if check1 or check2:
            edges.append((u, v, k))
    return set(edges) # using set to only return unique items

# function to get the nearest edge based on given longitude/latitude
def get_nearest(src_points, candidates, k_neighbors=1):
    """Find nearest neighbors for all source points from a set of candidate points"""

    # Create tree from the candidate points
    tree = BallTree(candidates, leaf_size=15, metric='haversine')

    # Find closest points and distances
    distances, indices = tree.query(src_points, k=k_neighbors)

    # Transpose to get distances and indices into arrays
    distances = distances.transpose()
    indices = indices.transpose()

    # Get closest indices and distances (i.e. array at index 0)
    # note: for the second closest points, you would take index 1, etc.
    closest = indices[0]
    closest_dist = distances[0]

    # Return indices and distances
    return (closest, closest_dist)

# define overall place of data
place = 'salzburg, austria'

# define filter: use only highways (=roads) that have the following attribute/value
filter = '["highway"~"primary|secondary|tertiary|residential|cycleway|living street|pedestrian"]'

# define the colors to use for different edge types
hwy_colors = {'footway': 'skyblue',
              'residential': 'paleturquoise',
              'cycleway': 'orange',
              'living street': 'lightgreen',
              'secondary': 'grey',
              'pedestrian': 'lightskyblue'}

#%%
##### plot the graph

G = ox.graph_from_place(place, network_type='bike', 
                        custom_filter = filter)

# first plot all edges that do not appear in hwy_colors's types
G_tmp = G.copy()
G_tmp.remove_edges_from(G.edges - find_edges(G, hwy_colors.keys()))
m = ox.plot_graph_folium(G_tmp, popup_attribute='highway', weight=5, color='black')

# then plot each edge type in hwy_colors one at a time
for hwy, color in hwy_colors.items():
    G_tmp = G.copy()
    G_tmp.remove_edges_from(find_edges(G_tmp, [hwy]))
    
    # if G has some edges, then plot it using plot_graph_folium
    if G_tmp.edges:
        m = ox.plot_graph_folium(G_tmp,
                                 graph_map = m,
                                 popup_attribute = 'highway',
                                 weight = 5,
                                 color = color)
#%%
print("Now creating the map!")
m