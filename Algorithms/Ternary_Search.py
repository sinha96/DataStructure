from datetime import datetime as dt


# O(log3(n))
def ternary_search(arr, ele, low, high):
	if low > high:
		return -1
	elif len(arr) == 1 and arr[0] == ele:
		return 0
	elif len(arr) == 1 and arr[0] != ele:
		return -1
	elif arr is None:
		return -1

	mid1 = low + (high - low) // 3
	mid2 = high - (high - low) // 3

	print(f'low: ({low}, {arr[low]}), mid1: ({mid1}, {arr[mid1]}), mid2: ({mid2}, {arr[mid2]}), high: ({high}, {arr[high]})')

	if arr[mid1] == ele:
		return mid1

	if arr[mid2] == ele:
		return mid2

	if ele < arr[mid1]:
		return ternary_search(arr=arr, low=low, high=mid1-1, ele=ele)

	elif ele > arr[mid2]:
		return ternary_search(arr=arr, ele=ele, low=mid2+1, high=high)

	else:
		return ternary_search(arr=arr, ele=ele, low=mid1+1, high=mid2-1)


if __name__ == '__main__':
	a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
	st = dt.now()
	print(ternary_search(arr=a, ele=9, low=0, high=len(a)-1))
	print(dt.now() - st, 's')
