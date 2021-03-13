from time import strftime, localtime
import os.path

class Match:

    def __init__(self, home, away):
        self.home = home
        self.away = away
        self.homeScore = int(0)
        self.awayScore = int(0)
        self.matchActive = 1
        self.date = strftime('%Y%m%d', localtime())
        self.path = r"D:\Computing\Python\MyPythonScripts\Footy Python\Match Update\files"
        self.file = (self.date + '.' + self.home + self.away + '.txt')
        self.fileName = os.path.join(self.path, self.file)
        self.time = ''
        self.scoreLine = ''
        self.event = ''
        
    def writeLine(self, line):
        with open(self.fileName, "a+") as f:
            f.write(line + "\n")

    def setScore(self):
        self.scoreLine = (self.home + ' ' + str(self.homeScore) + ' ' + self.away + ' ' + str(self.awayScore))

    def printScore(self):
        self.time = strftime('%I:%M %p', localtime())
        print('Current score is ' + self.scoreLine)
        self.writeLine(self.time + ' | ' + self.scoreLine)
        
    def changeScore(self, team):
        if self.home == team:
            self.homeScore += 1
            self.setScore()
        else:
            self.awayScore += 1
            self.setScore()
            
    def correctScore(self, team):
        if self.home == team:
            self.homeScore -= 1
            self.setScore()
        else:
            self.awayScore -= 1
            self.setScore()
    
    def mainMenu(self):
        print('********************')
        print('1 - General event')
        print('2 - Goal scored')
        print('3 - Show current score')
        print('4 - Score correction')
        print('5 - Half time')
        print('6 - Full time')
        self.event = input('Choose an event: ')

    def generalEvent(self):
        print('************')
        minute = input('What minute: ')
        genEvent = str(input('What happened: '))
        self.time = strftime('%I:%M %p', localtime())
        genEventLine = f"{self.time} | {minute} | {genEvent}"
        self.writeLine(genEventLine)
    
    def goalScored(self):
        print('******************')
        print('1: ' + self.home)
        print('2: ' + self.away)
        scoringTeam = int(input('Which team scored: '))
        minute = str(input('What minute: '))
        scoreEvent = str(input('What happened: '))
      
        self.time = strftime('%I:%M %p', localtime())
        scoreEventLine = f"{self.time} | {minute} | {scoreEvent}"

        if scoringTeam == 1:
            self.writeLine(self.time + ' | ' + minute + ' | ' + self.home + ' scored!')
            self.changeScore(self.home)
            self.setScore()
            self.writeLine(self.scoreLine)
            self.writeLine(scoreEventLine)
        else:
            self.writeLine(self.time + ' | ' + minute + ' | ' + self.away + ' scored!')
            self.changeScore(self.away)
            self.setScore()
            self.writeLine(self.scoreLine)
            self.writeLine(scoreEventLine)
            
    def removeGoal(self):
        print('******************')
        print('Current score is: ' + self.scoreLine)
        print('1: ' + self.home)
        print('2: ' + self.away)
        removeGoal = input('Remove which team\'s goal: ')
        self.correctScore(int(removeGoal))
        print('Updated score is: ' + self.scoreLine)
        
    def startMatch(self):
        self.setScore()
        while self.matchActive == 1:
            self.mainMenu()

            if int(self.event) == 1:
                self.generalEvent()

            elif int(self.event) == 2:
                self.goalScored()
                    
            elif int(self.event) == 3:
                self.printScore()
                    
            elif int(self.event) == 4:
                self.removeGoal()        
                
            elif int(self.event) == 5:
                self.setScore()
                self.writeLine('********************')
                self.writeLine('Half time')
                self.writeLine(self.scoreLine)
                self.writeLine('********************')
                                
            elif int(self.event) == 6:
                self.matchActive = 0
                self.writeLine('********************')
                self.writeLine('Full time')
                self.writeLine(self.scoreLine)
                self.writeLine('********************')

                if self.homeScore > self.awayScore:
                    self.writeLine(self.home + ' wins!')
                    self.writeLine(self.scoreLine)
                elif self.homeScore < self.awayScore:
                    self.writeLine(self.away + ' wins!')
                    self.writeLine(self.scoreLine)
                else:
                    self.writeLine('The match is a draw')
                    self.writeLine(self.scoreLine)
                
            else:
                continue


playMatch = Match('NEW','SOU')
