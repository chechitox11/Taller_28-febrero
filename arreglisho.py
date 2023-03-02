def funcion(arr):
    mini = arr[0]
    for x in range (1,len(arr)):
        if arr[x] < mini:
            mini = arr[x]
    return mini