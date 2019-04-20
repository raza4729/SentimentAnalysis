from nltk.corpus import stopwords
from nltk import PorterStemmer
from nltk.tokenize import word_tokenize
import csv

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

# PreProcessing.py
obj = Preprocessing()

cleaned_tweets = open(parent_dir_of_file + '\ProcessedTweets/temp.txt', 'w', encoding="utf-8")
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
        # spell = SpellChecker()
        var = [word for word in tokenized_words.split() if word not in stop_words]
        # print(var)
        # for word in var:
        # Get the one `most likely` answer
        # print(count, "      ", spell.correction(word))
        # print(var)
        # var_new = spell.correction(str(var))
        # print(var_new)
        # Get a list of `likely` options
        # print(spell.candidates(word))

        neg_removed = replacer.repalce_negations(var)
        tweets.append(neg_removed)

Line = ''
democrat = 0
republican = 0
repub_tweets = open(parent_dir_of_file + '\ProcessedTweets/republicans-tweets.txt', 'w', encoding="utf-8")
democrat_tweets = open(parent_dir_of_file + '\ProcessedTweets/democrat-tweets.txt', 'w', encoding="utf-8")
for i in tweets:
    line = ' '.join(i)
    if 'republican' in line or 'trump' in line or 'donald' in line:
        republican = republican + 1
        # print(republican, "  REPUBLICAN       ", line)
        repub_tweets.write(line)
        repub_tweets.write('\n')
    elif 'democrat' in line or 'clinton' in line or 'hillary' in line:
        democrat = democrat + 1
        # print(democrat, "  DEMOCRAT       ", line)
        democrat_tweets.write(line)
        democrat_tweets.write('\n')
    cleaned_tweets.write(line)
    cleaned_tweets.write('\n')
    # print(line)
cleaned_tweets.close()

# Stemming and Sorting
vocabulary = open(parent_dir_of_file + '\ProcessedTweets/vocab.txt', 'w', encoding="utf-8")
file = sorted(open(parent_dir_of_file + '\ProcessedTweets/final_ready-tweets-csv.txt').read().split())
# print(file)
stemmer = PorterStemmer()
for word in file:
    vocab =stemmer.stem(word)
    vocabulary.write(vocab)
    vocabulary.write('\n')
vocabulary.close()

contents = open(parent_dir_of_file + '\ProcessedTweets/vocab.txt', 'r').readlines()
content_set = set(contents)
cleanData = open(parent_dir_of_file + '\ProcessedTweets/preprocessed-Vocab.txt', 'w')

for line in content_set:
    cleanData.write(line)

# PerformSentimentAnalysis.py
with open(parent_dir_of_file + '\ProcessedTweets/final_ready-tweets-csv.txt', 'r') as f:
    SA.vader(f)

with open(parent_dir_of_file + '\ProcessedTweets/final_ready-tweets-csv.txt', 'r') as f:
    SA.textblob(f)
