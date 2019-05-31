#coding=utf-8
import time


class solution(object):
    def __init__(self, board):
        self.b = board
        self.t = 0

    def check(self, i, j, x):
        if x in self.b[i]:
            return False
        for row in self.b:
            if x==row[j]:
                return False
        new_row, new_column = i/3*3, j/3*3
        new_range = self.b[new_row][new_column:new_column+3]+self.b[new_row+1][new_column:new_column+3]+self.b[new_row+2][new_column:new_column+3]
        if x in new_range:
            return False
        else:
            return True

    def get_next(self, i, j):
        for jj in range(j+1, 9):
            if self.b[i][jj] == 0:
                return i, jj
        for ii in range(i+1, 9):
            for jj in range(9):
                if self.b[ii][jj] == 0:
                    return ii, jj
        return -1, -1


    def fill(self, i, j):
        if self.b[i][j] == 0:
            for x in range(1,10):
                self.t += 1
                if self.check(i,j,x):
                    self.b[i][j] = x
                    next_i, next_j = self.get_next(i,j)
                    if next_i == -1:
                        return True
                    else:
                        end = self.fill(next_i, next_j)
                        if end:
                            return True
                        else:
                            self.b[i][j] = 0


    def start(self):
        start_time = time.time()
        if self.b[0][0] == 0:
            self.fill(0,0)
        else:
            i,j = self.get_next(0,0)
            self.fill(i,j)
        end_time = time.time()
        cost_time = end_time-start_time
        print cost_time
        print self.t
        for row in range(9):
            print self.b[row]
        return self.b



s=solution([[8,0,0,0,0,0,0,0,0],
        [0,0,3,6,0,0,0,0,0],
        [0,7,0,0,9,0,2,0,0],
        [0,5,0,0,0,7,0,0,0],
        [0,0,0,8,4,5,7,0,0],
        [0,0,0,1,0,0,0,3,0],
        [0,0,1,0,0,0,0,6,8],
        [0,0,8,5,0,0,0,1,0],
        [0,9,0,0,0,0,4,0,0]])
s.start()

s = solution([[0,0,0,9,5,0,0,0,2],
            [9,0,2,0,1,0,7,0,0],
            [0,0,0,0,0,3,0,0,5],
            [0,2,3,1,9,0,4,0,0],
            [0,0,9,0,0,0,5,0,0],
            [0,0,4,0,3,2,6,9,0],
            [3,0,0,8,0,0,0,0,0],
            [0,0,5,0,6,0,8,0,4],
            [7,0,0,0,2,4,0,0,0]]
        )


s.start()
