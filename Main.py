import unittest
import BowlingGame

class TestBowlingGame(unittest.TestCase):

    def setUp(self):
        self.game = BowlingGame.BowlingGame()
        """Called at the start of every"""

    def testGutterGame(self):
        """simulate a Game with not having one pin down"""
        for i in range(0, 20):
            self.game.roll(0)
        assert self.game.score()==0
    def testAllOnes(self):
        """simulate a Game with 1 pin down in all games"""
        self.rollMany(1, 20)
        assert self.game.score()==20
    def testOneSpare(self):
        """simulate a Game with 1 spare"""
        self.game.roll(5)
        self.game.roll(5)
        self.game.roll(3)
        self.rollMany(0,17)
        assert self.game.score()==16
    def testOneStrike(self):
        """simulate a Game with 1 strick"""
        self.game.roll(10)
        self.game.roll(4)
        self.game.roll(3)
        self.rollMany(0,16)
        assert  self.game.score()==24
    def testPerfectGame(self):
        """simulate a Game with strick in all games"""
        self.rollMany(10,12)
        assert self.game.score()==300
    def testOneSpare(self):
        """simulate a Game with spare in all games"""
        self.rollMany(5,21)
        assert self.game.score()==150
    def rollMany(self, pins,rolls):
        """add the pins to the array"""
        for i in range(rolls):
            self.game.roll(pins)
            
if __name__ == '__main__':
    """ Unit Tests """
    unittest.main()
