import unittest
from translator import frenchToEnglish, englishToFrench

class TestTranslator(unittest.TestCase):
    def test_1(self):
        self.assertEqual(frenchToEnglish('Bonjour'),'Hello')
        self.assertEqual(frenchToEnglish(None),None)
        self.assertEqual(frenchToEnglish(''),'')

    def test_2(self):
        self.assertEqual(englishToFrench('Hello'), 'Bonjour')
        self.assertEqual(englishToFrench(None),None)
        self.assertEqual(englishToFrench(''),'')

if __name__=='__main__':
    unittest.main()
    
