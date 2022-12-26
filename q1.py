# Find the mean, median, and mode in an array
# arr=[1, 2, 3, 4, 5, 6]
# count=0
# sum=0
# for i in arr:
#     count+=1
#     sum+=i
# print("mean of array is",sum/count)


# 1
# Reverse an array
# arr=[1,2,3,4,5,6,7,8,9]
# a=[]
# for i in (arr):
#     a=[i]+a
# print(a)


# 2
# Find the mean, median, and mode in an array
# arr=[2,3,4,5,6,7,9,9,4,9]
# count=0
# sum=0
# for i in arr:
#     count+=1
#     sum+=i
#     mean=(sum/count)
# print("mean is",mean)
# c1=0
# for i in arr:
#     c1+=1
#     m=c1//2
#     n=c1//2-1
# if c1%2!=0:
#     print(m)
# elif c1%2==0:
#     median=((arr[m]/2)+((arr[n]/2)+1))/2
# print("median is",median)
# mode=[]
# for i in arr:
#     c=0
#     for j in arr:
#         if i==j:
#             c+=1
#     if c>1:
#         if i not in mode:
#             mode=mode+[i]
# print("mode is",mode)


# 4
#  Find duplicate elements in an array.
# arr=[1,1,2,2,3,3,4,4,4,4,5,6,6,7,7]
# b=[]
# for i in arr:
#     c=0
#     for j in arr:
#         if i==j:
#             c+=1
#     if c>1:
#         if i not in b:
#             b=b+[i]
# print(b)


# 5
# Merge two sorted arrays into a single sorted array
# arr1=[1,2,3,4,5,6]
# arr2=[1,2,3,4,5,6]
# total=arr1+arr2
# c=0
# for i in total:
#     d=0
#     for j in total:
#         if total[c]<=total[d]:
#             total[c],total[d]=total[d],total[c]
#         d+=1
#     c+=1
# print(total)



# 8
# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the
# median of the two sorted arrays.
# num1=[1,2,3,4,5,6,7]
# num2=[8,9,10,11,12,13,14,3]
# c=0
# c1=0
# for i in num1:
#     c+=1
#     a=c//2
# for j in num2:
#     c1+=1
#     b=c1//2
# print(num1[a])
# print(num2[b])


# 10.
# Learn these sorting algorithms and apply them to an unsorted array:

# a. Selection Sort
# a=[3,4,2,5,7,6]
# c=0
# for i in a:
#     c+=1
# print(c)
# for i in range(c):
#     min=i
#     for j in range(i+1,c):
#         if a[min]>a[j]:
#             min=j
#     a[min],a[i]=a[i],a[min]
# print(a)        



# b. Insertion Sort
# arr=[8,4,5,2,1,9,3,2,7,6]
# c=0
# for i in arr:
#     c+=1
# print(c)
# for i in range(c):
#     j=i
#     while arr[j-1]>arr[j] and j>0:
#         arr[j-1],arr[j]=arr[j],arr[j-1]
#         j-=1
# print(arr)





# c. Bubble Sort
# arr=[5,3,9,6,7,2,8,1]
# c=0
# for i in arr:
#     c+=1
# print(c)
# for i in range(c):
#     for j in range(c-1):
#         if arr[j]>arr[j+1]:
#             arr[j],arr[j+1]=arr[j+1],arr[j]
# print(arr)




# e. Merge Sort
# def mergeSort(array):
#     c=0
#     for i in array:
#         c+=1
#     if c>1:
#         midle=c//2
#         left=array[:midle]
#         cl=0
#         for i in left:
#             cl+=1
#         right=array[midle:]
#         cr=0
#         for i in right:
#             cr+=1
#         mergeSort(left)
#         mergeSort(right)
#         left_index=0
#         right_index=0
#         position=0
#         while left_index<cl and right_index<cr:
#             if left[left_index]<right[right_index]:
#                 array[position]=left[left_index]
#                 left_index+=1
#             else:
#                 array[position]=right[right_index]
#                 right_index+=1
#             position+=1
#         while left_index<cl:
#             array[position]=left[left_index]
#             position+=1
#             left_index+=1
#         while right_index<cr:
#             array[position]=right[right_index]
#             position+=1
#             right_index+=1
# array=[31,5,6,4,1,3,9,11,2,7]
# mergeSort(array)
# print(array)



# 9. Find a number using Binary Search in a sorted array
# array=[1,2,3,4,5,6,7,8,9,10,11,12,13]
# c=0
# for i in array:
#     c+=1
# def binary(array,start,end,num):
#     if start<=end:
#         mid=start+(end-start)//2 
#         if array[mid]==num:
#             return mid
#         elif array[mid]>num:
#             return binary(array,start,mid-1,num)
#         elif array[mid]<num:
#             return binary(array,mid+1,end,num)
#     else:
#         print('this number is not present in list')
# num=14
# print(binary(array,0,c,num))







    
    



# string=input("Enter string:")
# vowels=0
# for i in string:
#       if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
#             vowels=vowels+1
# print("Number of vowels are:")
# print(vowels)



# a=[1,2,3,4,5,6,7,8,9,10]
# b=[]
# c=[]
# for i in range(len(a)):
#     if a[i]%2==0:
#         b.append(a[i])
#     else:
#         c.append(a[i])
# print(b)
# print(c)
        
        


