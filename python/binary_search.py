# this function shoule return an index if found and -1 if not found
def Iter_binary_search(arr,element_to_find):
    start_index = 0
    end_index = len(arr)-1
    

    while start_index <= end_index:
        

        middle_index = (start_index+end_index)//2
     
        if element_to_find == arr[middle_index]:
            return middle_index
            
        elif element_to_find < arr[middle_index]:
            end_index = middle_index - 1

        elif element_to_find > arr[middle_index]:
            start_index = middle_index + 1
    return -1 
    pass

