import svgwrite
import numpy as np
import json
import xml.etree.ElementTree as ET
 

COLOR_VISITED = "#ff0000"
COLOR_NOT_VISITED = "#d3d2d1"


#Read the json file
with open('countries.json', 'r') as f:
    data = json.load(f)
N = len(data["countries"])


#Add the countries in the markdown list
with open('ListCountries.md', 'w') as f:
    for i in range(N):
        strike = ""
        if(data["countries"][i]["visited"]):
            strike = "~~"
        f.write("- " + strike + data["countries"][i]["country"] + strike +"\n")


#Color the map
tree = ET.parse('Map.svg')
root = tree.getroot()

for child in root[0]:
    #print(child.tag, child.attrib)
    countryId = child.get('id')
    if len(countryId)==2:
        #print(countryId) 
        for i in range(N):
            if data["countries"][i]["id"] == countryId:
                print(countryId)
                if data["countries"][i]["visited"]:
                    child.set('style', 'fill:' + COLOR_VISITED) 
                else:
                    child.set('style', 'fill:' + COLOR_NOT_VISITED) 
                break

tree.write('FinalMap.svg')