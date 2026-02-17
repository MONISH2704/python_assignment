def runner(array):
    array=list(array)
    array.sort(reverse=True)
    runner_up=0
    for i in range(len(array)-1):
        if array[i] != array[i+1]:
            runner_up=array[i+1]
            break
        else:
            continue
    return runner_up 