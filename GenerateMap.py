import svgwrite
import numpy as np
import json

COLOR = "red"
R = 5

Y = 600.81262
X = 1404.7773


#Read the json file
with open('countries.json', 'r') as f:
    data = json.load(f)
N = len(data["countries"])

#Add the points in the map
dwg = svgwrite.Drawing('FinalMap.svg')
im = svgwrite.image.Image("Map.svg", size = [X, Y])
dwg.add(im)

for i in range(N):
    if(data["countries"][i]["visited"]):
        c = svgwrite.shapes.Circle(center=(data["countries"][i]["x"]*X/100, data["countries"][i]["y"]*Y/100), r=R, fill=COLOR)
        dwg.add(c)

dwg.save()

#Add the countries in the markdown list
with open('ListCountries.md', 'w') as f:
    for i in range(N):
        strike = ""
        if(data["countries"][i]["visited"]):
            strike = "~~"
        f.write("- " + strike + data["countries"][i]["country"] + strike +"\n")





