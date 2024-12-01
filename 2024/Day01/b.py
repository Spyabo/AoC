with open('./2024/Day01/testinput.txt', 'r') as f:
    lines: str = f.read().splitlines()

from collections import Counter

nums1 = []
nums2 = []

for line in lines:
    num1, num2 = line.split('  ')
    nums1.append(int(num1))
    nums2.append(int(num2))
    
sim = Counter(nums2)
res = []

for i in range(len(nums1)):
    if nums1[i] in sim:
        res.append(nums1[i] * sim[nums1[i]])
        
print(sum(res))