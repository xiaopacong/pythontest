# a=(1,2,3,4,4,5,66,3,3,3,4,3,2)
# # print(a[0][2])
# # print(a[2])
# # print(a[3][2])
# # print(a.index(5))
# # print(a.count(66))
# print(a[0,1])
a=[1,2,3,3,4,55,23]
# b=["haha","python",4,88]
# a.extend(b)
# print(a)
a.sort()
a.insert(2,55)
print(a)
# a.remove(55)
del(a[2])

print(a)
a.pop(1)
print(a)
print("-----------------------------")
a={
    "name":"刘德华",
    "age":65,
    "sex":"男",
    "love":["排球"],
    "habit":("java","python")
}
# print(a)
print(a.get("sex"))
print (list((a.keys())))
print(list((a.values())))
a.update(name="赵四")
print(a)
print("-----------------------")
a["name"]="蔡聪"
print(a)
a["name2"]="刘德华"


v=bool(-55)
print(v)