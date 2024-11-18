#!/usr/bin/env python3
def swap(list, index1, index2):
	temp = list[index1]
	list[index1] = list[index2]
	list[index2] = temp

def bubble_sort(list):
	for x in range(0, len(list)):
		for y in range(0, len(list) - 1):
			if(list[x] > list[y]):
				swap(list, x, y)
	return list
