def  BinarySearch(item_list,item):
    first = 0
    last = len(item_list)-1
    found = False
    
    while(first<=last and not found):
        mid = (first+last)//2
        if item_list[mid] == item:
            found = True
            
        else:
            if item < item_list[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return found

print(BinarySearch([1,2,4,5,8,9,0,12,22,3],6))
print(BinarySearch([1,2,4,5,8,9,0,12,3,22],12))


