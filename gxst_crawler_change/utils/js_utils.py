# -*- coding: utf-8 -*-
import random


class UsrResponseGenerate(object):
    def userresponse_generate(self):
        l = self.l
        challenge = self.challenge
        c = challenge[32:]
        d = []
        for e in range(len(c)):
            f = ord(c[e])
            # print(type(f))
            de = f - 87 if f > 57 else f - 48
            d.append(de)
        # print(d)
        c = 36 * d[0] + d[1]
        # 用l生成g
        g = round(l) + c
        b = challenge[0:32]
        i = [[], [], [], [], []]
        j = {}
        k = 0
        # e = 0
        for e in range(len(b)):
            h = b[e]
            # 待定 j[h] || (j[h] = 1,i[k].push(h)
            if h not in j.keys():
                j[h] = 1
                i[k].append(h)
                k += 1
                k = 0 if k == 5 else k
        # print(i)
        # print(j)
        n = g
        o = 4
        p = ''
        q = [1, 2, 5, 10, 50]
        while n > 0:
            if n - q[o] >= 0:
                m = int(random.random() * len(i[o]))
                p += str(i[o][m])
                n -= q[o]
            else:
                i = i[:o] + i[o + 1:]
                q = q[:o] + q[o + 1:]
                o -= 1
        return p

    def __init__(self, l, challenge):
        self.l = l
        self.challenge = challenge
        self.userresponse_generate()


class ATrackGenerate(object):
    def gee_fun_f_run_c_e(self, f_child):
        b = [[1, 0], [2, 0], [1, -1], [1, 1], [0, 1], [0, -1], [3, 0], [2, -1], [2, 1]]
        c = "stuvwxyz~"
        for k in range(len(b)):
            if f_child[0] == b[k][0] and f_child[1] == b[k][1]:
                return c[k]
        return 0

    def gee_fun_f_run_c(self, c):
        g = []
        h = []
        i = []
        f = c
        for j in range(len(f)):
            # fun e、d  !!!
            b = self.gee_fun_f_run_c_e(f[j])
            if b:
                h.append(b)
            else:
                g.append(self.gee_fun_f_run_c_d(f[j][0]))
                h.append(self.gee_fun_f_run_c_d(f[j][1]))
            i.append(self.gee_fun_f_run_c_d(f[j][2]))
        # result = g.join("") + "!!" + h.join("") + "!!" + i.join("")
        res = "".join(g) + "!!" + "".join(h) + "!!" + "".join(i)
        return res

    def gee_fun_f_run_c_d(self, xpos):
        b = "()*,-./0123456789:?@ABCDEFGHIJKLMNOPQRSTUVWXYZ_abcdefghijklmnopqr"
        c = len(b)
        d = ""
        e = abs(xpos)
        f = int(e / c)
        if f >= c:
            f = c - 1
        if f:
            d = b[f]
        e = e % c
        g = ""
        g = g + "!" if xpos < 0 else g
        g = g + "$" if d else g
        return g + d + b[e]

    def gee_fun_c_run_Qt(self, Qt):
        g = []
        e = []
        f = 0
        for h in range(len(Qt) - 1):
            # xpos
            b = round(Qt[h + 1][0] - Qt[h][0])
            # ypos
            c = round(Qt[h + 1][1] - Qt[h][1])
            # passtime
            d = round(Qt[h + 1][2] - Qt[h][2])
            # trace list
            g.append([b, c, d])
            if not (b == 0 and c == 0 and d == 0):
                if b == 0 and c == 0:
                    f += d
                else:
                    e.append([b, c, d + f])
                    f = 0
            else:
                pass
        if f != 0:
            e.append([b, c, f])
            return e
        else:
            return e

    def start_gen(self):
        cqt = self.gee_fun_c_run_Qt(self.trace)
        ann = self.gee_fun_f_run_c(cqt)
        # print('ann is', ann)
        return ann

    def __init__(self, trace):
        self.trace = trace
