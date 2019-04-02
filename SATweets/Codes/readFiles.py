import json


class ReadFiles(object):
    count = 0
    data = []
    tweets = []
    location = []
    created_at = []

    def readjson(self):

        # Reading needed data from given json file
        file = open("C:/Users/Dell/PycharmProjects/SATweets/ProcessedTweets/rawTweets-Location-Date.txt", 'w', encoding="utf-8")
        file_tweets = open("C:/Users/Dell/PycharmProjects/SATweets/ProcessedTweets/rawTweets.txt", 'w', encoding="utf-8")
        try:
            for line in open('C:/Users/Dell/PycharmProjects/SATweets/TweetsFiles/usa_election16.json'):
                data = json.loads(line)
                # print(data['user']['location'], "               ", data['text'])
                if data.get('user') is not None:
                    if data['user']['location'] is not None and data.get('text') is not None and data.get('created_at') is not None:
                        if 'California' in str(data['user']['location']):
                            self.tweets.append(data.get('text'))
                            self.location.append(data['user']['location'])
                            self.created_at.append(data.get('created_at'))
                            self.count = self.count + 1

        except KeyError as e:
            print(e)
        except IOError as e:
            print(e)
        except IndexError as e:
            print(e)
        except Exception as e:
            print(e)
        finally:
            for i in range(self.count):
                # print(self.created_at[i], "          ", self.location[i], "         ", self.tweets[i])
                # print(i, "          ", self.tweets[i].encode("utf-8"))
                var = self.created_at[i], "           ", self.location[i], "           ", self.tweets[i]
                file.write(str(var))
                file_tweets.write(self.tweets[i])

                file_tweets.write('\n')
                file.write('\n')

        file.close()


#obj = ReadFiles()
#obj.readjson()
