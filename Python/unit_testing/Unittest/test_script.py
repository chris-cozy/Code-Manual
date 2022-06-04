import unittest
import script

class TestScript(unittest.TestCase):

    def test_one_word(self):
        '''
        This is the general structure of a test
        '''
        text = 'python'
        result = script.caps(text)
        self.assertEqual(result, 'Python')
    
    def test_multiple_words(self):
        text = 'monty python'
        result = script.caps(text)
        self.assertEqual(result, 'Monty Python')

if __name__ == '__main__':
    unittest.main()