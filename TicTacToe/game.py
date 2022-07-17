from ai import Agent


from ai import Agent, RandomAgent

PRINT = False
class Game:
    
    def __init__(self, size:int = 3):
        self.size = size
        self.reset()
        self.result = []
    
    def reset(self):
        self.board = [[None for _ in range(self.size)] for _ in range(self.size)]
        
    def play(self, agent1, agent2):
        '''
        play method
        '''
        self.assemble(agent1, agent2)
        
        complete = False
        curr_turn = 'x'
        # always start with x
        count = 0
        self.agent1.game_init()
        self.agent2.game_init()
        while(not complete):
            if(PRINT):
                self.__print__()
            if(curr_turn == agent1.symbol):
                move = self.agent1.move(self.board)
                self.agent2.register_opponent_move(self.board, move)
            else:
                move = self.agent2.move(self.board)
                self.agent1.register_opponent_move(self.board, move)
                
            x, y = move // self.size, move % self.size
            self.board[x][y] = curr_turn
            

                
            status = self.check()
            if(status != None):
                complete = True
                
            count += 1
            if(count == self.size * self.size):
                break
            
            curr_turn = Game.flip(curr_turn)
                
        print('Result of match is {}'.format(status))
        
        self.agent1.backprop(status)
        self.agent2.backprop(status)
        self.result.append(1 if status == 'x' else -1 if(status == 'o') else 0)
            
        
    def assemble(self, agent1:Agent, agent2:Agent):
        if(agent2 == None):
            agent2 = RandomAgent('o')
        self.agent1 = agent1
        self.agent2 = agent2
        self.agent1.assign('x')
        self.agent2.assign('o')
        
        self.reset()
        
    def flip(curr_turn):
        if(curr_turn == 'x'):
            curr_turn = 'o'
        elif(curr_turn == 'o'):
            curr_turn = 'x'
            
        return curr_turn
    
    def check(self):
        # in each row
        cols = [set() for _ in range(self.size)]
        diag1 = set()
        diag2 = set()
        for row in self.board:
            r = set(row)
            if(r.__len__() == 1 and next(iter(r)) != None):
                return next(iter(r))
            for i in range(self.size):
                cols[i].add(row[i])
                
        for c in cols:
            if(c.__len__() == 1 and next(iter(c)) != None):
                return next(iter(c))
            
        for i in range(self.size):
            diag1.add(self.board[i][i])
            diag2.add(self.board[i][self.size-i-1])
            
        if(diag1.__len__() == 1 and next(iter(diag1)) != None):
            return next(iter(diag1))
        
        if(diag2.__len__() == 1 and next(iter(diag2)) != None):
            return next(iter(diag2))
        
        # check draw
        for row in self.board:
            for block in row:
                if(block == None):
                    return None
        
        return 'draw'
    
    def __print__(self):
        '''
        =============
        | o | x | o |
        | x | o | o |
        | x | x | x |
        =============
        '''
        
        n = self.size
        l = n*3 + 2*n
        
        print('='*l)
        for row in self.board:
            s = '| {} |'*n
            print(s.format(*[x if x is not None else ' ' for x in row]))
        print('='*l)