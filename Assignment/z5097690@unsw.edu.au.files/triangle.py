import sys


rows = []

filename = input('Which data file do you want to use? ')
try:
    with open(filename) as file:
        for L in file:
            rows.append([int(v) for v in L.split()])
except FileNotFoundError:
    print('Could not open a file named', filename)
    print('Giving up...')
    sys.exit()

N = len(rows) - 1
rows[N] = [(rows[N][i], [rows[N][i]], 1) for i in range(N + 1)]
for i in range(N - 1, -1, -1):
    for j in range(i + 1):
        if rows[i + 1][j][0] > rows[i + 1][j + 1][0]:
            rows[i][j] = (rows[i][j] + rows[i + 1][j][0],
                          [rows[i][j]] + rows[i + 1][j][1],
                          rows[i + 1][j][2])
        elif rows[i + 1][j][0] == rows[i + 1][j + 1][0]:
            rows[i][j] = (rows[i][j] + rows[i + 1][j][0],
                          [rows[i][j]] + rows[i + 1][j][1],
                          rows[i + 1][j][2] + rows[i + 1][j + 1][2])                                            
        else:
            rows[i][j] = (rows[i][j] + rows[i + 1][j + 1][0],
                          [rows[i][j]] + rows[i + 1][j + 1][1],
                          rows[i + 1][j + 1][2])
            
print(rows)
print('The largest sum is:', rows[0][0][0])
print('The number of paths yielding this sum is:', rows[0][0][2])
print('The leftmost path yielding this sum is:', rows[0][0][1])

