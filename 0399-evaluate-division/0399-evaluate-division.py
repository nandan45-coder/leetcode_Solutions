class Solution:
    def calcEquation(self, equations, values, queries):
        graph = {}

        for i in range(len(equations)):
            a = equations[i][0]
            b = equations[i][1]
            value = values[i]

            if a not in graph:
                graph[a] = []
            if b not in graph:
                graph[b] = []

            graph[a].append((b, value))
            graph[b].append((a, 1.0 / value))

        def dfs(current, target, visited):
            if current == target:
                return 1.0

            visited.add(current)

            for neighbor, value in graph[current]:
                if neighbor not in visited:
                    result = dfs(neighbor, target, visited)

                    if result != -1.0:
                        return value * result

            return -1.0

        answer = []

        for a, b in queries:
            if a not in graph or b not in graph:
                answer.append(-1.0)
            else:
                answer.append(dfs(a, b, set()))

        return answer