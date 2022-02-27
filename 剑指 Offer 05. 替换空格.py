class Solution:
    def replaceSpace(self, s: str) -> str:
        s_lis = []
        for i in range(len(s)):
            if s[i] != ' ':
                s_lis.append(s[i])
            else:
                s_lis.append('%20')
        return ''.join(s_lis)
