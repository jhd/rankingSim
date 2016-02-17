import matplotlib.pyplot as pyplot
import random
import itertools

class Player:
    pid = -1	
    skill = -1.0
    rank = 0
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
        player = Player(i, skill, 0)
        players.append(player)
    return players

def nextRound(players):
    for playerA, playerB in list(itertools.combinations(players, 2)):
        variance = random.uniform(-1, 1)
        if playerA.skill > playerB.skill + variance:
            playerA.rank += 1
        elif playerB.skill + variance > playerA.skill:
            playerB.rank += 1

def runSimulation(numPlayers, generations):

    players = generatePlayers(numPlayers)
    
    rankHistory = []

    for i in range(0, generations):
        for player in players:
            rankHistory.append((i, player.pid, player.rank))
        nextRound(players)
    for player in players:
        rankHistory.append((generations, player.pid, player.rank))
    
    for i in range(0, numPlayers):
        history = []
        for (rounds, pid, rank) in rankHistory:
            if i == pid:
                history.append((rounds, rank))
        pyplot.plot(range(0, generations+1), history, 's-')
            
    pyplot.show()

    #for player in players:
    #    print player.pid, player.skill, player.rank

runSimulation(10, 5)
