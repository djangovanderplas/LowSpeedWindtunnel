""" 
What does the program do?
    It reads all the raw thermal imaging data, averages it out and makes a 
    thermal image of this average data
How to use: 
    1. Put the python file in the same directory as all the 2D or 3D subdata
       i.e. .\2D\put_file_here
    2. Run the python file on the condition that you have the libraries installed
    3. It will create figures and put them into the !images folder in the same
       path.
"""

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

try:
    os.mkdir(".\\!images")
    print("Making file \"!images\" in same directory")
except:
    print("File already exists")
def get_paths():
    for root, dirs, path in os.walk("."):
        filenames = []
        for file in path:
            filenames.append(file)
        # yield because to iterate over each folder like a generator object
        yield root, filenames


def get_data(path):
    # Header = None so it does not skip the first line (there is no header)
    data = pd.read_csv(path, ";", header=None)
    # The last column is read as NaN, so it needs to be deleted
    data = data.drop(columns = data.columns[-1])
    data = data.to_numpy()
    return data

def get_average_data(paths):
    total_data = np.zeros(np.shape(get_data(paths[0])))
    n = 0
    for path in paths:
        data = get_data(path)
        total_data += data
        n+=1
    total_data /= n
    return(total_data)

for root, filenames in get_paths():
    paths = []
    foldername = root[2:]
    for filename in filenames:
        if filename[-4:] == ".csv":
            paths.append(root + "\\" + filename)
    if paths != []:
        data = get_average_data(paths)
        
        plt.imshow(data, cmap ='hot', interpolation = 'None')
        plt.title(f"Hotspot temperature [C]: {round(np.amax(data), 2)}")
        plt.colorbar()
        plt.savefig(f'!images\\thermalimage{foldername}.png')
        plt.close()
