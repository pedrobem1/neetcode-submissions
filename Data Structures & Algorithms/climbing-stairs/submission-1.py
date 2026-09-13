class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}
        def dfs(passos_restantes,n_total,cache):

            if passos_restantes in cache:
                return cache[passos_restantes]

            if passos_restantes < 0:
                return 0
            
            if passos_restantes == 0:
                return 1

            um_passo = dfs(passos_restantes-1, n_total,cache)
            dois_passos = dfs(passos_restantes-2, n_total,cache)
            cache[passos_restantes] = um_passo + dois_passos

            return (cache[passos_restantes])

        return dfs(n,n,cache)