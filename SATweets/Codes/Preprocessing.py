import re
from nltk import PorterStemmer
from nltk.stem import SnowballStemmer
from nltk.tokenize import word_tokenize
# from nltk.corpus import stopwords

#nltk.download()


class Preprocessing(object):

    def preprocess_word(self, word):

        # Remove punctuation
        word = word.strip('\'"?!,.():;')
        # Convert more than 2 letter repetitions to 2 letter
        # funnnnny --> funny
        word = re.sub(r"(.)\1+", r'\1\1', word)
        # Remove - & '
        word = re.sub(r"(-|')", '', word)
        # Checked-spellings
        # spell = SpellChecker()
        # Get the one `most likely` answer
        # spell.correction(word)
        # Removes Stopwords
        # var = ''
        # stop_words = stopwords.words('english')
        # if word not in stop_words:
        #    var = word
        return word

    def is_valid_word(self, word):
        # Check if word begins with an alphabet
        return re.search(r'^[a-zA-Z][a-z0-9A-Z\._]*$', word) is not None

    def handle_emojis(self, tweet):

        # Smile -- :), : ), :-), (:, ( :, (-:, :')
        tweet = re.sub(r"(:\s?\)|:-\)|\(\s?:|\(-:|:'\))", ' EMO_POS ', tweet)
        # Laugh -- :D, : D, :-D, xD, x-D, XD, X-D
        tweet = re.sub(r"(:\s?D|:-D|x-?D|X-?D)", ' EMO_POS ', tweet)
        # Love -- <3, :*
        tweet = re.sub(r'(<3|:\*)', ' EMO_POS ', tweet)
        # Wink -- ;-), ;), ;-D, ;D, (;,  (-;
        tweet = re.sub(r'(;-?\)|;-?D|\(-?;)', ' EMO_POS ', tweet)
        # Sad -- :-(, : (, :(, ):, )-:
        tweet = re.sub(r'(:\s?\(|:-\(|\)\s?:|\)-:)', ' EMO_NEG ', tweet)
        # Cry -- :,(, :'(, :"(
        tweet = re.sub(r'(:,\(|:\'\(|:"\()', ' EMO_NEG ', tweet)
        return tweet

    def preprocess_tweet(self, tweet):
        processed_tweet = []
        # Convert to lower case
        tweet = tweet.lower()
        # Replaces URLs with the word URL
        tweet = re.sub(r'((www\.[\S]+)|(https?://[\S]+))', ' ', tweet)
        # Replace @handle with the word USER_MENTION
        tweet = re.sub(r'@[\S]+', ' ', tweet)
        # Replaces #hashtag with hashtag
        tweet = re.sub(r'#(\S+)', r' \1 ', tweet)
        # Remove RT (retweet)
        tweet = re.sub(r'\brt\b', '', tweet)
        # Replace 2+ dots with space
        tweet = re.sub(r'\.{2,}', ' ', tweet)
        # Strip space, " and ' from tweet
        tweet = tweet.strip(' "\'')
        # Replace emojis with either EMO_POS or EMO_NEG
        tweet = self.handle_emojis(tweet)
        # Replace multiple spaces with a single space
        tweet = re.sub(r'\s+', ' ', tweet)
        tweet = re.sub(r'text', ' ', tweet)
        words = tweet.split()

        for word in words:
            word = self.preprocess_word(word)
            use_stemmer = False
            porter = PorterStemmer()
            # print("BEFORE -> ", input_str)
            if self.is_valid_word(word):
                if use_stemmer:
                    word = porter.stem(word)
                    # print("AFTER -> ", word)
                processed_tweet.append(word)

        return ' '.join(processed_tweet)


# obj = Preprocessing()
# cleaned_tweets = open('C:/Users/Dell/PycharmProjects/SATweets/ProcessedTweets/temp.txt', 'w')
# with open('C:/Users/Dell/PycharmProjects/SATweets/ProcessedTweets/rawTweets.txt', 'r', encoding="utf-8") as f:
#     for line in f:
#         clnd_tweets = obj.preprocess_tweet(line)
#         print(clnd_tweets)
#         cleaned_tweets.write(clnd_tweets)
#         cleaned_tweets.write('\n')
#
# cleaned_tweets.close()
# f.close()
#
# contents = open('C:/Users/Dell/PycharmProjects/SATweets/ProcessedTweets/temp.txt', 'r').readlines()
# content_set = set(contents)
# cleanData = open('C:/Users/Dell/PycharmProjects/SATweets/ProcessedTweets/preprocessedTweets.txt', 'w')
#
# for line in content_set:
#     cleanData.write(line)
# cleanData.close()

