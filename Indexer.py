from bs4 import BeautifulSoup
import re
from urllib.parse import urldefrag

#Inverted Index Template
# {
#     token: {
#         total_frequency: 0,
#         postings: [{url_id: token_freq}],
#         tf-idf: 0 (total_frequency for now)
#     
# }

class Indexer:
    invertedIndex = {}

    def __init__(self):
        pass

    def parse(self, content, url):
        defraggedUrl = urldefrag(url)[0]
        soup = BeautifulSoup(content, 'html.parser')
        tokens = re.findall(r'[A-Za-z0-9]+', soup.get_text().lower())
        for t in tokens:
            if t not in self.invertedIndex:
                self.invertedIndex[t] = {"tf-idf": 1, "postings": {defraggedUrl: 1}}
            else:
                self.invertedIndex[t]["tf-idf"] += 1
                if defraggedUrl not in self.invertedIndex[t]['postings']:
                    self.invertedIndex[t]['postings'][defraggedUrl] = 1
                else:
                    self.invertedIndex[t]['postings'][defraggedUrl] += 1
            
