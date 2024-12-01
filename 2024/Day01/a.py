with open('./2024/Day01/input.txt', 'r') as f:
    lines: str = f.read().splitlines()

nums1 = []
nums2 = []

for line in lines:
    num1, num2 = line.split('  ')
    nums1.append(int(num1))
    nums2.append(int(num2))
    
nums1.sort()
nums2.sort()

pairs = []
for i in range(len(nums1)):
    pairs.append(abs(nums2[i] - nums1[i]))
    
print(sum(pairs))