from os.path import dirname, realpath
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import math

from Codes.Preprocessing import Preprocessing
from nltk.corpus import stopwords
from nltk import PorterStemmer
from Codes.replacer import AntonymReplacer

matplotlib.use('TkAgg')

filepath = realpath(__file__)
dir_of_file = dirname(filepath)
parent_dir_of_file = dirname(dir_of_file)
pd.set_option('display.max_colwidth', -1)


class LoadData(object):
    count = 0
    data = []
    tweets = []

    @staticmethod
    def pie_chart(pos, neg, neu, title):

        # Drawing Pie chart
        slices_hours = [pos, neg, neu]
        activities = ['pos', 'neg', 'neu']
        colors = ['#99ff99', '#ff9999', '#66b3ff']
        explode = (0, 0.1, 0)

        plt.pie(slices_hours, explode=explode, labels=activities, colors=colors, startangle=90, autopct='%.1f%%',
                shadow=True)
        # Equal aspect ratio ensures that pie is drawn as a circle
        plt.axis('equal')
        plt.title(title)
        plt.tight_layout()

        plt.show()

    def perform_Preprocessing(self):

        # Reading needed data from given json file
        # file_tweets = open(parent_dir_of_file + "/ProcessedTweets/rawTweets.csv", 'w', encoding="utf-8")
        try:
            df_clinton = pd.read_excel(r'' + parent_dir_of_file + '/TweetsFiles/final clinton.xlsx')
            df_trump = pd.read_excel(r'' + parent_dir_of_file + '/TweetsFiles/final trump.xlsx')
            # df_clinton.loc[:, 'candidate': 'label'].to_csv('rawTweets.csv', 'a')
            # df_trump.loc[:, 'Candidate': 'label'].to_csv('rawTweets.csv', 'a')

            df_clinton["tweet"].replace('\n', '', regex=True)
            df_trump["tweet"].replace('\n', '', regex=True)

            df_clinton.to_csv(parent_dir_of_file + '/ProcessedTweets/rawTweets-clinton.csv')
            df_trump.to_csv(parent_dir_of_file + '/ProcessedTweets/rawTweets-trump.csv')
            # df_tweets = df_clinton.append(df_trump.loc[:, 'candidate': 'label'], sort=False)
            # df_tweets = df_tweets.replace('\n', '', regex=True)
            # df_tweets.to_csv(parent_dir_of_file + '/ProcessedTweets/rawTweets-clinton.csv')

            df_rawTweets_trump = pd.read_csv(r'' + parent_dir_of_file + '/ProcessedTweets/rawTweets-clinton.csv')
            df_rawTweets_trump['tweet'].replace('\n', '', regex=True)

            # PreProcessing.py
            obj = Preprocessing()

            cleaned_tweets = open(parent_dir_of_file + '/ProcessedTweets/preprocessed-rawTweets-clinton.txt', 'w', encoding="utf-8")
            for line in df_rawTweets_trump['tweet']:
                clnd_tweets = obj.preprocess_tweet(line)
                # print(line)
                # print(clnd_tweets, "\n")
                cleaned_tweets.write(clnd_tweets)
                cleaned_tweets.write('\n')
            cleaned_tweets.close()

            replacer = AntonymReplacer()
            count = 0
            tweets = []

            # replacer.py
            cleaned_tweets = open(parent_dir_of_file + '/ProcessedTweets/final_ready-clinton-tweets.txt', 'w',
                                   encoding="utf-8")
            with open(parent_dir_of_file + '/ProcessedTweets/preprocessed-rawTweets-clinton.txt', 'r') as f:
                for tokenized_words in f:
                    count = count + 1
                    stop_words = stopwords.words('english')
                    # spell = SpellChecker()
                    var = [word for word in tokenized_words.split() if word not in stop_words]

                    neg_removed = replacer.repalce_negations(var)
                    tweets.append(neg_removed)

                    cleaned_tweets.write(str(tweets))
                    # cleaned_tweets.write('\n')

                print(tweets)
                wordSet = []

                for line in tweets:
                    wordSet = set(wordSet).union(set(line))

                print(wordSet)
                wordDictA = dict.fromkeys(wordSet, 0)
                # print(wordSet)

                for word in wordSet:
                    wordDictA[word] += 1
                print(wordDictA)

                # Calling computeTF
                print(self.computeTF(wordDictA, wordSet))

                # Calling computeTFIDF
                idfs = self.computeIDF(wordDictA)
                print(idfs)
                tfidfTweets = self.computeTFIDF(wordDictA, idfs)
                print(pd.DataFrame([tfidfTweets]))



        except KeyError as e:
            print(e)
        except IOError as e:
            print(e)
        except IndexError as e:
            print(e)
        except Exception as e:
            print(e)


    def computeTF(self, wordDict, bow):
        tfDict = {}
        bowCount = len(bow)
        for word, count in wordDict.items():
            tfDict[word] = count/float(bowCount)
        return tfDict

    def computeIDF(self, docList):
        idfDict = {}
        N = len(docList)

        idfDict = dict.fromkeys(docList, 0)

        for word, val in docList.items():
            if val > 0:
                idfDict[word] += 1

        for word, val in idfDict.items():
            idfDict[word] = math.log10(N / float(val))

        return idfDict

    def computeTFIDF(self, tfBow, idfs):
        tfidf = {}
        for word, val in tfBow.items():
            tfidf[word] = val * idfs[word]
        return tfidf

    def display(self):
        positive = 0
        negative = 0
        neutral = 0
        try:
            df_clinton = pd.read_csv(r'' + parent_dir_of_file + '/ProcessedTweets/rawTweets-clinton.csv')
            print(df_clinton['label'])
            for label in df_clinton['label']:
                if label == 'negative':
                    negative = negative + 1
                elif label == 'neutral':
                    neutral = neutral + 1
                else:
                    positive = positive + 1
            self.pie_chart(positive, negative, neutral, 'Hilllary Clinton')

        except KeyError as e:
            print(e)
        except IOError as e:
            print(e)
        except IndexError as e:
            print(e)
        except Exception as e:
            print(e)


obj = LoadData()
obj.perform_Preprocessing()
