#!/usr/bin/ python3
# -*- coding: utf-8 -*-
"""
    @Author: iamusera
    @date: 2023-08-02 15:42
    @description: 
"""
from copy import deepcopy

N, m = map(int, input().split(' '))
# 每件物品的价格（都是 10 元的整数倍），为了加快处理速度，先除以10
vpq_list = []

for i in range(m):
    v, p, q = map(int, input().split(' '))
    # v = v  # 每件物品的价格（都是 10 元的整数倍），为了加快处理速度，先除以10
    vpq_list.append([v, v * p, q])

main_dict = {}
for idx, i in enumerate(vpq_list):
    if i[2]:
        if main_dict.get(i[2]):
            main_dict[i[2]][3].append(i)
        else:
            m = vpq_list[i[2] - 1]
            m.append([])
            main_dict[i[2]] = m

print(1)
# # 主配件列表
# for idx, i in enumerate(vpq_list):
#     if i[2]:
#         main_dict[]
# 
# # [(20, 60, 5, []), (20, 60, 5, []), (10, 30, 0, []), (10, 20, 0, []), (10, 10, 0, [1, 2])]
# for i in range(m):
#     tmp_list = [0] * m
#     _vpq_list = deepcopy(vpq_list)
#     v, p, q, f = _vpq_list.pop(i)
#     tmp_list[i] = p * q
#     for idx, j in enumerate(_vpq_list):
#         ...
#     print(1)
