from sys import stdin, stdout
from collections import defaultdict

input = stdin.read
data = input().splitlines()

n = int(data[0])  # Number of vertices (not directly used)
k = int(data[1])  # Number of operations

# Using defaultdict of sets to store adjacency lists
graph = defaultdict(set)
output = []

for line in data[2:]:
    op = line.split()
    if op[0] == "1":
        # Add an edge between vertices u and v
        u, v = int(op[1]), int(op[2])
        graph[u].add(v)
        graph[v].add(u)
    elif op[0] == "2":
        # Print the adjacent vertices of u
        u = int(op[1])
        if graph[u]:
            output.append(" ".join(map(str, graph[u])))
        else:
            output.append("")

# Output all results at once
stdout.write("\n".join(output) + "\n")
