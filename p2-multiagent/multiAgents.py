# multiAgents.py
# --------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


from util import manhattanDistance
from game import Directions
import random, util

from game import Agent

class ReflexAgent(Agent):
    """
    A reflex agent chooses an action at each choice point by examining
    its alternatives via a state evaluation function.

    The code below is provided as a guide.  You are welcome to change
    it in any way you see fit, so long as you don't touch our method
    headers.
    """


    def getAction(self, gameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {NORTH, SOUTH, WEST, EAST, STOP}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices) # Pick randomly among the best

        "Add more of your code here if you want to"

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition() ## 坐标
        newFood = successorGameState.getFood() ## 矩阵
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]
        "*** YOUR CODE HERE ***"
        newGhostDirection = [ghostState.getDirection() for ghostState in newGhostStates]
        newGhostPos = [ghostState.getPosition() for ghostState in newGhostStates]
        minGhostDist = 999999
        nearGhostIndex = -1
        for index, pos in enumerate(newGhostPos):
            if newScaredTimes[index] == 0:
                if minGhostDist > util.manhattanDistance(pos, newPos):
                    minGhostDist = util.manhattanDistance(pos, newPos)
                    nearGhostIndex = index
        minFoodDist = 999999
        for i in range(newFood.width):
            for j in range(newFood.height):
                if newFood[i][j]:
                    minFoodDist = min(minFoodDist, abs(i-newPos[0])+ abs(j-newPos[1]))

        if minGhostDist <= minFoodDist:
            return successorGameState.getScore() + minGhostDist * 0.1

        food_cnt = 0
        for i in range(newFood.width):
            for j in range(newFood.height):
                if util.manhattanDistance((i, j), newPos) < minGhostDist:
                    if newFood[i][j]:
                        food_cnt += 1
        return successorGameState.getScore() + food_cnt

def scoreEvaluationFunction(currentGameState):
    """
    This default evaluation function just returns the score of the state.
    The score is the same one displayed in the Pacman GUI.

    This evaluation function is meant for use with adversarial search agents
    (not reflex agents).
    """
    return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
    """
    This class provides some common elements to all of your
    multi-agent searchers.  Any methods defined here will be available
    to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

    You *do not* need to make any changes here, but you can if you want to
    add functionality to all your adversarial search agents.  Please do not
    remove anything, however.

    Note: this is an abstract class: one that should not be instantiated.  It's
    only partially specified, and designed to be extended.  Agent (game.py)
    is another abstract class.
    """
    def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
        self.index = 0  # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)
        self.cnt = 1  # 角色人数

class MinimaxAgent(MultiAgentSearchAgent):
    """
    Your minimax agent (question 2)
    """
    def minimax(self, state, dep, agentId):
        if state.isWin() or state.isLose():
            return self.evaluationFunction(state)
        if agentId == self.numAgents:
            if dep == self.depth:
                return self.evaluationFunction(state)
            return self.minimax(state, dep+1, 0)

        legalMoves = state.getLegalActions(agentId)
        bestScore = -999999 if agentId == 0 else 999999
        for action in legalMoves:
            neState = state.generateSuccessor(agentId, action)
            neScore = self.minimax(neState, dep, agentId+1)
            if agentId == 0:
                bestScore = max(bestScore, neScore)
            else:
                bestScore = min(bestScore, neScore)
        return bestScore

    def getAction(self, gameState):
        """
        Returns the minimax action from the current gameState using self.depth
        and self.evaluationFunction.

        Here are some method calls that might be useful when implementing minimax.

        gameState.getLegalActions(agentIndex):
        Returns a list of legal actions for an agent
        agentIndex=0 means Pacman, ghosts are >= 1

        gameState.generateSuccessor(agentIndex, action):
        Returns the successor game state after an agent takes an action

        gameState.getNumAgents():
        Returns the total number of agents in the game

        gameState.isWin():
        Returns whether or not the game state is a winning state

        gameState.isLose():
        Returns whether or not the game state is a losing state
        """
        "*** YOUR CODE HERE ***"
        self.numAgents = gameState.getNumAgents()

        bestScore = -999999
        bestAction = None
        for action in gameState.getLegalActions(0):
            neState = gameState.generateSuccessor(0, action)
            neScore = self.evaluationFunction(neState) if neState.isWin() or neState.isLose() else self.minimax(neState, 1, 1)
            if bestScore < neScore:
                bestScore = neScore
                bestAction = action
        return bestAction
        # util.raiseNotDefined()

class AlphaBetaAgent(MultiAgentSearchAgent):
    """
    Your minimax agent with alpha-beta pruning (question 3)
    """
    def alphabeta(self, state, dep, alpha, beta, agentId):
        if state.isWin() or state.isLose():
            return self.evaluationFunction(state), None
        if agentId == self.numAgents:
            if dep == self.depth:
                return self.evaluationFunction(state), None
            return self.alphabeta(state, dep+1, alpha, beta, 0)

        bestScore, bestAction = -999999 if agentId == 0 else 999999, None
        legalMoves = state.getLegalActions(agentId)
        for action in legalMoves:
            neState = state.generateSuccessor(agentId, action)
            neScore, neAct = self.alphabeta(neState, dep, alpha, beta, agentId+1)
            if agentId == 0:
                if bestScore < neScore:
                    bestScore, bestAction = neScore, action
                if bestScore > beta:
                    return bestScore, action
                alpha = max(alpha, bestScore)
            else:
                if bestScore > neScore:
                    bestScore, bestAction = neScore, action
                if bestScore < alpha:
                    return bestScore, action
                beta = min(beta, bestScore)
        return bestScore, bestAction

    def getAction(self, gameState):
        """
        Returns the minimax action using self.depth and self.evaluationFunction
        """
        "*** YOUR CODE HERE ***"
        self.numAgents = gameState.getNumAgents()
        bestScore, bestAction = self.alphabeta(gameState, 1, -999999, 999999, 0)
        return bestAction
        # util.raiseNotDefined()

class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """
    def expectimax(self, state, dep, agentId):
        if state.isWin() or state.isLose():
            return self.evaluationFunction(state)
        if agentId == self.cnt:
            if dep == self.depth:
                return self.evaluationFunction(state)
            return self.expectimax(state, dep + 1, 0)

        legalMoves = state.getLegalActions(agentId)
        bestScore = -999999 if agentId == 0 else 0
        for action in legalMoves:
            neState = state.generateSuccessor(agentId, action)
            neScore = self.expectimax(neState, dep, agentId + 1)
            if agentId == 0:
                bestScore = max(bestScore, neScore)
            else:
                bestScore += neScore / len(legalMoves)
        return bestScore

    def getAction(self, gameState):
        """
        Returns the expectimax action using self.depth and self.evaluationFunction

        All ghosts should be modeled as choosing uniformly at random from their
        legal moves.
        """
        "*** YOUR CODE HERE ***"
        self.cnt = gameState.getNumAgents()

        bestScore = -999999
        bestAction = None
        for action in gameState.getLegalActions(0):
            neState = gameState.generateSuccessor(0, action)
            neScore = self.evaluationFunction(neState) if neState.isWin() or neState.isLose() else self.expectimax(neState, 0, 1)
            if bestScore < neScore:
                bestScore = neScore
                bestAction = action
        return bestAction
        util.raiseNotDefined()

def betterEvaluationFunction(currentGameState):
    """
    Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
    evaluation function (question 5).

    DESCRIPTION: <write something here so we know what you did>
    """
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

# Abbreviation
better = betterEvaluationFunction
