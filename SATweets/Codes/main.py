from nltk.corpus import stopwords
from Codes.PerformSentimentAnalysis import PerformSentimentAnalysis
from Codes.replacer import AntonymReplacer
# from spellchecker import SpellChecker
from Codes.readCSV import ReadCSV
from Codes.Preprocessing import Preprocessing
from os.path import dirname, realpath

filepath = realpath(__file__)
dir_of_file = dirname(filepath)
parent_dir_of_file = dirname(dir_of_file)

# readCSV.py
obj = ReadCSV()
obj.read()

# Preprocessing.py
obj = Preprocessing()
cleaned_tweets = open(parent_dir_of_file + '\ProcessedTweets/temp.txt', 'w')
# with open('C:/Users/Dell/PycharmProjects/SATweets/ProcessedTweets/rawTweets.txt', 'r', encoding="utf-8") as f:
with open(parent_dir_of_file + '\ProcessedTweets/rawTweets.txt', 'r', encoding="utf-8") as f:
    for line in f:
        clnd_tweets = obj.preprocess_tweet(line)
        # print(clnd_tweets)
        cleaned_tweets.write(clnd_tweets)
        cleaned_tweets.write('\n')

cleaned_tweets.close()
f.close()

contents = open(parent_dir_of_file + '\ProcessedTweets/temp.txt', 'r').readlines()
content_set = set(contents)
cleanData = open(parent_dir_of_file + '\ProcessedTweets/preprocessedTweets.txt', 'w')

for line in content_set:
    cleanData.write(line)

cleanData.close()

replacer = AntonymReplacer()
SA = PerformSentimentAnalysis()
count = 0
tweets = []

# replacer.py
cleaned_tweets = open(parent_dir_of_file + '\ProcessedTweets/final_ready-tweets-csv.txt', 'w', encoding="utf-8")
with open(parent_dir_of_file + '\ProcessedTweets/preprocessedTweets.txt', 'r') as f:
    for tokenized_words in f:
        count = count + 1
        stop_words = stopwords.words('english')
        # print(tokenized_words)
        # spell = SpellChecker()
        var = [word for word in tokenized_words.split() if word not in stop_words]
        # for word in var:
        # Get the one `most likely` answer
        # print(count, "      ", spell.correction(word))
        # print(var)
        # var_new = spell.correction(str(var))
        # print(var_new)
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

# PerformSentimentAnalysis.py
with open(parent_dir_of_file + '\ProcessedTweets/final_ready-tweets-csv.txt', 'r') as f:
    SA.vader(f)

with open(parent_dir_of_file + '\ProcessedTweets/final_ready-tweets-csv.txt', 'r') as f:
    SA.textblob(f)
