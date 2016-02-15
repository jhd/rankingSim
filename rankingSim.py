import matplotlib.pyplot as pyplot
import random

class Player:
    pid = -1	
    skill = -1.0
    rank = -1
    def __init__(self, newpid, newskill, newrank):
        self.pid = newpid
        self.skill = newskill
        self.rank = newrank

def playerMatch(playerA, playerB):
    if playerA.skill >= playerB.skill:
        return playerA
    else:
        return playerB

def generatePlayers(numPlayers):
    players = []
    for i in range(0, numPlayers):
        skill = random.uniform(0, 10)
        player = Player(i, skill, -1)
        players.append(player)
    return players

def nextRound(players):
    pass

def runSimulation(numPlayers, generations):

    players = generatePlayers(numPlayers)

    for i in range(0, generations):
        nextRound(players)
    for player in players:
        print player.skill

runSimulation(10, 10)
