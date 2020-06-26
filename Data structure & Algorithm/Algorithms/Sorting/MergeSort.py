# Merge Sort

def sort(array, firstIndex, lastIndex):
    if (firstIndex < lastIndex):
        middleIndex = (firstIndex + lastIndex) / 2
        sort(array, firstIndex, middleIndex)
        sort(array, middleIndex + 1, lastIndex)
        merge(array, firstIndex, middleIndex, lastIndex)


def merge(array, firstIndex, middleIndex, lastIndex):
    lils = middleIndex - firstIndex + 1
    lirs = lastIndex - middleIndex

    left = [lils]
    right = [lirs]

    for i in range(lils):
        left[i] = array[firstIndex + i]
    for j in range(lirs):
        right[i] = array[middleIndex + j + 1]
    i=0
    j=0
    k=0
    while(i< lils and j<lirs):
        if(left[i]<=right[j]):
            array[k]=left[i]
            i=i+1
        else:
            array[k]=right[j]
            j=j+1
        k=k+1
        while(i<lils):
            left[i]=array[i]
            i=i+1
            k=k+1
        while(j<lirs):
            right[j]=array[j]
            j=j+1
            k=k+1


def main():
    array = [1, 3, 5, 7, 2, 4, 6, 8]
    firstIndex = 0
    lastIndex = len(array) - 1
    print("Unsorted array: " + str(array))
    sort(array, firstIndex, lastIndex)
    print("Sorted array: " + str(array))

main()