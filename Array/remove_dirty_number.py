class Solution(object):
    def rangeSumBST(self, A):
        """
        :type A: List of integers  
        :rtype: do not return anything, modify A in place
        """
        #using two pointer, when encounter dirty numbers, move j to the next non dirty number and swap A[i] and A[j], after swap i+=1. 
        #This will eventually move all the dirty numbers to the end of the array, and then we only need to pop these dirty numbers out. 
        i,j=0,0
        N = len(A)
        need_to_swap = 0
        
        while j<N:
            if need_to_swap:
                A[i],A[j]=A[j],A[i]
                i+=1
            if is_dirty(A[j]):
                while is_dirty(A[j]):
                    j+=1
                need_to_swap=1
            else:
                i+=1
                j+=1
        while A and is_dirty(A[-1]):
            A.pop()
        
