from datetime import datetime as dt
import math


# O(n^(1/2))
def jump_search(arr, ele, n):
	step = math.sqrt(n)

	while arr[int(min(step, n))] < ele:
		prev = step
		step += step
		if prev > n:
			return -1

	while arr[int(prev)] < ele:
		prev += 1
		if prev == min(step, n):
			return -1

	if arr[int(prev)] == ele:
		return int(prev)

	return -1


if __name__ == '__main__':
	a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
	st = dt.now()
	print(jump_search(arr=a, ele=9, n=len(a)))
	print(dt.now() - st, 's')
