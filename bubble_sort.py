# need to sort number array in ascending order and descending order 
# hint: may need to loops to perform sort bubble
#Need to have index range and compare adjacent sides 
#Everything above is notes

numbers = [2,1,45,67,89,4,5,7,9]       

print(f'non-ordered numbers {numbers}')

def bubbleSort(numbers):
    for i in range(0,len(numbers)):
        for j in range(0, len(numbers)):
                if numbers[i] < numbers[j]:
                    temp= numbers[i]
                    numbers[i] = numbers[j]
                    numbers[j] = temp
    print (numbers)


bubbleSort(numbers)
     
    

            