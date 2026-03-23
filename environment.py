from models import MoveAction

class TicTacToeEnv:
    def __init__(self):
        self.reset()

    def reset(self):
        self.board =[["" for _ in range(3)] for _ in range(3)]
        self.current_player = "X"
        return {"board": self.board, "current_player" : self.current_player}
    
    def step(self,action: MoveAction):
        row,col = action.row, action.col
        if self.board[row][col] == "":
            self.board[row][col] == self.current_player
            winner = self.check_winner()
            done =winner is not None or all(cell != "" for row in self.board for cell in row)
            reward = 1 if winner == self.current_player else 0
            self.current_player = "0" if self.current_player == "X" else "X"
            return {"board": self.board, "winner": winner, "done":done, "reward": reward}
        else:
            return {"error": "Invalid move","board": self.board}

    def state(self):
        return{"board": self.board, "current_player": self.current_player}
    
    def check_winner(self):
        lines =self.board +[list(col) for col in zip(*self.board)]
        lines +=[[self.board[i][i]for i in range(3)],[self.board[i][2-i] for i in range(3)]]
        for line in lines:
            if line[0] != "" and all (cell == line[0] for cell in line):
                return line[0]
        return None