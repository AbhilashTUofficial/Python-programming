# Bubble sort

def sort(array):
    temp=0
    for i in range(len(array)):
        for j in range(len(array)):
            if array[i]<array[j]:
                temp=array[i]
                array[i]=array[j]
                array[j]=temp
def main():
    array = [1, 3, 5, 7, 2, 4, 6, 8]
    print("Unsorted array: " + str(array))
    sort(array)
    print("Sorted array: "+str(array))


main()
