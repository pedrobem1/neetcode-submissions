class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap1 = {}
        for i in nums:
            if i in hashmap1:
                hashmap1[i] +=1
            else:
                hashmap1[i] = 1
        
        buckets = [[] for _ in range(len(nums) + 1)]
        for chave in hashmap1:
            frequencia = hashmap1[chave]
            buckets[frequencia].append(chave)

        answer = []
        for frequencia in range(len(buckets) - 1, 0, -1):
            for num in buckets[frequencia]:
                answer.append(num)

                if len(answer) == k:
                    return answer

        