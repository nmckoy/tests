s = "abcabcbb"
# s = "bbbbb"
# s = "pwwkew"
start_index = 0
current_index = 0
current_substring = ""
substrings = []

while start_index < len(s):
	remaining_string = s[start_index:]
	print(remaining_string, current_substring, substrings)
	if current_index >= len(remaining_string):
		break
	if remaining_string[current_index] not in current_substring:
		current_substring += remaining_string[current_index]
		current_index += 1
	else:
		substrings.append(current_substring)
		current_substring = ""
		start_index += 1
		current_index = 0

print(max(substrings, key=len))