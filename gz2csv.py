import fileinput
import sys
import os
import time
from tqdm import tqdm

""""

python3 gz2csv.py <nome file di origine, io ho il "data"> <parole da cercare separate da spazio>

"""

path = os.path.dirname(os.path.abspath(__file__)) #
noself = False
keys = []

q1 = len(sys.argv)

for k in range(q1):
	if k > 1:
		if sys.argv[k] != "noself":
			keys.append(sys.argv[k])

if q1 <= 2:
	if q1 <= 1:
		print(" \t- Inserire il nome del file")
	print(" \t- Inserire uno o piu' Filtri come argomento \n")
else:
	autori = []
	itemSet = []
	f = open(path + "/dblp_coo.csv", "w") #azzero il file
	f.close()
	f = open(path + "/dblp_coo.csv", "a") #apro il file in scrittura


	for x in range(0, len(sys.argv)):
		print(sys.argv[x])

	pippo = sum(1 for line in open(path + "/" + sys.argv[1]))

	print("righe totali = " + str(pippo) + "\n")





	pbar = tqdm(total=pippo)
	for line in fileinput.input(path + "/" + sys.argv[1]):
		#print(" \n *** INIZIO A FARE #COSE *** \n")
		pbar.update(1)
		line = line.replace(";","")
		if "<author>" in line: #controllo i tag autori
			line = line.replace("<author>","")
			line = line.replace("</author>","")
			line = line.replace("\n","")
			if not line in autori:
				autori.append( line ) #aggiungo gli autori alla lista

		if "<title>" in line: #controllo il tag titolo
			line = line.lower()
			for argument in keys:
				argument = argument.lower()
				argument = argument.replace("+"," ")

				itemSet.append( "Source;Target" )

				if argument in line:
					checked = len(autori)
					for i in range(0, checked):
						for k in range(i+1, checked):
							val = autori[i].replace(" ","_")
							val2 = autori[k].replace(" ","_")
							structPrint = val +"; "+ val2
							if not structPrint in itemSet: #solo se la correlazione non esiste nel set, la aggiungo
								itemSet.append( structPrint )
				autori = []

	pbar.close()


	for elem in itemSet:
		f.write(elem + "\n")
	print ("\n Trovate %d correlazioni fra autori. \n" % len(itemSet))
	f.close()
