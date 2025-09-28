class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        return len(set(sentence)) == 26
    
    def checkIfPangramUsingBooleanArray(self, sentence: str) -> bool:
        alphabet_array = [False] * 26
        for ch in sentence:
            alphabet_array[ord(ch) - ord('a')] = True
        return all(alphabet_array)
    
    
    
sol = Solution()
print(sol.checkIfPangram(sentence = "thequickbrownfoxjumpsoverthelazydog"))
print(sol.checkIfPangram(sentence = "leetcode"))
print(sol.checkIfPangramUsingBooleanArray(sentence = "thequickbrownfoxjumpsoverthelazydog"))
print(sol.checkIfPangramUsingBooleanArray(sentence = "leetcode"))