from nltk.corpus import stopwords
from Codes.PerformSentimentAnalysis import PerformSentimentAnalysis
from Codes.replacer import AntonymReplacer
from spellchecker import SpellChecker
from Codes.readCSV import ReadCSV
from Codes.Preprocessing import Preprocessing


# readCSV.py
obj = ReadCSV()
obj.read()

# Preprocessing.py
obj = Preprocessing()
cleaned_tweets = open('C:/Users/Dell/PycharmProjects/SATweets/ProcessedTweets/temp.txt', 'w')
with open('C:/Users/Dell/PycharmProjects/SATweets/ProcessedTweets/rawTweets.txt', 'r', encoding="utf-8") as f:
    for line in f:
        clnd_tweets = obj.preprocess_tweet(line)
        # print(clnd_tweets)
        cleaned_tweets.write(clnd_tweets)
        cleaned_tweets.write('\n')

cleaned_tweets.close()
f.close()

contents = open('C:/Users/Dell/PycharmProjects/SATweets/ProcessedTweets/temp.txt', 'r').readlines()
content_set = set(contents)
cleanData = open('C:/Users/Dell/PycharmProjects/SATweets/ProcessedTweets/preprocessedTweets.txt', 'w')

for line in content_set:
    cleanData.write(line)
cleanData.close()


replacer = AntonymReplacer()
SA = PerformSentimentAnalysis()
count = 0
tweets = []

cleaned_tweets = open('C:/Users/Dell/PycharmProjects/SATweets/ProcessedTweets/final_ready-tweets-csv.txt', 'w', encoding="utf-8")
with open('C:/Users/Dell/PycharmProjects/SATweets/ProcessedTweets/preprocessedTweets.txt', 'r') as f:
    for tokenized_words in f:
        count = count + 1
        stop_words = stopwords.words('english')
        # print(tokenized_words)
        # spell = SpellChecker()
        var = [word for word in tokenized_words.split() if word not in stop_words]
        # for word in var:
            # Get the one `most likely` answer
            # print(count, "      ", spell.correction(word))
            # spell.correction(word)
            # Get a list of `likely` options
            # print(spell.candidates(word))

        neg_removed = replacer.repalce_negations(var)
        # print(str(neg_removed))
        tweets.append(neg_removed)

for i in tweets:
    line = ' '.join(i)
    cleaned_tweets.write(line)
    cleaned_tweets.write('\n')
    # print(line)
cleaned_tweets.close()
# for line in cleaned_tweets:
#     print(line.split())
#     line = ' '.join(neg_removed)
#     cleaned_tweets.write(line)
#     cleaned_tweets.write('\n')
#     cleaned_tweets.close()

with open('C:/Users/Dell/PycharmProjects/SATweets/ProcessedTweets/final_ready-tweets-csv.txt', 'r') as f:
    SA.claculate_results(f)


