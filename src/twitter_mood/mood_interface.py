class MoodInterface:
    def __init__(self, polarity=0, subjectivity=0):
        self.__polarity = polarity
        self.__subjectivity = subjectivity
        pass

    @property
    def polarity(self):
        return self.__polarity

    @property
    def subjectivity(self):
        return self.__subjectivity

    def __add__(self, other):
        return MoodInterface(self.polarity + other.polarity,
                             self.subjectivity + other.subjectivity)

    def __radd__(self, other):
        return self

    def __truediv__(self, value):
        return MoodInterface(self.polarity / value, self.subjectivity / value)
