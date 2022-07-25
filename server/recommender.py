from rank_bm25 import BM25Okapi

from persistance import get_docs, get_tags, get_doc, get_docs_sorted

import os
import pickle
from datetime import datetime

class Recommender():

    def __init__(self):
        docs = get_docs_sorted()
        self.corpus, self.ids, self.labels = self._preprocess_docs(docs)
        # preprocessed_corpus = preprocess_docs(corpus)

        self.model = BM25Okapi(self.corpus)
        self.real_labels = get_tags()

    def _preprocess_doc(self, doc: str):
        doc.split(" ")
        return doc

    def _preprocess_docs(self, docs):
        texts = []
        ids = []
        labels = []
        for doc in docs:
            print(doc)
            text = self._preprocess_doc(doc['text'])

            ids.append(doc['id'])
            texts.append(text)
            labels.append(doc['tags'])

        return texts, ids, labels

    def _remove_duplicates(self,recommendation):
        set_of_used_ids = set()

        no_duplicate_list = []
        for r in recommendation:
            if r['id'] not in set_of_used_ids:
                no_duplicate_list.append(r)

                set_of_used_ids.add(r['id'])

        return no_duplicate_list

    def recommend_tags(self, text: str, k: int = 5):
        # function to recommend tags, based on 5 most relevant documents, sorted by relevance

        query = text
        preprocessed_query = self._preprocess_doc(query)

        doc_scores = self.model.get_scores(preprocessed_query)
        top_docs = sorted(range(len(doc_scores)), key=lambda i: doc_scores[i])[-k:]

        print("DEUBG RECOMMEND")
        for i in top_docs:
            print(i)
            print(get_doc(self.ids[i]))

        print("DEUBG END")
        recommendation = []
        for i in top_docs:
            tags = get_doc(self.ids[i])['tags']
            recommendation.extend(tags)

        recommendation = self._remove_duplicates(recommendation)
        print(recommendation)
        # recommendation = set(recommendation)
        # return set([get_doc(self.ids[i])['tags'] for i in top_docs])
        return recommendation

model = None

def get_recommendations(text: str):
    tags = model.recommend_tags(text)
    return tags

def init_recommender():
    global model
    model = Recommender()

    filename = datetime.now().date().strftime('%Y-%m-%d')
    filename = "recommender_model" + filename + ".pkl"
    print(filename)

    with open(filename, 'wb') as outp:
        pickle.dump(model, outp)

