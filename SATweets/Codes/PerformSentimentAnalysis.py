import matplotlib
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
# from spellchecker import SpellChecker
import matplotlib.pyplot as plt
from textblob import TextBlob
matplotlib.use('TkAgg')


class PerformSentimentAnalysis(object):

    @staticmethod
    def pie_chart(pos, neg, neu, title):

        # Drawing Pie chart
        slices_hours = [pos, neg, neu]
        activities = ['pos', 'neg', 'neu']
        colors = ['#99ff99', '#ff9999', '#66b3ff']
        explode = (0, 0.1, 0)

        plt.pie(slices_hours, explode=explode, labels=activities, colors=colors, startangle=90, autopct='%.1f%%', shadow=True)
        # Equal aspect ratio ensures that pie is drawn as a circle
        plt.axis('equal')
        plt.title(title)
        plt.tight_layout()

        plt.show()

    def vader(self, tweets):

        # Utility function to classify the polarity of a tweet using VaderSentiment.
        neg = 0.0
        pos = 0.0
        neu = 0.0
        total = 0
        analyzer = SentimentIntensityAnalyzer()
        for sentence in tweets:
            vs = analyzer.polarity_scores(sentence)
            # print("{:-<50} {}".format(sentence, str(vs)))
            print("(VaderSentiment) ", sentence, "       -----------     ", vs)
            total = total + 1
            pos = pos + float(vs.get('pos'))
            neg = neg + float(vs.get('neg'))
            neu = neu + float(vs.get('neu'))
            analysis = TextBlob(sentence)
            if analysis.sentiment.polarity > 0:
                print("(TextBlob) Positive tweet -> ", analysis)
                # return 1
            elif analysis.sentiment.polarity == 0:
                print("(TextBlob) Neutral tweet -> ", analysis)
                # return 0
            else:
                text = analysis
                print("(TextBlob) Negative tweet -> ", text)
                # return -1

        if pos is not None and neg is not None and neu is not None:
            pos = (pos/total)*100
            neg = (neg/total)*100
            neu = (neu/total)*100
            # calling pie chart drawing method
            self.pie_chart(pos, neg, neu, 'VaderSentiment')
        else:
            print('Empty values were given.')

    def textblob(self, tweet):

        # Utility function to classify the polarity of a tweet using TextBlob.
        neg = 0
        pos = 0
        neu = 0
        total = 0

        for sentence in tweet:
            analysis = TextBlob(sentence)
            total = total + 1
            # Checked-spellings
            # spell = SpellChecker()
            # Get the one `most likely` answer
            # print("SpellChecker->   ", spell.correction(str(analysis)))
            # print("SpellChecker->   ", analysis.correct())
            if analysis.sentiment.polarity > 0:
                # print("Positive tweet -> ", analysis)
                pos = pos + 1
                # return 1
            elif analysis.sentiment.polarity == 0:
                # print("Neutral tweet -> ", analysis)
                neu = neu + 1
                # return 0
            else:
                # text = analysis
                neg = neg + 1
                # print("Negative tweet -> ", text)
                # return -1

        if pos is not None and neg is not None and neu is not None:
            pos = (pos/total)*100
            neg = (neg/total)*100
            neu = (neu/total)*100
            # calling pie chart drawing method
            self.pie_chart(pos, neg, neu, 'TextBlob')
        else:
            print('Empty values were given.')
