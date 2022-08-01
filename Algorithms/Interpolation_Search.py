from datetime import datetime as dt


def interpolation_search(arr, ele, low, high):
	if arr is None:
		return -1
	elif len(arr) == 1 and arr[0] != ele:
		return -1
	elif len(arr) == 1 and arr[0] == ele:
		return 0
	elif low > high:
		return -1

	pos = low + (ele - arr[low]) * (high - low)//(arr[high] - arr[low])
	print(f'low: ({low}, {arr[low]}), pos: ({pos}, {arr[pos]}), high: ({high}, {arr[high]})')
	if arr[pos] == ele:
		return pos
	if arr[pos] > ele:
		return interpolation_search(arr=arr, ele=ele, low=low, high=pos-1)
	elif arr[pos] < ele:
		return interpolation_search(arr=arr, ele=ele, low=pos+1, high=high)


if __name__ == '__main__':
	a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
	st = dt.now()
	print(interpolation_search(arr=a, ele=9, low=0, high=len(a)-1))
	print(dt.now() - st, 's')
