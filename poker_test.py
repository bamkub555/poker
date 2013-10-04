'''poker_test.py'''
import unittest
import poker

class TestPoker(unittest.Testcase):
    '''Example unittest test methods for poker'''

    def test_poker_straight_flush(self):
        '''Test get straightflush'''

        
    actual = poker.straight_flush(['JC', 'TC', '9C', '8C', '7C'])
    expected = 8
    self.assertEqual(actual, expected)



if __name__ == '__main__':
    unittest.main(exit=False)
