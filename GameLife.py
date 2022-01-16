import numpy as np
"""В нашем случае начальный массив создан изначально и width, height = (8,8)
(но где то есть маленбкая ошибка)"""


class CreateBoard:
    def __init__(self, width, height):  # где width - количество квадрат горизоньально, height-вертикально
        print('class CreateBoard is working...')
        self.width = width - 1
        self.height = height - 1
        # self.arr = np.zeros((self.width, self.height))
        self.arr = np.array([
            [1, 0, 0, 1, 0, 1, 0, 1],
            [0, 1, 0, 0, 0, 0, 0, 0],
            [1, 1, 0, 1, 0, 0, 1, 1],
            [1, 0, 0, 0, 0, 1, 1, 1],
            [0, 0, 1, 0, 1, 0, 0, 0],
            [1, 0, 1, 1, 0, 1, 1, 1],
            [0, 1, 1, 0, 0, 0, 1, 0],
            [0, 0, 1, 1, 0, 1, 0, 0]
        ])

        self.arr_zeros = np.zeros((8, 8))


class Update(CreateBoard):
    s = 0

    def __init__(self, width, height):
        super().__init__(width, height)

    def is_survive(self, index1, index2):
        """ Метод проверит что данной клеток выживет или нет """

        self.neighbor_cnt = 0

        if (index1 not in [0, self.height]) and (index2 not in [0, self.width]):
            if self.arr[index1 - 1][index2 - 1] == 1:  # верхний част
                self.neighbor_cnt += 1
            if self.arr[index1 - 1][index2] == 1:  # верхний част
                self.neighbor_cnt += 1
            if self.arr[index1 - 1][index2 + 1] == 1:  # верхний част
                self.neighbor_cnt += 1

            if self.arr[index1 + 1][index2 - 1] == 1:  # нижний част
                self.neighbor_cnt += 1
            if self.arr[index1 + 1][index2] == 1:  # нижний част
                self.neighbor_cnt += 1
            if self.arr[index1 + 1][index2 + 1] == 1:  # нижний част
                self.neighbor_cnt += 1

            if self.arr[index1][index2 - 1] == 1:  # левый бок
                self.neighbor_cnt += 1
            if self.arr[index1][index2 + 1] == 1:  # правый бок
                self.neighbor_cnt += 1
                # ------------------------------------------------------------------------
        if index1 == 0:
            if index2 == 0:
                if self.arr[index1][index2 + 1] == 1:
                    self.neighbor_cnt += 1
                if self.arr[index1 + 1][index2] == 1:
                    self.neighbor_cnt += 1
                if self.arr[index1 + 1][index2 + 1] == 1:
                    self.neighbor_cnt += 1
            if index2 == self.width:
                if self.arr[index1][index2 - 1] == 1:
                    self.neighbor_cnt += 1
                if self.arr[index1 + 1][index2] == 1:
                    self.neighbor_cnt += 1
                if self.arr[index1 + 1][index2 - 1] == 1:
                    self.neighbor_cnt += 1
            if index2 != 0 and index2 != self.width:
                if self.arr[index1][index2 - 1] == 1:
                    self.neighbor_cnt += 1
                if self.arr[index1][index2 + 1] == 1:
                    self.neighbor_cnt += 1
                if self.arr[index1 + 1][index2 - 1] == 1:
                    self.neighbor_cnt += 1
                if self.arr[index1 + 1][index2] == 1:
                    self.neighbor_cnt += 1
                if self.arr[index1 + 1][index2 + 1] == 1:
                    self.neighbor_cnt += 1

        if index1 == self.height:
            if index2 == 0:
                if self.arr[index1][index2 + 1] == 1:
                    self.neighbor_cnt += 1
                if self.arr[index1 - 1][index2] == 1:
                    self.neighbor_cnt += 1
                if self.arr[index1 - 1][index2 + 1] == 1:
                    self.neighbor_cnt += 1

            if index2 == self.width:
                if self.arr[index1][index2 - 1] == 1:
                    self.neighbor_cnt += 1
                if self.arr[index1 - 1][index2] == 1:
                    self.neighbor_cnt += 1
                if self.arr[index1 - 1][index2 - 1] == 1:
                    self.neighbor_cnt += 1

            if index2 != 0 and index2 != self.width:
                if self.arr[index1][index2 - 1] == 1:
                    self.neighbor_cnt += 1
                if self.arr[index1][index2 + 1] == 1:
                    self.neighbor_cnt += 1
                if self.arr[index1 - 1][index2 - 1] == 1:
                    self.neighbor_cnt += 1
                if self.arr[index1 - 1][index2] == 1:
                    self.neighbor_cnt += 1
                if self.arr[index1 - 1][index2 + 1] == 1:
                    self.neighbor_cnt += 1

        # ------------------------------------------------------------------
        if index2 == 0:
            if index1 != 0 and index1 != self.height:
                if self.arr[index1 - 1][index2] == 1:
                    self.neighbor_cnt += 1
                if self.arr[index1 - 1][index2 + 1] == 1:
                    self.neighbor_cnt += 1
                if self.arr[index1][index2 + 1] == 1:
                    self.neighbor_cnt += 1
                if self.arr[index1 + 1][index2] == 1:
                    self.neighbor_cnt += 1
                if self.arr[index1 + 1][index2 + 1] == 1:
                    self.neighbor_cnt += 1

        if index2 == self.width:
            if index1 != 0 and index1 != self.height:
                if self.arr[index1 - 1][index2] == 1:
                    self.neighbor_cnt += 1
                if self.arr[index1 - 1][index2 - 1] == 1:
                    self.neighbor_cnt += 1
                if self.arr[index1][index2 - 1] == 1:
                    self.neighbor_cnt += 1
                if self.arr[index1 + 1][index2] == 1:
                    self.neighbor_cnt += 1
                if self.arr[index1 + 1][index2] == 1:
                    self.neighbor_cnt += 1

        Update.s += 1
        # print(Update.s,'neighbor: ',self.neighbor_cnt)
        # print(self.neighbor_cnt)
        if self.neighbor_cnt >= 2:
            return True
        else:
            # print('Something went wrong')
            return False

    def is_born(self, index1, index2):
        """ Функция проверит что в данном клетке появится существо или нет """
        if self.arr[index1][index2] == 0:
            if self.neighbor_cnt == 3:
                return True
            else:
                return False

    def new_board(self):
        """ Этот метод создает новая доска и выведет ее"""

        for ind1 in range(self.height + 1):
            for ind2 in range(self.width + 1):
                if self.arr[ind1][ind2] == 1:
                    if self.is_survive(ind1, ind2):
                        self.arr_zeros[ind1][ind2] = 1
                    else:
                        self.arr_zeros[ind1][ind2] = 0
                else:
                    if self.is_born(ind1, ind2):
                        self.arr_zeros[ind1][ind2] = 1

        CreateBoard.arr = self.arr_zeros
        print(self.arr_zeros)


update = Update(8,8)

print(update.arr)

############## Создаем генератор

def generator():
    while True:
        yield update.new_board()

gen = generator()
#next(gen)