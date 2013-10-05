import unittest
import poker

class TestPoker(unittest.TestCase):
    '''Example unittest test methods for poker'''

    def test_poker_straight_flush(self):
        '''Test get straight_flush'''
        actual = poker.straight_flush(['JC', 'TC', '9C', '8C', '7C'])
        expected = True
        self.assertEqual(actual, expected)

    def test_poker_straight(self):
        '''Test get straight'''
        actual = poker.straight(['JC', 'TC', '9C', '8C', '7C'])
        expected = True
        self.assertEqual(actual, expected)

    def test_poker_flush(self):
        '''Test get flush'''
        actual = poker.flush(['JC', 'TC', '9C', '8C', '7C'])
        expected = True
        self.assertEqual(actual, expected)
        
    def test_poker_full_house(self):
        '''Test get full_house'''
        actual = poker.fullhouse(['3', '3', '3', '4', '4'])
        expected = True
        self.assertEqual(actual, expected)
    def test_four_of_a_kind(self)
        '''Test get four_of_a_kind'''
        actual = poker.kind(4, [7,7,7,7,5])
        expected = 7
        self.assertEqual(actual, expected)



if __name__ == '__main__':
    unittest.main(exit=False)
