#!/usr/bin/env python
# coding: utf-8

# In[47]:


#Morgan Smith
#This is a program to classify Github Repositories and label them with possible points of contributions.
#NLP will be used on README files as well as the most recent issues published.LDA is used to
#find the needed contributions.
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize, PunktSentenceTokenizer
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from gensim.test.utils import common_texts
from gensim.corpora.dictionary import Dictionary

#filter with stopwords
stopwords = (nltk.corpus.stopwords.words('english'))
newStops = ['.', '#', ',', 'txt']
stopwords.extend(newStops)

#opening file to be tokenized
f = open('C:/Users/jmorg/390/390SNA/README.txt')
raw = f.read()

#creating tokenized word list
tokens = word_tokenize(raw)
lemma = WordNetLemmatizer()
wordList = []
lower = (w.lower() for w in tokens)

for i in lower:
    if i not in stopwords:
        i = wordList.append(lemma.lemmatize(i))
        
numTopics = 5
test = []

for element in wordList:
    temp = element.split(', ')
    test.append(temp)


common_dic = Dictionary(test)
common_corpus = [common_dic.doc2bow(text) for text in test]
lda = models.ldamodel.LdaModel(common_corpus, num_topics=5)

topics = lda.print_topics(num_topics =5, num_words=10)
for topic in topics:
    print(topic)
    
#print common_texts
print (test)
#print (wordList)
#print
#print
#print (raw)

f.close()



# In[ ]:




