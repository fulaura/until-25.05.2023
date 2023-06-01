
#bubblesort is comparison based sorting
'''def bubblesort(list):
    for i in range(0,len(list)-1):
        for j in range(i+1,len(list)):
            if list[i]>list[j]:
                temp=list[i]
                list[i]=list[j]
                list[j]=temp
                
list= [12,45,11,1,25,65,41,25,13,4564,41]
bubblesort(list)
print("sorted",list)'''

#Merge sort divides the array into equal halves and combines in sorted manner
def merge_sort(unsorted_list):
    if len(unsorted_list)<=1:
        return unsorted_list
    #Find the middle point
    middle= len(unsorted_list)//2
    left_list=unsorted_list[:middle]
    right_list=unsorted_list[middle:]
    
    left_list=merge_sort(left_list)
    right_list=merge_sort(right_list)
    return list(merge(left_list,right_list))
#merge the sorted halves

def merge(left_half,right_half):
    
    res=[]
    while len(left_half)!=0 and len (right_half)!=0:
        if left_half[0]<right_half[0]:
            res.append(left_half[0])
            left_half.remove(left_half[0])
        else:
            res.append(right_half[0])
            right_half.remove(right_half[0])
    if len(left_half)==0:
        res=res+right_half
    else:
        res=res+left_half
    return res

unsorted_list=[12,54,123,4548,414,512,369,141,0,1,4]
print(merge_sort(unsorted_list))