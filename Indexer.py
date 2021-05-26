from bs4 import BeautifulSoup
import re
from urllib.parse import urldefrag
import math

#Inverted Index Template
# {
#     token: {
#         total_frequency: 0,
#         postings: {url_id: TD-IDF},
#         tf-idf: 0 (total_frequency for now)
#     
# }

class Indexer:
    invertedIndex = {}
    total_documents = 0 
    stop_words = ["", "a", "about", "above", "after", "again", "against", "all", "am", "an", "and", "any", "are", "aren't",
                "as", "at", "be", "because", "been",
                "before", "being", "below", "between", "both", "but", "by", "can't", "cannot", "could", "couldn't",
                "did", "didn't", "do", "does", "doesn't", "doing", "don't", "down", "during", "each", "few", "for",
                "from", "further", "had", "hadn't", "has", "hasn't",
                "have", "haven't", "having", "he", "he'd", "he'll", "he's", "her", "here", "here's", "hers",
                "herself", "him", "himself", "his", "how", "how's", "i", "i'd", "i'll",
                "i'm", "i've", "if", "in", "into", "is", "isn't", "it", "it's", "its", "itself", "let's",
                "me", "more", "most", "mustn't", "my",
                "myself", "no", "nor", "not", "of", "off", "on", "once", "only", "or", "other", "ought", "our",
                "ours", "ourselves", "out",
                "over", "own", "same", "shan't", "she", "she'd", "she'll", "she's", "should", "shouldn't",
                "so", "some", "such", "than", "that", "that's", "the", "their",
                "theirs", "them", "themselves", "then", "there",
                "there's", "these", "they", "they'd", "they'll", "they're", "they've", "this", "those", "through", "to",
                "too",
                "under", "until", "up", "very", "was", "wasn't", "we", "we'd", "we'll", "we're", "we've", "were",
                "weren't", "what", "what's", "when", "when's", "where", "where's", "which",
                "while", "who", "who's", "whom", "why", "why's", "with", "won't", "would", "wouldn't", "you",
                "you'd", "you'll", "you're", "you've", "your", "yours", "yourself", "yourselves"]

    content = {}

    def __init__(self):
        pass

    def parse(self, content, url):
        defraggedUrl = urldefrag(url)[0]
        soup = BeautifulSoup(content, 'html.parser')
        # if soup.get_text() not in content.values():
        #     return
        tokens = re.findall(r'[A-Za-z0-9]+', soup.get_text().lower())
        for t in tokens:

            if t not in self.stop_words: 
                if t not in self.invertedIndex:
                    self.invertedIndex[t] = {"total_frequency": 1, "postings": {defraggedUrl: 1}}
                    
                else:
                    self.invertedIndex[t]["total_frequency"] += 1 
                    if defraggedUrl not in self.invertedIndex[t]['postings']:
                        self.invertedIndex[t]['postings'][defraggedUrl] = 1
                    else:
                        self.invertedIndex[t]['postings'][defraggedUrl] += 1
                # content[defraggedUrl] = soup.get_text()
        self.total_documents += 1

    def compute_tdidf(self):
        for token, value in self.invertedIndex.items():
            for p,freq in self.invertedIndex[token]["postings"].items():
                total_freq = freq

                self.invertedIndex[token]["postings"][p] = (1+math.log(total_freq))* math.log(self.total_documents/len(self.invertedIndex[token]["postings"])) 

            self.invertedIndex[token]["postings"]
            
