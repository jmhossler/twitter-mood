from .mood_interface import MoodInterface


class TwitterMoodGatherer:

    def __init__(self, twitter_interface, sentiment_interface):
        self.__twitter_interface = twitter_interface
        self.__sentiment_interface = sentiment_interface

    def get_mood(self, query):
        tweets = self.__twitter_interface.query(query)
        if len(tweets) == 0:
            return MoodInterface()
        return sum([self.__sentiment_interface.analyze(tweet)
                    for tweet in tweets]) / len(tweets)
