import os
import json
from Indexer import Indexer



def main():
    indexer = Indexer()
    numDocs = 0

    for subdir, dirs, files in os.walk(r'C:\Users\Justin Ho\Documents\CS 121\developer\DEV'): ## TODO: need to update to directory's DEV folder
        for filename in files:
            filepath = subdir + os.sep + filename
            f = open(filepath)
            data = json.load(f)
            print(data["url"])
            indexer.parse(data['content'], data['url'])
            numDocs += 1
    
    sortedTokens = sorted(indexer.invertedIndex.items(), key=lambda x: x[1]["tf-idf"], reverse=True)
    print("Number of Documents: {}".format(numDocs))
    print("Number of Unique Tokens: {}".format(len(indexer.invertedIndex.keys())))
    file1 = open("index.txt", "a")
    for k,v in sortedTokens:
        file1.write("{}:{}\n".format(k,v))
    file1.close()


main()
