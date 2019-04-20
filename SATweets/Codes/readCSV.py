import csv
from os.path import dirname, realpath


filepath = realpath(__file__)
dir_of_file = dirname(filepath)
parent_dir_of_file = dirname(dir_of_file)


class ReadCSV(object):
    count = 0
    data = []
    tweets = []
    location = []
    created_at = []

    def read(self):

        # Reading needed data from given json file
        file = open(parent_dir_of_file + "/ProcessedTweets/rawTweets-Location-Date.txt", 'w', encoding="utf-8")
        file_tweets = open(parent_dir_of_file + "/ProcessedTweets/rawTweets.txt", 'w', encoding="utf-8")
        try:
            with open(parent_dir_of_file + '/TweetsFiles/tweets.csv', 'r', encoding="utf8") as f:
                data = csv.reader(f)
                for row in data:
                    if 'California' in row[17]:
                        # print(row[17], "            ", row[2])
                        self.tweets.append(row[2])
                        self.location.append(row[17])
                        self.created_at.append(row[5])
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
                file_tweets.write(str(self.tweets[i]))

                file.write('\n')
                file_tweets.write('\n')
        file.close()


