import nltk.sentiment
nltk.download('vader_lexicon')
analyzer = nltk.sentiment.SentimentIntensityAnalyzer()

def get_sentiment(user_text):
    scores = analyzer.polarity_scores(user_text)
    sentiment_score = scores['compound']
    return sentiment_score

def get_reaction(score):
    return_text = ""
    if score > 0.45:
        return_text = "Very positive text (Sentiment score of " + str(score) + ")"
    elif score > 0:
        return_text = "Fairly positive text (Sentiment score of " + str(score) + ")"
    elif score == 0:
        return_text = "Neutral text (Sentiment score of " + str(score) + ")"
    elif score < -0.45:
        return_text = "Very negative text (Sentiment score of " + str(score) + ")"
    elif score < 0:
        return_text = "Fairly negative text (Sentiment score of " + str(score) + ")"
    return return_text

def main():
    print("Welcome to the Sentiment Analyzer!")
    while True:
        text = input("Enter text to be analyzed: ")
        text_score = get_sentiment(text)
        print(get_reaction(text_score)+"\n")
        text2 = input("Would you like to go again? (y/n): ")
        if text2 == "n":
            print("Exiting the program")
            break
        
if __name__ == "__main__":
    main()
