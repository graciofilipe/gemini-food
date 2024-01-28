import os
import json
import matplotlib.pyplot as plt
import numpy as np
import plotly.graph_objects as go
from aux_functions import list_files, import_json

from collections import Counter 


def plot_bar(list_of_tuples, file_name):
        """save a bar chart from a list_of_tuples in the form (name, height).

        Args:
            list_of_tuples: list of tuples in the form (name, height).
            file_name: name of the bar chart.
        """

        # Get the keys and values from the Counter.
        names = [d[0] for d in list_of_tuples]
        heights = [d[1] for d in list_of_tuples]

        # # Create the bar chart.
        fig = go.Figure(data=[go.Bar(x=names, y=heights)])
        fig.update_layout(title=name, xaxis_title="Name", yaxis_title="mentions")
        fig.write_image(file_name)



def run():

    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--folder_path", type=str, required=True)
    
    args = parser.parse_args()
    folder_path = args.folder_path
    hash_list = []
    countries_list = []
    ingredients_list = []
    
    # capture the info from all jsons into single lists
    for file_name in list_files(folder_path):
        d = import_json(file_name)
        
        hash_list.extend([x.lower() for x in  d["hashtags"]])
        countries_list.extend([x.lower() for x in  d["countries"]])
        ingredients_list.extend([x.lower() for x in  d["ingredients"] if (x!= "salt" and x!= "Salt")])
    
    hash_counter = Counter(hash_list)
    countries_counter = Counter(countries_list)
    ingredients_counter = Counter(ingredients_list)
           
    plot_bar(hash_counter.most_common(8), "hash.png")
    plot_bar(countries_counter.most_common(8), "countries.png")
    plot_bar(ingredients_counter.most_common(8), "ingredients.png")


if __name__ == "__main__":
    run()