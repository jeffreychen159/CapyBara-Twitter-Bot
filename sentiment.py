import nltk
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

sentence = 'Shitty fun doing'
positive = []
negative = []
lst = []
lsti = []

vs = SentimentIntensityAnalyzer().polarity_scores(sentence)
print(vs)
for i in vs: 
    lst.append(i)

for i in vs: 
    lsti.append(vs[i])

#print(lst)
#print(lsti)
#print(positive)
#print(negative)

