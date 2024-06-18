def merge_sort(arr):
    if len(arr) > 1:
        left_arr = arr[:len(arr)//2]
        right_arr = arr[len(arr)//2:] 

        merge_sort(right_arr)
        merge_sort(left_arr) 

        i = 0 # numero piu a sinistra del array di Sinistra
        j = 0 # numero piu a sinistra del array di Destra
        k = 0 # indice dell'array unito

        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1
        
        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1
        
        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1

arr_test = [5, 6, 1, 6, 8, 9, 5, 2, 1, 3, 1]    
merge_sort(arr_test)
print(arr_test)