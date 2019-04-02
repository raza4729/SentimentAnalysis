import matplotlib
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')


class PerformSentimentAnalysis(object):

    def claculate_results (self, tweets):

        neg = 0.0
        pos = 0.0
        neu = 0
        total = 0
        analyzer = SentimentIntensityAnalyzer()
        for sentence in tweets:
            vs = analyzer.polarity_scores(sentence)
            # print("{:-<50} {}".format(sentence, str(vs)))
            print(sentence, "       -----------     ", vs)
            total = total + 1
            pos = pos + float(vs.get('pos'))
            neg = neg + float(vs.get('neg'))

            # neu = neu + int(vs.get('neu'))

        # print(total)
        pos = (pos/total)*100
        neg = (neg/total)*100
        # print(pos, "         ", neg)
        # neu = (neu*100)/100
        slices_hours = [pos, neg]
        activities = ['pos', 'neg']
        colors = ['g', 'r']

        plt.pie(slices_hours, labels=activities, colors=colors, startangle=90, autopct='%.1f%%')
        plt.show()
