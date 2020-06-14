'''
Our application will store high scores for a video game
TO begin, our Game Entry class will take care of a high score entry
'''


class GameEntry:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def get_name(self):
        return self.name

    def get_score(self):
        return self.score

    def __str__(self):
        return '{0}, {1}'.format(self.name, self.score)


# To maintain a sequence of high scores, we develop a class names Scoreboard
# A scoreboard is limited to a certain number of high scores and a top score will only make it onto
# a full board if it the highest score. We use a list in order to manage the GameEntry instances

class Scoreboard:
    def __init__(self, capacity=10):
        self.board = [None] * capacity  # reserve space for future scores
        self.n = 0  # number of actual entries

    def __getitem__(self, k):
        return self.board[k]

    def __str__(self):
        return '\n'.join(str(self.board[j] for j in range(self.n)))

    def add(self, entry):
        score = entry.get_score()  # consider adding entry to high score

        # now we check to see if entry qualifies to be added to the board. yes if board not full or is higher than
        # last entry

        good = self.n < len(self.board) or score > self.board[-1].get_score()
        if good:
            if self.n < len(self.board):  # no socre will drop out
                self.n += 1  # overall number increases
            # shift lower score right to make room for new entry
            j = self.n - 1
            while j > 0 and self.board[j - 1].get_score() < score:
                self.board[j] = self.board[j - 1]
                j -= 1
            self.board[j] = entry
