# Insertion sort

def sort(array):
    length=len(array)
    for i in range(length):
        key=array[i]
        j=i-1

        while(j>=0 and key<array[j]):
            array[j+1]=array[j]
            j=j-1
        array[j+1]=key


def main():
    array=[1,3,5,7,2,4,6,8]
    print("Unsorted array: "+str(array))
    sort(array)
    print("Sorted array: "+str(array))

main()