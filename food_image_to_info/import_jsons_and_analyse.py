import os
import json
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import plotly.graph_objects as go



def list_files(directory):
    for entry in os.listdir(directory):
        full_path = os.path.join(directory, entry)
        if os.path.isfile(full_path):
            yield full_path


## import json file as dictionary
def import_json(filename):
    with open(filename) as json_file:
        data = json.load(json_file)
    return data

from collections import Counter 



def plot_bar(list_of_tuples, name):
        """Plot a bar chart from a Python Counter.

        Args:
            counter: A Python Counter object.

        Returns:
            A matplotlib bar chart.
        """

        # Get the keys and values from the Counter.
        names = [d[0] for d in list_of_tuples]
        heights = [d[1] for d in list_of_tuples]

        # # Create the bar chart.
        # sns.barplot(x=names, y=heights)
        # plt.xlabel("Name", fontsize=14)
        # plt.ylabel("Number of mentions", fontsize=14)
        # plt.xticks(rotation=45)
        # plt.yticks(np.arange(0, max(heights) + 1, 1))
        # plt.savefig(name)
        # plt.clf()

        fig = go.Figure(data=[go.Bar(x=names, y=heights)])
        fig.update_layout(title=name, xaxis_title="Name", yaxis_title="mentions")
        #fig.show()
        fig.write_image(name)



def run():

    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--folder_path", type=str, required=True)
    
    args = parser.parse_args()
    folder_path = args.folder_path
    hash_list = []
    countries_list = []
    ingredients_list = []
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