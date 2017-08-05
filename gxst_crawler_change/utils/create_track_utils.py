# -*-coding:utf-8 -*-
import time

import random


class CreateTracklUtils(object):
    def __init__(self):
        pass

    def create_action(self, xpos):
        # print('init xpos is', str(xpos))
        actions = []
        self.init_pre_two(actions)
        self.make_two(actions)
        self.add_point(actions, xpos)
        self.make_point_list(actions, xpos)
        # print(actions)
        return actions

    def init_pre_two(self, actions):
        """
        添加最前面的两个点
        """
        actions.append([-1 - random.randint(19, 29), -1 - random.randint(19, 29), 0])
        actions.append([0, 0, 0])

    def make_two(self, actions):
        x, y, t = 0, 0, 0
        x = 3 + random.randint(0, 9)
        y = -2 + random.randint(0, 2)
        t = 10 * x + random.randint(0, 30)
        actions.append([x, y, t])
        x += random.randint(0, 9)
        y += -2 + random.randint(0, 2)
        t += 8 * x + random.randint(0, 24)
        actions.append([x, y, t])

    def add_point(self, actions, xpos):
        # p = []
        # xstep = 0
        t_offset = 80 + random.randint(0, 179)
        x = 0
        print('xpos is ', xpos)
        while x < xpos:
            p = actions[len(actions) - 1]
            xstep = self.get_x_offset(self.get_last_acc(actions), p[0], xpos)
            xs = p[0] + xstep
            curr_acc = self.get_acc(actions, xpos)
            t = abs(int(5 + random.randint(0, 19) if xstep == 0 else xstep * t_offset / curr_acc))
            t = p[2] + t
            y = self.get_y(p, xpos, curr_acc)
            actions.append([xs, y, t])
            x += xstep

    def pre_two_point(self, actions):
        actions.append([-1 - random.randint(0, 29), -1 - random.randint(0, 29), 0])
        actions.append([0, 0, 0])

    def get_y(self, p, xpos, curr_acc):
        """
        得到Y坐标
        :param p:
        :param xpos:
        :param curr_acc:
        :return:
        """
        x, y, offset = p[0], p[1], 0
        if x * 5 < xpos:
            if random.randint(0, 4) / 2 == 0:
                offset = 1
        elif x > (xpos * 0.8):
            if random.randint(0, 3) == 2:
                offset = 1
            else:
                offset = 0
        else:
            if curr_acc > 60:
                if random.randint(0, 4) % 2 == 0:
                    offset = 1
            else:
                if random.randint(0, 3) == 2:
                    offset = 1
        y += offset * (-2 + random.randint(0, 4))
        return y

    def make_point_list(self, actions, xpos):
        p = []
        t = 5
        while t > 3:
            p = actions[len(actions) - 1]
            if abs(p[0] - xpos) > 3:
                actions.append([p[0] + 1 + random.randint(0, 4) if xpos > p[0] else p[0] - 1 - random.randint(0, 4),
                                p[1] - 1 + random.randint(0, 4) if p[0] % 4 == 0 else p[1],
                                p[2] + 10 + random.randint(0, 49)])
                p = actions[len(actions) - 1]
                t = abs(xpos - p[0])
            else:
                break
        xnum = -3 + random.randint(0, 6)
        o = 4 + random.randint(0, 9)
        for i in range(0, abs(xnum) + 1):
            p = actions[len(actions) - 1]
            actions.append([xpos, p[1] + 1 + random.randint(0, 1) if p[0] % 2 == 0 else p[1] - 1 - random.randint(0, 1),
                            (p[2] + 10 * i + random.randint(0, 49))])
        p = actions[len(actions) - 1]
        actions.append([xpos, p[1], (p[2] + o * 20 + random.randint(0, 249))])

    def get_acc(self, actions, xpos):
        prAcc1 = self.get_last_acc(actions)
        mark = 0
        offset = 0.0
        if prAcc1 > 120:
            if random.randint(0, 4) % 4 == 0:
                mark = -1
                offset = random.randint(0, 19)
            else:
                mark = 0
        if prAcc1 < 20:
            if random.randint(0, 4) % 3 == 0:
                mark = 1
            else:
                mark = 0
        ac = mark * offset * 0.2 + 10 + random.randint(0, 19)
        return ac

    def get_x_offset(self, last_acc, x, xpos):
        """
        根据上个点的加速度和当前点的x坐标得到下一个点的x坐标
        :param last_acc:当前点的加速度
        :param x:当前点的x坐标
        :param xpos:distance
        :return:
        """
        at = 1.0  # 加速度决策因子
        if last_acc > 40:
            at = at - 1 / (last_acc / 40)
        elif last_acc > 20:
            at = at - 1 / 2
        else:
            at = at / 50
        xt = 1  # xpos位置决策因子
        s = (xpos / 5)
        if x < 2 * s:
            xt = 1 - xt * 0.7 / s
        elif x > 4 * s:
            at = (x - 4 * s) / (s * 2)
        else:
            at = 1 / (1 + random.randint(0, 2))

        t = xt + at
        if t > 1.6:
            if random.randint(0, 4) / 3 == 0:
                return random.randint(0, 20)
            if random.randint(0, 7) / 6 == 0:
                return random.randint(0, 16)
            return random.randint(0, 9) + 1
        elif t > 1:
            return random.randint(0, 7)
        else:
            return random.randint(0, 4)

    def get_last_acc(self, actions):
        """
        得到上一个点的加速度
        :param actions:
        :return:
        """
        res = 0
        p = actions[len(actions) - 1]
        p1 = actions[len(actions) - 2]
        if p[2] - p1[2] != 0:
            res = ((p[0] - p1[0]) * 100) / (p[2] - p1[2])
        else:
            res = (p[0] - p1[0]) * (50 + random.randint(0, 50))
        return res
