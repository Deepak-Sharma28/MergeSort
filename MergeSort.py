def mergesort(arr):
    if len(arr)>1:
        #getting the middle position of the list

        mid = len(arr)//2

        #dividing list into two parts from middle

        lefthalf = arr[:mid]
        righthalf = arr[mid:]

        #calling recursion
        #here we have two parameters one lefthalf and second is righthalf

        mergesort(lefthalf)
        mergesort(righthalf)

        #below the whole program is for comparing and swapping in between lists

        i=j=k=0

        while i<len(lefthalf) and j<len(righthalf):
            if lefthalf[i]<righthalf[j]:
                arr[k] = lefthalf[i]
                i+=1
            else:
                arr[k] = righthalf[j]    
                j+=1
            k+=1

        while i<len(lefthalf):
            arr[k] = lefthalf[i]
            i+=1
            k+=1
        while j<len(righthalf):
            arr[k] = righthalf[j]
            j+=1
            k+=1
    return arr 


#an empty list
arr = []

for elements in range(int(input())):
    arr+=[int(input())]
sorted_list = mergesort(arr)
print(*sorted_list)