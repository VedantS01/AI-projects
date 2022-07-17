import numpy as np
from scipy.special import softmax
import random

class Agent:
    '''
    Agents derived from this class should provide their own move method
    def move(self, board:List) -> int
    '''
    
    def __init__(self, symbol):
        self.symbol = symbol
        pass
    
    def get_empty(self, board):
        list_ = []
        x = 0
        size = len(board)
        for row in board:
            y = 0
            for block in row:
                if(block == None):
                    list_.append(size*x + y)
                y += 1
            x += 1   
        return list_
    
    def assign(self, symbol):
        self.symbol = symbol
        
    
    def game_init(self):
        pass
    
    def backprop(self, status):
        pass
    
    def register_opponent_move(self, board, move):
        pass


class RandomAgent(Agent):
    
    def __init__(self, symbol, seed:int = 0):
        super().__init__(symbol)
        self.random = random.Random(seed)
        
        
    def move(self, board):
        moves = self.get_empty(board)
        return self.random.choice(moves)
        
class QAgent(Agent):
    
    def __init__(self, symbol, size:int, gamma:float=0.9, alpha:float=0.4, seed:int = 0):
        super().__init__(symbol)
        self.q_table = np.zeros((3**(size*size), size*size))
        self.alpha = alpha
        self.gamma = gamma
        self.random = random.Random(seed)
        
    def game_init(self):
        self.state_action_pairs = []
        pass
        
    def move(self, board):
        moves = self.get_empty(board)
        state = self.get_state(board)
        choices = softmax(self.q_table[state, moves])
        action = random.choices(moves, weights=choices, k=1)[0]
        self.state_action_pairs.append((state, action, True))
        return action
    
    def register_opponent_move(self, board, move):
        state = self.get_state(board)
        self.state_action_pairs.append((state, move, False))
        
    def backprop(self, status):
        if(status == self.symbol):
            # positive pipe
            r = 1
            i = len(self.state_action_pairs) - 1
            state, action, is_self = self.state_action_pairs[0]
            # debug mode
            print('state action pairs: {}'.format(self.state_action_pairs))
            print('backprop starts.')
            for pair in self.state_action_pairs[1:]:
                next_state, next_action, is_self_next = pair
                print('State {} Action {} Q Value {} Is_self {}'.format(state, action, self.q_table[state, action], is_self))
                if(is_self):
                    self.q_table[state, action] += self.alpha*(r + self.q_table[next_state].min()*(self.gamma**i) - self.q_table[state, action])
                else:
                    self.q_table[state, action] += self.alpha*(r + self.q_table[next_state].max()*(self.gamma**i) - self.q_table[state, action])
                print('State {} Action {} Q Value {} Is_self {}'.format(state, action, self.q_table[state, action], is_self))
                i -= 1
                state = next_state
                action = next_action
                is_self = is_self_next
            
        elif(status == 'draw'):
            # nothing to do
            return
        else:
            # negative pipe
            r = -2
            i = len(self.state_action_pairs) - 1
            state, action, is_self = self.state_action_pairs[0]
            # debug mode
            print('state action pairs: {}', self.state_action_pairs)
            print('backprop starts.')
            for pair in self.state_action_pairs[1:]:
                next_state, next_action, is_self_next = pair
                print('State {} Action {} Q Value {} Is_self {}', state, action, self.q_table[state, action], is_self)
                if(is_self):
                    self.q_table[state, action] += self.alpha*(r + self.q_table[next_state].min()*self.gamma - self.q_table[state, action])
                else:
                    self.q_table[state, action] -= self.alpha*(r + self.q_table[next_state].max()*self.gamma - self.q_table[state, action])
                print('State {} Action {} Q Value {} Is_self {}', state, action, self.q_table[state, action], is_self)
                i -= 1
                state = next_state
                action = next_action
                is_self = is_self_next
        pass
    
    def get_state(self,board):
        state = 0
        size = len(board)
        for i in range(size):
            for j in range(size):
                pos = i*size + j
                b = board[i][j]
                state = 3*state
                if(b == None):
                    continue
                if(b == 'x'):
                    state += 1
                else:
                    state += 2
                    
        return state
        