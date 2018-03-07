from ._tools import MoodInterface

class TwitterMoodGatherer:

    def __init__(self, twitter_interface):
        self.__twitter_interface = twitter_interface

    def get_mood(self, query):
        return MoodInterface()
