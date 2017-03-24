from bisect import bisect_left

def find_array_index(lst, start=0):
	if len(lst) == 0 or (len(lst) == 1 and lst[0] != start):
		return -1
	middle_index = len(lst) // 2
	middle_value = lst[middle_index]
	real_middle_index = middle_index + start
	if real_middle_index == middle_value:
		return real_middle_index
	elif real_middle_index < middle_value:
		return find_array_index(lst[:middle_index], start=start)
	else:
		return find_array_index(lst[middle_index:], start=middle_index)

def find_array_index2(lst):
	lst2 = [x-i for i,x in enumerate(lst)]
	index = bisect_left(lst2, 0)
	return -1 if index == len(lst2) or lst2[index] != 0 else index

def test(fn):
	# given test cases
	assert fn([-8,0,2,5]) == 2
	assert fn([-1,0,3,6]) == -1

	# custom test cases
	assert fn([]) == -1
	assert fn([0]) == 0
	assert fn([1]) == -1
	assert fn([0,1]) in [0,1]
	assert fn([-1,-2,3]) == -1
	assert fn([-1,-2,2]) == 2
	assert fn([0,1,2,3,4,5,6,7,8,9]) in [0,1,2,3,4,5,6,7,8,9] # multiple answers

test(find_array_index)
test(find_array_index2)