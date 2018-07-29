import markov
import genDict


def main ():
	
	dictObj = genDict.GenDict(textFile = 'testie.txt',outputFile = 'markovdictfile.txt')
	dictObj.fileToTokens()
	dictObj.writeDictFile()

	#print( "lines: " + str(lineCount) )
	#print( "total words: " + str(wordCount) )
	

	markovObj = markov.Markov(dictFile = 'markovdictfile.txt')
	for i in range(10):
		text = markovObj.generateText()
		if text.endswith("."):
			print(text)


if __name__ == "__main__":
    main()