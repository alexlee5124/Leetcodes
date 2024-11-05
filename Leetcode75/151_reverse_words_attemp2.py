class Solution:
    def reverseWords(self, s: str) -> str:
        s = s[::-1]
        answer = list()

        left,right,i = 0,0,0
        while i < len(s):
            while (i< len(s)) and (s[i] == " "):
                i += 1 
            if i >= len(s):
                break
            while (i< len(s)) and (s[i] != " "):
                answer.append("".join(s[i]))
                i += 1
                right += 1
            answer[left:right] = answer[left:right][::-1]
            answer.append(" ")
            right += 1
            left = right
        return "".join(answer[:right-1])
