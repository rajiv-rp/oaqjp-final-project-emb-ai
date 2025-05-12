import unittest
from EmotionDetection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detection_joy(self):
        ''' test cases for emotion detector joy '''
        result = emotion_detector("I am glad this happened")['dominant_emotion']
        self.assertEqual(result, "joy")

    def test_emotion_detection_anger(self):
        ''' test cases for emotion detector anger'''
        result = emotion_detector("I am really mad about this")['dominant_emotion']
        self.assertEqual(result, "anger")

    def test_emotion_detection_disgust(self):
        ''' test cases for emotion detector disgust'''
        result = emotion_detector("I feel disgusted just hearing about this")['dominant_emotion']
        self.assertEqual(result, "disgust")

    def test_emotion_detection_sadness(self):
        ''' test cases for emotion detector sadness'''
        result = emotion_detector("I am so sad about this")['dominant_emotion']
        self.assertEqual(result, "sadness")

    def test_emotion_detection_fear(self):
        ''' test cases for emotion detector fear'''
        result = emotion_detector("I am really afraid that this will happen")['dominant_emotion']
        self.assertEqual(result, "fear")

    if __name__ == '__main__':
        unittest.main()