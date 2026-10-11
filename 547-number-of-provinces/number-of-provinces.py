class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)

        adjlist = [[] for _ in range(n)]

        for i in range(n):
            for j in range(n):
                if i != j and isConnected[i][j] == 1:
                    adjlist[i].append(j)

        
        visited = [False] * n
        provinces = 0

        def dfs(city):
            visited[city] = True

            for neighbor in adjlist[city]:
                if not visited[neighbor]:
                    dfs(neighbor)

        for i in range(n):
            if not visited[i]:
                provinces += 1
                dfs(i)
        
        return provinces



        