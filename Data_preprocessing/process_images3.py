import json
import numpy as np
from os.path import join
import os

def intersection(lst1, lst2): 
    return list(set(lst1) & set(lst2)) 

path = '/Users/jenny/Desktop/pix-plot-masterv2/utils/classification.json' 
centroid_json = []
centroid = np.zeros((1623,2))
with open(path) as f:
  data = json.load(f)

newlist = []
result = []
for item in range(len(data)):
	
	cluster = data[item]['list']
	f = open ("adjacency-list.csv", "r")
	for item1 in range(len(cluster)):
		for line in f:
			elements = line.split(',')

			if cluster[0] == elements[0]:
				target = cluster[0]
				cluster.pop(0)
				elements.pop(0)
				newele = []
				weight = []
				for ele in range(len(elements)):
					tmp = elements[ele].split('\n')
					tmp = tmp[0].split(' ')
					newele.append(tmp[0])
					weight.append(tmp[1])
				intersect = intersection(cluster,newele)
				index = []
				for ele in range(len(elements)):
					tmp = elements[ele].split(' ') 
					for ele1 in range(len(intersect)):
						if tmp[0] == intersect[ele1]:
							index.append(weight[ele]) 

				for ele in range(len(intersect)):
					centroid_json.append({
    					'a': target,
    					'b': intersect[ele],
    					'c': index[ele]
    				
  					})
  				#with open('link.json', 'w') as file:
  				#	json.dump(centroid_json, file)
				break
	result.append({'list':centroid_json})
	centroid_json = []
with open('link.json', 'w') as file:
  	json.dump(result, file)	

	
