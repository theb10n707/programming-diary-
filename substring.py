'''
Largest substring in string
'''

def largest_substring(s):
    '''
    Input: String
    Output: String
    
    Given "abcabcbb", the answer is "abc", which the length is 3.

    Given "bbbbb", the answer is "b", with the length of 1.

    Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
    '''
    substring = {}
    substring_holder = ''
    for character in s:
        previous_character = character
        if character not in substring_holder:
            substring_holder += character
            substring[substring_holder] = len(substring_holder)
        else:
            substring_holder = previous_character
    return max(substring, key = substring.get)

if __name__ == '__main__':
    s = 'abcdeabcdabcdefabc'
    print(largest_substring(s))





