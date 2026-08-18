class Solution:
    def minReorder(self, n, connections):
        graph = [[] for _ in range(n)]

        for a, b in connections:
            graph[a].append((b, 1))
            graph[b].append((a, 0))

        visited = set()
        changes = 0
        stack = [0]

        while stack:
            city = stack.pop()
            visited.add(city)

            for neighbor, cost in graph[city]:
                if neighbor not in visited:
                    changes += cost
                    stack.append(neighbor)

        return changes