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
    def test2strike2spare(self):
        """simulate a Game with 2spare and 2 strikes"""
        self.game.roll(10)
        self.game.roll(5)
        self.game.roll(5)
        self.game.roll(10)
        self.game.roll(5)
        self.game.roll(5)
        self.rollMany(1,12)
        assert self.game.score()==83
    def test2strike2spare(self):
        """simulate a Game with all game with 9 pins"""
        self.rollMany(9,20)
        assert self.game.score()==180
    def test2strike2spare(self):
        """simulate a Game with random number"""
        self.game.roll(8)
        self.game.roll(7)
        self.game.roll(5)
        self.game.roll(1)
        self.game.roll(9)
        self.game.roll(6)
        self.rollMany(0,14)
        assert self.game.score()==36
    def test2strike2spare(self):
        """simulate a Game with one strike and one spere"""
        self.game.roll(10)
        self.game.roll(5)
        self.game.roll(5)
        self.rollMany(0,16)
        assert self.game.score()==30
    def rollMany(self, pins,rolls):
        """add the pins to the array"""
        for i in range(rolls):
            self.game.roll(pins)
            
if __name__ == '__main__':
    """ Unit Tests """
    unittest.main()
