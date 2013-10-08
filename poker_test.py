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
        actual = poker.full_house([3, 3, 3, 4, 4])
        expected = True
        self.assertEqual(actual, expected)
        
    def test_poker_four_of_kind(self):
        '''Test get four_of_kind'''
        actual = poker.kind(4, [7, 7, 7, 7, 5])
        expected = 7
        self.assertEqual(actual, expected)

    def test_poker_three_of_kind(self):
        '''Test get three_of_kind'''
        actual = poker.kind(3, [4, 7, 7, 7, 5])
        expected = 7
        self.assertEqual(actual, expected)

    def test_poker_one_pair(self):
        '''Test get one_pair'''
        actual = poker.kind(2, [4, 6, 7, 7, 5])
        expected = 7
        self.assertEqual(actual, expected)

    def test_poker_twopair(self):
        '''Test get twopair'''
        actual = poker.twopair([9, 9, 8, 7, 7])
        expected = (9, 7)
        self.assertEqual(actual, expected)

    def test_poker_high_rank(self):
        '''Test get high_rank'''
        actual = poker.hand_rank(['4S', '3H', '9D', '8C', 'TS'])
        expected = (0, [10, 9, 8, 4, 3])
        self.assertEqual(actual, expected)

    def test_poker_hand_rank(self):
        '''Test get hand_rank'''
        actual = poker.hand_rank(['5S', '3H', '9D', '8C', '8S'])
        expected = (1, 8, [9, 8, 8, 5, 3]) 
        self.assertEqual(actual, expected)

    def test_poker_all_max(self):
        '''Test get all_max'''
        actual = poker.all_max([['5S', '3H', '9D', '8C', '8S'],['JC', 'TC', '9C', '8C', '7C']])
        expected = [['JC', 'TC', '9C', '8C', '7C']]
        self.assertEqual(actual, expected)

    def test_poker_rank(self):
        '''Test get rank'''
        actual = poker.rank(['5S', '3H', '9D', '8C', '8S'])
        expected = [9, 8, 8, 5, 3]
        self.assertEqual(actual, expected)

    def test_poker_show_rank(self):
        '''Test get show_rank'''
        actual = poker.show_rank(['JC', 'TC', '9C', '8C', '7C'])
        expected = 'Straight flush'
        self.assertEqual(actual, expected)

    def test_poker_poker(self):
        '''Test get poker'''
        actual = poker.poker([['5S', '5H', '5D', '5C', '4S'],['JC', 'TC', '9C', '8H', '7S']])
        expected = ([['5S', '5H', '5D', '5C', '4S']], 'Four of a kind')
        self.assertEqual(actual, expected)

        
        
     


if __name__ == '__main__':
    unittest.main(exit=False)
