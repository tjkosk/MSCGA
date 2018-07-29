import random as rm
import numpy as np
import nltk


class Markov(object):
	def __init__(self,dictFile=""):
		self.markovDict = {}
		self.sentLength = 20
		if dictFile:
			self.loadDictionary(dictFile)

	def loadDictionary(self,dictFile):
		filey = open(dictFile,'r')
		self.markovDict = eval(filey.read())
		#print(self.markovDict)


	def generateText(self):
		key = list(rm.choice(self.markovDict['#BEGIN#']))
		genStr = " ".join(key)
		for _ in range(self.sentLength):
			newKey = self.markovDict.setdefault( tuple(key), "") 
			if(newKey == ""):
				break
			newVal = rm.choice(newKey)
			genStr = genStr + " " + newVal

			key.pop(0)
			key.append(newVal)

		return genStr


