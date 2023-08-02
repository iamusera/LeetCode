#!/usr/bin/ python3
# -*- coding: utf-8 -*-
"""
    @Author: iamusera
    @date: 2023-08-02 15:21
    @description: 
"""

"""
解法1
"""
while True:
    try:
        # 金额限制总价，物品数量
        total, k = list(map(int, input().split(" ")))
        # 单价
        W = {}
        # 单价* 重要程度=价值
        V = {}
        # 因为价格是10的倍数，为方便运算，价格/10
        total = int(total )
        # 主件个数
        main_key = []
        # 构造字典
        for i in range(1, k + 1):
            W[i] = [0, 0, 0]
            V[i] = [0, 0, 0]
        for i in range(k):
            # 单价，重要程度，类别
            v, p, q = list(map(int, input().split(" ")))
            if q == 0:
                W[i + 1][0] = int(v )
                V[i + 1][0] = int(v * p )
                main_key.append(i + 1)
            else:
                if W[q][1] == 0:
                    W[q][1] = int(v )
                    V[q][1] = int(v * p )
                else:
                    W[q][2] = int(v)
                    V[q][2] = int(v * p )
        W_lst = []
        V_lst = []
        for key in W.keys():
            if key in main_key:
                W_lst.append(W[key])
                V_lst.append(V[key])
        m = len(W_lst)
        # 构造二维数
        dp = [[0] * (total + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            w1 = W_lst[i - 1][0]
            w2 = W_lst[i - 1][1]
            w3 = W_lst[i - 1][2]
            v1 = V_lst[i - 1][0]
            v2 = V_lst[i - 1][1]
            v3 = V_lst[i - 1][2]
            for j in range(total + 1):
                # dp[i][j]表示在 [ 前i ] 个物品里面 [ 预算值（背包）容量允许为j ] 的情况下可以获得的最大的价值加权和
                # 1. 不放入:
                dp[i][j] = dp[i - 1][j]
                # 2. 放入一个主件，比较上一个主件和放入这一个主件后哪个大
                if j - w1 >= 0:
                    dp[i][j] = max(dp[i][j], dp[i - 1][j - w1] + v1)
                # 3. 1个主件+附件1
                if j - w1 - w2 >= 0:
                    dp[i][j] = max(dp[i][j], dp[i - 1][j - w2 - w1] + v1 + v2)
                # 4. 一个主件+附件2
                if j - w1 - w3 >= 0:
                    dp[i][j] = max(dp[i][j], dp[i - 1][j - w3 - w1] + v1 + v3)
                # 5. 一个主见+附件1+附件2
                if j - w1 - w2 - w3 >= 0:
                    dp[i][j] = max(dp[i][j], dp[i - 1][j - w3 - w2 - w1] + v1 + v2 + v3)
        print(int(dp[m][total] * 10))
    except:
        break
