import numpy as np
import copy
I = np.inf

T = np.array([[I, 8, 12, 11, I, I, I],
              [I, I, I, I, 3, 15, I],
              [I, I, I, I, 1, 13, I],
              [I, I, I, I, I, 10, I],
              [I, I, I, I, I, I, 15],
              [I, I, I, I, I, I, 13],
              [I, I, I, I, I, I, I]])
N = 3 + 6
result_table = []
table = []
table.append([0] * N)
table2 = []
while table:
    for i in range(len(table)):
        for j in range(len(T[table[i][0]])):
            if T[table[i][0]][j] < I:
                index = -1
                for k in range(len(table2)):
                    if table2[k][0] == j:
                        index = k
                if index == -1:
                    table2.append([I] * N)
                    index = len(table2) - 1
                    table2[index][0] = j
                table2[index][table[i][0] + 1] = T[table[i][0]][j] + table[i][-2]
    for i in range(len(table2)):
        table2[i][-2] = min(table2[i][1:-2])
        table2[i][-1] = table2[i].index(table2[i][-2]) - 1
    table = copy.copy(table2)
    result_table.append(table2)
    table2 = []

print("tables:")
for row in result_table:
    print(*row)

print("vertices:")
i = len(result_table) - 2
print(result_table[i][0][0])
tmp = result_table[i][0][-1]
while i >= 0:
    print(tmp)
    i -= 1
    for j in range(len(result_table[i])):
        if result_table[i][j][0] == tmp:
            tmp = result_table[i][j][-1]
