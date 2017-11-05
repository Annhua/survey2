
li=[2,5,9,6,3,1]
print(len(li))

#冒泡排序
# for i in range(len(li)): #[0,1,2,3,4,5,6,]
#     # print(li[i])[2,5,9,6,3,1]
#
#     for j in range(len(li)-i-1):#
#         # print(li[j])[2,5,9,6,3]
#         if li[j]>li[j+1]:
#             li[j],li[j+1]=li[j+1],li[j]
#
# print(li)

#选择排序

for  i in range(len(li)):
    # print(i)#[0,1,2,3,4,5]

    for j in range(len(li)-i):
        if li[i]>li[i+j]:
            li[i],li[i+j]=li[i+j],li[i]

print(li)

        # pass
        # print(j)[0,1,2,3,4,5][0,1,2,3,4]






