
#tutorials

array = [5,3,1,2,6,8,4,9,7]

print(array[:6]) #print first 6 letters.
print(array[6:]) # print the letters after the 6th.

print(array[0])

left = [x for x in array[1:] if x <= array[0]]
print(left)

right = [x for x in array[1:] if x > array[0]]
print(right)