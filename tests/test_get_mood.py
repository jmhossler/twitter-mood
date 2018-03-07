from unittest.mock import MagicMock
from twitter_mood.mood_gatherer import TwitterMoodGatherer

class TestGetMoodSuite:
    def test_get_mood_empty_tweets(self):
        mood_gatherer = TwitterMoodGatherer(MagicMock())
        mood = mood_gatherer.get_mood(query='foo')
        assert mood.polarity == 0
        assert mood.subjectivity == 0
