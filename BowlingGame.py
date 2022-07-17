class BowlingGame:
    def __init__(self):
        self.rolls=[]
        """pins array"""
        
    def roll(self,pins):
        """add pins to array"""
        self.rolls.append(pins)

    def score(self):
        """
        going to calculate the total score the
        player score in all games
        """
        totalarray = len(self.rolls)
        """Total bumber of times the player use the ball"""
        result = 0
        """total result of the game"""
        rollIndex=0
        """What index from array"""
        for frameIndex in range(totalarray):
            if self.isStrike(rollIndex):
                result += self.stickeScore(rollIndex)
                rollIndex +=1
            elif self.isSpare(rollIndex):
                result += self.spareScore(rollIndex)
                rollIndex +=2
            else:
                result += self.frameScore(rollIndex)
                rollIndex +=2
            if result >= 300:
                return result
            if rollIndex >= totalarray:
                return result
            if rollIndex > 19:
                return result

    def isStrike(self, rollIndex):
        """going to check if is strike frame"""
        return self.rolls[rollIndex] == 10
    def isSpare(self, rollIndex):
        """going to check if is spare frame"""
        return self.rolls[rollIndex] + self.rolls[rollIndex + 1]==10
    def stickeScore(self,rollIndex):
        """returns Score for strike frame and goes to next frame"""
        return  10 + self.rolls[rollIndex + 1] + self.rolls[rollIndex + 2]
    def spareScore(self,rollIndex):
        """returns Score for spare frame and goes to next frame"""
        return  10 + self.rolls[rollIndex + 2]
    def frameScore(self, rollIndex):
        """returns Score for normal frame and goes to next frame"""
        return self.rolls[rollIndex] + self.rolls[rollIndex + 1]
