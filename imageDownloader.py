import pickle
import os
import urllib.request


coins = pickle.load(open("coins.pickle","rb"))

i = 0
for c in coins:
	directory = "coins/"+str(c[1])
	path = os.path.join(directory+"/"+str(c[1])+"_coin"+"_"+str(i)+".jpg")
	print(path)
	if not os.path.exists(directory):
		os.makedirs(directory)
	urllib.request.urlretrieve(str(c[5]), path)
	i = i+1
