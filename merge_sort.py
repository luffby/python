def merge(A:list, B:list):

	C=[0]*(len(A+B))
	i = j = k = 0 
		
	while i < len(A) and j < len(B):
	
			if A[i] <= B[j]:
				C[k] = A[i]
				i += 1
			
			else:
	
				C[k] = B[j]  
				j += 1 
			
			k += 1		

	while i < len(A): 
		C[k] = A[i]
		i += 1
		k += 1    

	while j < len(B): 
		C[k] = B[j]
		j  += 1
		k += 1    

	return C

def merge_sort(A):

	if len(A) < 2:
		return A
	
	mid = len(A) // 2
	L = [A[i] for i in range(0,mid)]
	R = [A[i] for i in range(mid, len(A))]
 
	A =  merge(merge_sort(L), merge_sort(R))			
	
	return A



print(merge_sort([3,4,5,1,2,4]))


