import collections as coll

a = [1,1,1,1,1,2,2,2]

c = coll.Counter(a)

def jjj(nums,target):
     nums.append(target)
     a = sorted(nums).index(target)
     print(a)

a = [1,2,3,4,5]
print(a)
a.extend([1,2,3,4])
print(a)
b = [1,2]

a.extend(b[6:])
print(a)