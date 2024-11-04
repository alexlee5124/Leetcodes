class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        sentence = list()
        i = 0
        while i < len(s):
            while i < len(s) and s[i] == " ":
                i += 1
            if i >= len(s):
                break
            word = list()
            while i < len(s) and s[i] != " ":
                word.append(s[i])
                i += 1
            sentence.insert(0, "".join(word))
            sentence.insert(0, " ")

        sentence = sentence[1:]
        return "".join(sentence)
