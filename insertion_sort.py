#insertation_sort

#instance
A=[5,2,4,6,1,3]


def INSERTATION_SORT(array_list):
    for i in range(1,len(array_list)):
        key=array_list[i]
        j=i-1
        while j>=0 and array_list[j]>key:
            array_list[j+1]=array_list[j]
            j=j-1
        array_list[j+1]=key
    return array_list
  
#output
A_sorted=INSERTATION_SORT(A.copy())
