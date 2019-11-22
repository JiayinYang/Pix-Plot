import json
import numpy as np
from os.path import join
import os


path = '/Users/jenny/Desktop/pix-plot/utils/coordinate.json' 
centroid_json = []
result = []
centroid = np.zeros((1623,2))
with open(path) as f:
  data = json.load(f)
for item in range(len(data["nodes"])):
  cluster = data["nodes"][item]["attributes"]["cluster"]
  centroid[int(cluster)][0] = centroid[int(cluster)][0] + data["nodes"][item]["x"]
  centroid[int(cluster)][1] = centroid[int(cluster)][1] + data["nodes"][item]["y"]
for i in range(1623):
  x = centroid[i,0]/1623
  y = centroid[i,1]/1623
  dist = float("inf")
  img = []
  rep = []
  for item in range(len(data["nodes"])):
    dist1 = (x - data["nodes"][item]["x"])**2 + (y - data["nodes"][item]["x"])**2
    if (int(data["nodes"][item]["attributes"]["cluster"]) == int(i)):
      if (dist1 <= dist):
        name = data["nodes"][item]["label"]
        rep = name
        dist = dist1
      #print("here")
      name = data["nodes"][item]["label"]
      img.append(name)
      centroid_json.append({'id':name}) #id
      
  result.append({'list':centroid_json,
                  'rep':os.path.splitext(rep)[0]})
  centroid_json = []
 
  #centroid_json.append({
   # 'rep': os.path.splitext(rep)[0],
    #'img': img,
    #'label': 'Cluster ' + str(i)
 # })

  

with open('classification.json', 'w') as f:
  json.dump(result, f)