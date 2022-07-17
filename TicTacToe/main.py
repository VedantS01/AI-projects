from ai import *
from game import Game
import random

def main():
    game = Game()
    
    agent1 = RandomAgent('x', random.randint(0, 100))
    agent2 = RandomAgent('o', random.randint(0, 100))
    
    game.reset()
    game.play(agent1, agent2)
    
    return

if __name__ == '__main__':
    main()