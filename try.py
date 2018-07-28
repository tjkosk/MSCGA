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

def FileToTokens(filename):

	global lineCount, wordCount, table, keyLen

	currentFile = open(filename,'r')
	readFile = currentFile.read()
	sent_tokens = nltk.sent_tokenize(readFile)
	currentFile.close()

	for sentence in sent_tokens:
		lineCount = lineCount + 1;
		cleanStr = sentence
		tokens = cleanStr.split()

		keyList = [];
		
		table.setdefault( '#BEGIN#', []).append(tokens[0:keyLen]);

		for item in tokens:
			if len(keyList) < keyLen:  #not enough items
				keyList.append(item)
				continue
			table.setdefault( tuple(keyList), []).append(item)
			keyList.pop(0)
			keyList.append(item)
			wordCount = wordCount + 1


def main ():
	
	global maxWordInSentence, table
	FileToTokens('testie.txt')

	#print( "lines: " + str(lineCount) )
	#print( "total words: " + str(wordCount) )
	
	markovDictFile=open('markovdictfile.txt', 'w')
	pprint.pprint(table,markovDictFile)
	markovDictFile.close()

	markovObj = markov.Markov(dictFile = 'markovdictfile.txt')
	for i in range(50):
		text = markovObj.generateText()
		if text.endswith("."):
			print(text)


if __name__ == "__main__":
    main()