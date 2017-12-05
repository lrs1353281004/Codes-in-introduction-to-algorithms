# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 09:06:32 2017
Merge sort
@author: Li Ruosong
"""
#input instance
array=[2,1,7,5,3,7,4,5,6,7,5]

#MERGE      we assume that A[p,...,q]  and A[q+1,...,r]  are already sorted in ascending order
def MERGE(A,p,q,r):
    n1=q-p+1
    n2=r-q
    L=[0]*(n1+1)
    R=[0]*(n2+1)
    for i in range(n1):
        L[i]=A[p+i]
    for j in range(n2):
        R[j]=A[q+1+j]
    L[n1]= + inf
    R[n2]= + inf
    i=0
    j=0
    for k in range(p,r+1):
        if L[i]<=R[j]:
            A[k]=L[i]
            i +=1
        else:
            A[k]=R[j]
            j +=1
    '''
    return A[p:r+1]
    '''
def MERGE_SORT(A,p,r):
    if r>p:
        q=int(floor((r+p)/2))
        MERGE_SORT(A,p,q)
        MERGE_SORT(A,q+1,r)
        MERGE(A,p,q,r)
    return A[p:r+1]
    
    
#output
array_sorted=MERGE_SORT(array.copy(),0,len(array)-1)
    
        
        
    
