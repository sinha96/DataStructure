from datetime import datetime as dt


# O(log(n))
def binary_search(arr, ele, low, high):
	if arr is None:
		return -1
	elif len(arr) == 1 and arr[0] != ele:
		return -1
	elif len(arr) == 1 and arr[0] == ele:
		return 0
	elif low > high:
		return -1

	mid = (low + high) // 2
	# print(f'low: ({low}, {arr[low]}), mid: ({mid}, {arr[mid]}), high: ({high}, {arr[high]})')
	if arr[mid] == ele:
		return mid
	elif arr[mid] > ele:
		return binary_search(arr, ele, low, mid-1)
	elif arr[mid] < ele:
		return binary_search(arr, ele, mid+1, high)


if __name__ == '__main__':
	a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
	st = dt.now()
	print(binary_search(arr=a, ele=21, low=0, high=len(a)-1))
	print(dt.now() - st, 's')
