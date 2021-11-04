# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 16:49:14 2021

@author: Luis Daladier Guerre
"""

import numpy as np 

def counter(n_array:np.array, value:int, index: int, acc:int =0) -> int:
	"""
	@param n_array
	@param value
	@param index
	"""
	if index < n_array.size and n_array[index] == value:
		return counter(n_array, value, index + 1)
	else:
		return index
	
# test


#print(counter(np.array([0,0,0,0,0,1,1,1,1,1,0,0,0,0,0]),0, 0) )
#print(counter(np.array([0,0,0,0,0,1,1,1,1,1,0,0,0,0,0]),1, 5) )
#print(counter(np.array([0,0,0,0,0,1,1,1,1,1,0,0,0,0,0]),0, 10) )
#
def consecutives(n_array:np.array, value:int, index:int =0, acc:np.array =[]) -> np.array:
	"""
	"""
	if index > n_array.size:
		return np.array( acc )
	elif index < n_array.size and n_array[index] == value:
		qty = counter(n_array, value, index)
		acc.append([index,  qty - 1])
		return consecutives(n_array, value, index=qty, acc=acc)
	else:
		return consecutives(n_array, value, index + 1, acc)

## test
# print( consecutives( np.array([]), 0) ) 
# print( consecutives( np.array([0,0,0,0]), 0) ) 
# print( consecutives( np.array([1,1,0,0,0]), 0) ) 
# print( consecutives( np.array([0,0,1,0,0]),0) )
# print( consecutives( np.array([0,0,1,1,0,1,0,0,0]), 0 )) 

## exec
data_index = np.array([0,0,0,0,0,1,1,1,1,1,0,0,0,0,0])
#data_index = np.array([0,0,1,1,0,1,0,0,0])
# print(consecutives(data_index, 0))
# print(consecutives(data_index, 1))

data_index =np.concatenate(((
	np.zeros(np.random.randint(2,5)), 
	np.ones(np.random.randint(2,5)))*np.random.randint(1,50)
))
#print(data_index)
print(consecutives(data_index, 1))
