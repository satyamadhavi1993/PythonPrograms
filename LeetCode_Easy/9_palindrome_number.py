# Given an integer x, return true if x is a palindrome, and false otherwise.

class Solution {
    public boolean isPalindrome(int x) {
        if (x < 0) {
            return false;
        }
        int temp = x;
        int result = 0;

        while (temp > 0) {
            result = result * 10 + (temp % 10);
            temp = temp / 10;
        }
        return result == x;
    }
}

sol = Solution()
print(sol.is_palindrome(121))
print(sol.is_palindrome(-121))
print(sol.is_palindrome(10))
print(sol.is_palindrome(12121))
print(sol.is_palindrome(123321))
print(sol.is_palindrome(0))
