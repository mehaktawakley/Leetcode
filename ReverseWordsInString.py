class Solution:
    def reverseWords(self, s):
        s = s.split()
        b = ""
        for i in s:
            b+= " " + (i[::-1])
        return (b[1:])
