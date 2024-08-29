n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    adjacency_list = []
    for j in range(n):
        if matrix[i][j] == 1:
            adjacency_list.append(j + 1)
    print(len(adjacency_list), *adjacency_list)
