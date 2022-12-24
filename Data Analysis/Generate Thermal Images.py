""" 
What does the program do?
    It reads all the raw thermal imaging data, averages it out and makes a 
    thermal image of this average data
How to use: 
    1. Put the python file under the same folder as data is located
    2. Change settings to desired values
    3. Run code to generate images
    4. The images will either appear in !images2D or !images3D under the same
       folder the file is located in
"""

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Change these values if necessary
# -----------------------------------------------------------------------------
# If set to True all images will have same colorscale
set_absolute_colorscale = True
# Show colorbar on plot
set_colorbar = False
# Either analyze 2D or 3D case
analysiscase = "2D"
# Show hotspot
show_hotspot_temperature = True
# -----------------------------------------------------------------------------

if not set_colorbar:
    y_text = 0.1
else:
    y_text = 0.17
if set_absolute_colorscale:
    if analysiscase == "2D":
        colorscale = [13.5, 17.5]
    elif analysiscase == "3D":
        colorscale = [13.5, 19.5]
    else:
        print("error, analysiscase is neither \"2D\" or \"3D\"")

if not os.path.exists(f".\\!images{analysiscase}"):
    os.mkdir(f".\\!images{analysiscase}")


def get_paths():
    for root, dirs, path in os.walk(f".\\data\\{analysiscase}"):
        filenames = []
        for file in path:
            if file[0] == "-":
                file = '!' + file
            
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


lowest_low = 1e9
highest_high = -1e9
for root, filenames in get_paths():
    paths = []
    foldername = root.split("\\")[-1]
    for filename in filenames:
        if filename[-4:] == ".csv":
            paths.append(root + "\\" + filename)
    if paths != []:
        data = get_average_data(paths)
        highest_value = np.max(data)
        lowest_value = np.min(data)
        
        if highest_value > highest_high:
            highest_high = highest_value
        if lowest_value < lowest_low:
            lowest_low = lowest_value

        print(foldername)
        
        plt.imshow(data, cmap ='hot', interpolation = 'None')
        plt.title(f"Alpha: {foldername}", loc="left", family = "monospace")
            
        if set_colorbar:
            plt.colorbar()
        if set_absolute_colorscale:
            plt.clim(colorscale)
        if show_hotspot_temperature:
            plt.suptitle(f"Hotspot temperature: {round(highest_value, 2)}",\
                         x=0.305, y=y_text)
        # x and y axis make no sense for an image
        plt.gca().axes.get_yaxis().set_visible(False)
        plt.gca().axes.get_xaxis().set_visible(False)
        plt.savefig(f'!images{analysiscase}\\{foldername}.png', dpi=200)
        plt.close()

print("For absolute temperature scale:")
print("Highest recorded temperature, Lowest recorded temperature")
print(round(highest_high,2), ", ", round(lowest_low,2))
