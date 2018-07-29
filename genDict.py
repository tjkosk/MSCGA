import nltk
import re
import numpy as np 
import random as rm
import pprint
import markov

table = {}
keyLen = 1
lineCount = 0
wordCount = 0
maxWordInSentence = 10
genNSentences = 5

class GenDict(object):

	def __init__(self,textFile="",outputFile=""):
		self.table = {}
		self.sent_tokens = []
		self.keyLen = 1
		self.lineCount = 0
		self.wordCount = 0
		self.outputFile = outputFile
		if textFile:
			self.loadFile(textFile)


	def loadFile(self,textFile):

		currentFile = open(textFile,'r')
		readFile = currentFile.read()
		self.sent_tokens = nltk.sent_tokenize(readFile)
		currentFile.close()

	def fileToTokens(self):	

		for sentence in self.sent_tokens:
			self.lineCount = self.lineCount + 1;
			cleanStr = sentence
			tokens = cleanStr.split()

			keyList = [];
			
			self.table.setdefault( '#BEGIN#', []).append(tokens[0:self.keyLen]);

			for item in tokens:
				if len(keyList) < self.keyLen:  #not enough items
					keyList.append(item)
					continue
				self.table.setdefault( tuple(keyList), []).append(item)
				keyList.pop(0)
				keyList.append(item)
				self.wordCount = self.wordCount + 1

	def writeDictFile(self):
		markovDictFile = open(self.outputFile, 'w')
		pprint.pprint(self.table,markovDictFile)
		markovDictFile.close()
