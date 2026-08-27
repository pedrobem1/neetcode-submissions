class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # sliding window + dict da janela
        # quando o numero de letras de uma letra diferente do num de letras da letra com mais numeros for igual a k, temos a sequencia que e = right - left. Quando passar de k, andar left ate voltar para k
        # sempre pegar a letra com mais ocorrencias no dict como base
        ...

        frequencies = {}
        max_freq = 0
        left = 0
        max_lenght = 0

        for right,char in enumerate(s):
            if char in frequencies:
                frequencies[char] += 1
            else:
                frequencies[char] = 1 
            
            max_freq = max(max_freq,frequencies[char])

            while (right - left + 1) - max_freq > k:
                frequencies[s[left]] -= 1
                left += 1 

            current = right - left + 1
            max_lenght = max(current, max_lenght)

        return max_lenght

