class Solution:
    def reverseVowels(self, s: str) -> str:
        start = 0
        end = len(s) - 1

        vowels = "AaEeIiOoUu"
        word = list(s)

        while start < end:
            while (start < end) and (word[start] not in vowels):
                start += 1
            while (start < end) and (word[end] not in vowels):
                end -= 1
            
            if start < end:
                temp = word[start]
                word[start] = word[end]
                word[end] = temp
            start += 1
            end -= 1
        return "".join(word)    
