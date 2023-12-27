class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort(key=len)                  # 리스트를 길이를 오름차순으로 정리
        prefix = ""

        for i in range(len(strs[0])):       # 오름차순으로 정리한 리스트의 첫번째(가장짧은거) 문자의 길이만큼 반복
            same = strs[0][i]               
            for j in range(len(strs)):      
                if(strs[j][i] != same):     # same과 리스트의 j번째 문자가 다를때 발동
                    return prefix
            prefix += same                  # 빈칸에 같은 부분을 삽입

        return prefix