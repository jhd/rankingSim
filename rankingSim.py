import matplotlib.pyplot as pyplot
import random

class Player:
    skill = -1.0
    rank = -1
    def __init__(this, newskill, newrank):
        skill = newskill
        rank = newrank

def playerMatch(playerA, playerB):
    if playerA.skill >= playerB.skill:
        return playerA
    else:
        return playerB

def generatePlayers(numPlayers):
    players = []
    for i in range(0, numPlayers):
        skill = random.uniform(0, 10)
        players.append(Player(skill, -1))
    return players

def nextRound(players):
    if len(players) == 1:
        return players
    nextGen = []
    for player in players:
        nextGen.append(playerMatch(player, random.choice(players)))
    return nextGen

def runSimulation(numPlayers, generations):
    players = generatePlayers(numPlayers)
    for i in range(0, generations):
        players = nextRound(players)
    for player in players:
        print player.skill

runSimulation(10, 10)
