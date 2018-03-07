from unittest.mock import MagicMock
from twitter_mood.mood_gatherer import TwitterMoodGatherer
from twitter_mood.mood_interface import MoodInterface

class TestGetMoodSuite:
    def test_get_mood_empty_tweets(self):
        twitter_mock = MagicMock()
        sentiment_mock = MagicMock()
        sentiment_mock.analyze.return_value = MoodInterface()
        mood_gatherer = TwitterMoodGatherer(twitter_mock, sentiment_mock)
        mood = mood_gatherer.get_mood(query='foo')
        assert mood.polarity == 0
        assert mood.subjectivity == 0

    def test_get_mood_single_tweet(self):
        twitter_mock = MagicMock()
        sentiment_mock = MagicMock()
        twitter_mock.query.return_value = ['bar']
        sentiment_mock.analyze.return_value = MoodInterface(-0.1, 0.8)

        mood_gatherer = TwitterMoodGatherer(twitter_mock, sentiment_mock)

        mood = mood_gatherer.get_mood(query='foo')
        assert mood.polarity == -0.1
        assert mood.subjectivity == 0.8

    def test_get_mood_multiple_tweets(self):
        twitter_mock = MagicMock()
        sentiment_mock = MagicMock()
        twitter_mock.query.return_value = ['bar', 'baz']
        sentiment_mock.analyze.side_effect = [MoodInterface(-0.3, 1),
                                              MoodInterface(-0.1, 0.8)]

        mood_gatherer = TwitterMoodGatherer(twitter_mock, sentiment_mock)

        mood = mood_gatherer.get_mood(query='foo')
        assert mood.polarity == -0.2
        assert mood.subjectivity == 0.9
