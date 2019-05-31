#coding=utf-8
import time
"""算法思路：
1.对于一个数独，每一个空格填入的候选值应该是确定的，首先计算每个空格可填入的候选值，并按照候选值的个数升序排列，
（首先选择确定性较大的空格填入）;
2.在填入候选值后，刷新数独矩阵，并重新计算空格位置的可选值;
3.当空格位置的候选值个数为0时，说明在前面某一步候选值填的有错，需要回溯，回溯错误上一步时，如果候选值个数为1，
说明错误还在前面，但需要将此处值重新置为0；
4.按照步骤3依次回溯，当回溯到候选值个数大于1时，（说明错误有可能是在此处发生），将指针指向此位置的下一个候选值填入，
在重新刷新记录插入位置和值的字典，并重复进行步骤1,2；
5.当记录步骤1的字典（空格位置及候选值）为空时，说明所有空格均已填完，则跳出所有循环
"""


class solution(object):
    def __init__(self, board):
        self.b = board
        self.possible_data = {} # 每个可能的空格需要填入的数字集合
        self.insert_data = [] # 记录插入的顺序及值
        self.t = 0

    def calculate_possible(self):
        _possible_data = {}
        for row in range(9):
            for column in range(9):
                if self.b[row][column] == 0:
                    new_row, new_column = row/3*3, column/3*3
                    new_range = self.b[new_row][new_column:new_column+3]+self.b[new_row+1][new_column:new_column+3]+self.b[new_row+2][new_column:new_column+3]
                    r = set(range(10))-set(self.b[row][:])-set([r[column] for r in self.b])-set(new_range)
                    _possible_data[str(row)+str(column)] = list(r)
        self.possible_data = sorted(_possible_data.items(), key=lambda x:len(x[1]))

    def start(self):
        start_time = time.time()
        while True:
            self.calculate_possible()
            if len(self.possible_data) == 0:
                break   # 无空格，数独填写完毕，退出
            key, value = self.possible_data[0]
            i = int(key[0])
            j = int(key[1])
            self.insert_data.append((i,j,value))
            if len(value) != 0:
                self.b[i][j] = value[0]
            else:
                self.insert_data.pop()
                for index in range(len(self.insert_data)):
                    self.t += 1
                    error_item = self.insert_data.pop()
                    i = error_item[0]
                    j = error_item[1]
                    value = error_item[2]
                    if len(value) == 1:
                        self.b[i][j] = 0
                    else:
                        self.b[i][j] = value[1]
                        self.insert_data.append((i,j,value[1:]))
                        break

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
