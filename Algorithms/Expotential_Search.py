from datetime import datetime as dt


def binary_search(arr, ele, low, high):
	if low > high:
		return -1
	elif arr is None:
		return -1
	elif (len(arr) == 1 and arr[0] == ele) or (len(arr) == 1 and arr[0] != ele):
		return -1

	mid = (low + high)//2

	if arr[mid] == ele:
		return mid
	if arr[mid] < ele:
		return binary_search(arr=arr, ele=ele, low=mid+1, high=high)
	elif arr[mid] > ele:
		return binary_search(arr=arr, ele=ele, low=low, high=mid-1)


def exponential_search(arr, ele, n):
	if arr[0] == ele:
		return 0

	i = 1
	while i < n and arr[i] <= ele:
		i *= 2
	return binary_search(arr=arr, ele=ele, low=i//2, high=min(i, n-1))


if __name__ == '__main__':
	a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
	st = dt.now()
	print(exponential_search(arr=a, ele=9, n=len(a)))
	print(dt.now() - st, 's')
