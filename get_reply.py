import sentiment

REPLY_POS_1 = 'Thanks for loving capybaras!'
REPLY_POS_2 = 'Thanks for liking capybaras!'
REPLY_NEG_1 = 'According to the bot, this is a negative comment.'
REPLY_NEG_2 = 'L + Ratio'

# Gets a sentiment score and gives a reply based on it. 
def auto_reply_message(message) -> str:
    score = sentiment.sentiment_score(message)
    if score[0] >= 0.75: 
        return REPLY_POS_1
    elif score[0] >= 0.5:
        return REPLY_POS_2
    elif score[0] >= 0.25:
        return REPLY_NEG_1
    else: 
        return REPLY_NEG_2