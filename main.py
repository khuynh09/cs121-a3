import os
import json
from Indexer import Indexer



def main():
    indexer = Indexer()
    numDocs = 0

    for subdir, dirs, files in os.walk(r'C:\Users\Kevin Huynh\Projects\cs121-a3\DEV'): ## TODO: need to update to directory's DEV folder
        for filename in files:
            filepath = subdir + os.sep + filename
            f = open(filepath)
            data = json.load(f)
            print(data["url"])
            indexer.parse(data['content'], data['url'])
            numDocs += 1
    
    indexer.compute_tdidf()
    sortedTokens = sorted(indexer.invertedIndex.items(), key=lambda x: x[1]["total_frequency"], reverse=True)
    print("Number of Documents: {}".format(numDocs))
    print("Number of Unique Tokens: {}".format(len(indexer.invertedIndex.keys())))
    file1 = open("index.txt", "a")
    for k,v in sortedTokens:
        postings = v["postings"]
        sorted_postings = sorted(postings.items(), key=lambda x: x[1], reverse=True)
        
        file1.write("{}:{}\n".format(k,sorted_postings))
    file1.close()


def intersection(lst1, lst2):
    return list(set(lst1) & set(lst2))

def milestone2():


    running = True

 

        

    # words = ["cristina lopes", "machine learning", "ACM",  "master of software engineering"]
    

    while(running):
        query = input("Search... ")

        words = query.split()
        queries = dict()

        num_of_words = len(words)

    
        file1 = open("index.txt", "r")  

        found_words = 0
        for line in file1:
            
            if found_words == num_of_words:
                break

            token = line.split(":[")[0]

            if token in words:
                found_words += 1

                new_line = line.split(":[")[1].replace("]","")
                postings = new_line.split("), (")

                queries[token] = {}
                for doc in postings: 
                    mapping = doc.strip().split(",")
                    url = mapping[0].replace("(","").replace("'","")
                    score = float(mapping[1].replace(")",""))
                    
                    
                    queries[token][url] = score


        AND_postings = []


        for token in queries.keys():
            docs = queries[token].keys()

            if len(AND_postings) == 0:
                AND_postings = docs
            else:
                AND_postings = intersection(AND_postings, docs)



        total_doc_scores = dict()

        for docs in AND_postings:
            score = 0
            for token in queries.keys():
                score += queries[token][docs]

            total_doc_scores[docs] = score


        top5 = sorted(total_doc_scores.items(), key=lambda x: x[1], reverse=True)

        print(top5)

            


            


    

main()
# milestone2()
