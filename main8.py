import sys


class SolveBoard:
    def __init__(self, board):
        self.board = board
        self.count_F = 0
        self.count_for_every_path = [-1] * 8

    def place_F(self, x, y):
        self.fill_x(y)
        self.fill_y(x)
        self.fill_first_diagonal(x, y)
        self.fill_second_diagonal(x, y)
        self.board[y][x] = 'F'

    def remove_F(self, x, y):
        self.board[y][x] = 0
        self.remove_x(y)
        self.remove_y(x)
        self.remove_first_diagonal(x, y)
        self.remove_second_diagonal(x, y)

    def cage_check(self, x, y):
        for j in range(len(self.board)):
            if self.board[y][j] == 'F':
                return False

        for j in range(len(self.board)):
            if self.board[j][x] == 'F':
                return False

        j = x
        k = y
        while j != 0 and k != 0:
            j -= 1
            k -= 1

        while j != -1 and k != -1 and j != 8 and k != 8:
            if self.board[k][j] == 'F':
                return False
            j += 1
            k += 1

        j = x
        k = y
        while k != 0 and j != 7:
            j += 1
            k -= 1

        while j != -1 and k != -1 and j != 8 and k != 8:
            if self.board[k][j] == 'F':
                return False
            j -= 1
            k += 1

        return True

    def fill_x(self, y):
        for j in range(len(self.board)):
            self.board[y][j] = 1

    def fill_y(self, x):
        for j in range(len(self.board)):
            self.board[j][x] = 1

    def fill_first_diagonal(self, x, y):
        j = x
        k = y
        while j != 0 and k != 0:
            j -= 1
            k -= 1

        while j != -1 and k != -1 and j != 8 and k != 8:
            self.board[k][j] = 1
            j += 1
            k += 1

    def fill_second_diagonal(self, x, y):
        j = x
        k = y
        while k != 0 and j != 7:
            j += 1
            k -= 1

        while j != -1 and k != -1 and j != 8 and k != 8:
            self.board[k][j] = 1
            j -= 1
            k += 1

    def print(self):
        for f in self.board:
            print(f)

    def remove_x(self, y):
        for j in range(len(self.board)):
            if self.cage_check(j, y):
                self.board[y][j] = 0

    def remove_y(self, x):
        for j in range(len(self.board)):
            if self.cage_check(x, j):
                self.board[j][x] = 0

    def remove_first_diagonal(self, x, y):
        j = x
        k = y
        while j != 0 and k != 0:
            j -= 1
            k -= 1

        while j != -1 and k != -1 and j != 8 and k != 8:
            if self.cage_check(j, k):
                self.board[k][j] = 0

            j += 1
            k += 1

    def remove_second_diagonal(self, x, y):
        j = x
        k = y
        while k != 0 and j != 7:
            j += 1
            k -= 1

        while j != -1 and k != -1 and j != 8 and k != 8:
            if self.cage_check(j, x):
                self.board[k][j] = 0

            j -= 1
            k += 1

    def put_8_F(self, num_F):
        if self.count_for_every_path[num_F] == -1:
            self.count_for_every_path[num_F] += 1
        flag = False
        for q in range(self.count_for_every_path[num_F], 8):
            self.count_for_every_path[num_F] = q
            if self.board[num_F][q] == 'F':
                break
            if self.board[num_F][q] == 0:
                self.place_F(q, num_F)
                self.count_F += 1
                self.count_for_every_path[num_F] = q
                if self.count_F == 8:
                    self.print()
                    sys.exit("8 complete")
                flag = True
                break

        if not flag:
            flag_local = False
            for g in range(8):
                if self.board[num_F][g] == 'F':
                    self.remove_F(g, num_F)

                    for p in range(len(self.board)):
                        for h in range(len(self.board)):
                            if self.board[p][h] != 'F':
                                if self.cage_check(h, p):
                                    self.board[p][h] = 0
                                else:
                                    self.board[p][h] = 1

                    self.count_F -= 1
                    if self.count_for_every_path[num_F] != 7:
                        self.count_for_every_path[num_F] += 1
                        self.put_8_F(num_F)
                    else:
                        self.count_for_every_path[num_F] = -1
                    flag_local = True
                    break

            if not flag_local:
                self.count_for_every_path[num_F] = -1

            self.put_8_F(num_F - 1)
        else:
            self.put_8_F(num_F + 1)


a = 8
mas = [0] * a
for i in range(a):
    mas[i] = [0] * a

boards = SolveBoard(mas)
boards.put_8_F(0)
