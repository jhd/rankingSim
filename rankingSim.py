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

def pickPair(players, method, playerA = None):
    if method == 'random':
        return itertools.combinations(players, 2)
    if method == 'similar':
        if playerA == None:
            return sorted(players, key = lambda x: x.rank)
        else:
            return min(players, key = lambda x: (abs(x.rank - playerA.rank)) if x.pid != playerA.pid else float('inf'))
    else: 
        return (None, None)

def playerMatch(playerA, playerB):
    if playerA.skill >= playerB.skill:
        return playerA
    else:
        return playerB

def generatePlayers(numPlayers):
    players = []
    for i in range(0, numPlayers):
        skill = random.uniform(0, 10)
        player = Player(i, skill, skill)
        players.append(player)
    return players

def elo(playerA, playerB):
    probA = 1/(1+pow(10, (playerB.rank - playerA.rank)/400))
    probB = 1/(1+pow(10, (playerA.rank - playerB.rank)/400))

    return (probA, probB)

def nextRound(players):
    #for playerA, playerB in list(itertools.combinations(players, 2)):
    for playerA, playerB in zip(pickPair(players, 'similar'), pickPair(players, 'similar')[1:]):
        print playerA.pid, playerA.rank, playerA.skill, playerB.pid, playerB.rank, playerB.skill
        variance = random.uniform(-1, 1)
        (expectedA, expectedB) = elo(playerA, playerB)
        if playerA.skill > playerB.skill + variance:
            playerA.rank += 1 - expectedA
            playerB.rank -= 1 - expectedB
        elif playerB.skill + variance > playerA.skill:
            playerA.rank -= 1 - expectedA
            playerB.rank += 1 - expectedB

def runSimulation(numPlayers, generations):

    players = generatePlayers(numPlayers)
    
    rankHistory = []

    for i in range(0, generations):
        for player in players:
            rankHistory.append((i, player.pid, player.rank))

        #for player in players:
        #    print player.pid, player.rank, player.skill
        nextRound(players)

    for player in players:
        rankHistory.append((generations, player.pid, player.rank))
    
    for player in players:
        history = []
        for (rounds, pid, rank) in rankHistory:
            if player.pid == pid:
                history.append(rank)
        pyplot.plot(range(0, generations+1), history, 's-', label = str(player.skill))
           
    pyplot.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=-1)
    pyplot.show()

    #for player in players:
    #    print player.pid, player.skill, player.rank

runSimulation(10, 50)
