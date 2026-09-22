class Solution:
    def compress(self, chars: List[str]) -> int:
        write = 0 # Indice em que vamos escrever
        read = 0

        while read < len(chars):
            char_atual = chars[read]
            count = 0

            while read < len(chars) and char_atual == chars[read]:
                read += 1
                count += 1

            chars[write] = char_atual
            write += 1

            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1
        
        return write
