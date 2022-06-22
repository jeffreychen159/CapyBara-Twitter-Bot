import nltk
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

NEG = 0
POS = 1
NEU = 0.5

sentence = 'Shit happy sad love hot'

def sentiment_score(sentence): 
    vs = SentimentIntensityAnalyzer().polarity_scores(sentence)
    scorev1 = vs['neg'] * NEG + vs['neu'] * NEU + vs['pos'] * POS
    if vs['pos'] == 0 or vs['neg'] == 0: 
        scorev2 = scorev1
    else: 
        scorev2 = scorev1 * (vs['pos'] / vs['neg'])
    return scorev1, scorev2