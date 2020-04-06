"""
Given an array of strings, group anagrams together.

Note:
All inputs will be in lowercase.
The order of your output does not matter.
"""

# Example 1
# Input: ["eat", "tea", "tan", "ate", "nat", "bat"]
# Output: [["ate","eat","tea"], ["nat","tan"], ["bat"]]

# storing single digit != 1
num_history = []

def groupAnagrams(strs):
	# input: strs->list
	# output: list
	hashtab = dict()
	for word in strs:
		sorted_word = ''.join(sorted(word))

		if sorted_word in hashtab:
			hashtab[sorted_word].append(word)

		else:
			hashtab[sorted_word] = [word]
	return [val for val in hashtab.values()]


if __name__ == "__main__":
	print 'Execute input strs=["eat", "tea", "tan", "ate", "nat", "bat"]:: ', groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
	