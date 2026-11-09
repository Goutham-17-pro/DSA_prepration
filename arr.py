
#Arrays largest number

# array = [10, 20, 40, 50,]

# largest = array[0]

# for i in array:
#     if i> largest:
#         largest = i

# print("Largest number is:",largest)

#Reveseing an Array

# arr = [50, 60, 70, 80, 90]

# reverse = arr[::-1]

# print("Reversed array is",reverse)

#find the maximum number in array

# arr = [10,50,20,40,30]
# maximum = arr[0]

# for i in arr:
#     if i> maximum:
#         maximum = i

# print("maximum number in array is:",maximum)


#find second largest number in array

arr = [10,50,20,40,30]
uniqe = sorted(set(arr))
if len(uniqe) >= 2:
    print("second largest :", uniqe[-2])
else:
    print("no second largest number")

