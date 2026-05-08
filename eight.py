# Q1. User will input (2numbers).Write a program to swap the numbers
def swap(a, b):
    return b, a

x = int(input("enter first number:"))
y = int(input("enter second number:"))

x, y = swap(x, y)

print("after swapping: ")
print("first number: ",x)
print("second number:",y)

# Q2. write a program to palindrome or not?

def is_palindrome(num):
    if num < 0:
        return False

    original = num
    rev = 0

    while num > 0:
        rem = num % 10
        rev = (rev * 10) + rem
        num = num // 10

    return original == rev

a = int(input("Enter number: "))

if is_palindrome(a):
    print("Palindrome")
else:
    print("Not Palindrome")

# Q3. Write a program that will tell whether the given year is a leap year or not.

def is_leap_year(num):
    if(num % 4 == 0):
        return True
    else:
        False

print(is_leap_year(2024))

# Q4. write a program in two sum?

def two_sum(nums, target):
    new_map = {} 

    for i in range(len(nums)):
        a = target - nums[i]

        if a in new_map:
            return [new_map[a], i]

        new_map[nums[i]] = i

    return []

nums = [2, 7, 11, 15]
target = 9

print(two_sum(nums, target))

# Q5. You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their
    #  nodes contains a single digit. Add the two numbers and return the sum as a linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def build_list():
    values = list(map(int, input("Enter digits: ").split()))
    
    head = None
    current = None
    
    for v in values:
        node = ListNode(v)
        if head is None:
            head = node
            current = head
        else:
            current.next = node
            current = node
    
    return head

def addTwoNumbers(l1, l2):
    dummy = ListNode(0)
    current = dummy
    carry = 0

    while l1 or l2 or carry:
        v1 = l1.val if l1 else 0
        v2 = l2.val if l2 else 0

        total = v1 + v2 + carry
        carry = total // 10

        current.next = ListNode(total % 10)
        current = current.next

        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next

    return dummy.next

def print_list(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")

print("Enter first number:")
l1 = build_list()

print("Enter second number:")
l2 = build_list()

result = addTwoNumbers(l1, l2)

print("Result linked list:")
print_list(result)

# Q6. Given a string s, find the length of the longest substring without duplicate characters.

def longest_substring(s):
    char_set = set()
    left = 0
    max_length = 0

    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1

        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)

    return max_length

s = input("Enter string: ")
print("Length of longest substring:", longest_substring(s))

# Q7. Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays?

def SortedArrays(nums1, nums2):
    nums = nums1 + nums2
    nums.sort()

    n = len(nums)

    if n % 2 == 1:
        return nums[n // 2]
    else:
        return (nums[n // 2 - 1] + nums[n // 2]) / 2

print(SortedArrays([1,3], [2]))

# Q8. The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows 

def convert(s, numRows):
    if numRows == 1 or numRows >= len(s):
        return s

    rows = [""] * numRows
    current_row = 0
    going_down = False

    for char in s:
        rows[current_row] += char

        if current_row == 0 or current_row == numRows - 1:
            going_down = not going_down

        current_row += 1 if going_down else -1

    return "".join(rows)

s = "PAYPALISHIRING"
numRows = 3

print(convert(s, numRows))

# Q9. reverse integer?

def reverse(n):
    sign = -1 if n < 0 else 1
    n = abs(n)

    rev = 0

    while n > 0 :
        rem = n % 10 
        rev = (rev * 10) + rem
        n = n // 10

    return sign*rev

print(reverse(123))

# Q10. integer to roman

def int_to_roman(num):
    values = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4, 1
    ]

    symbols = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV", "I"
    ]

    result = ""

    for i in range(len(values)):

        while num >= values[i]:
            result += symbols[i]
            num -= values[i]

    return result


print(int_to_roman(14))
print(int_to_roman(20))  

# Q11. Write a function to find the longest common prefix string amongst an array of strings.

    # If there is no common prefix, return an empty string "".

def longest_common_prefix(strs):
    prefix = ""

    for char in zip(*strs):
        if len(set(char)) == 1:
            prefix += char[0]

        else:
            break

    return prefix

print(longest_common_prefix(["flower","flow","flight"]))

# Q12. three sum

def threeSum(nums):
    nums.sort()
    result = []

    for i in range(len(nums)):

        # duplicate avoid karne ke liye
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left = i + 1
        right = len(nums) - 1

        while left < right:

            total = nums[i] + nums[left] + nums[right]

            if total == 0:
                result.append([nums[i], nums[left], nums[right]])

                # duplicates skip karo
                while left < right and nums[left] == nums[left + 1]:
                    left += 1

                while left < right and nums[right] == nums[right - 1]:
                    right -= 1

                left += 1
                right -= 1

            elif total < 0:
                left += 1

            else:
                right -= 1

    return result


print(threeSum([-1,0,1,2,-1,-4]))

# Q13. Given an integer array nums of length n and an integer target, find three integers at distinct indices in nums such that the sum is closest to 
    # target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

def threeSumClosest(nums, target):
    nums.sort()
    closest = float('inf')
    
    for i in range(len(nums) - 2):
        left, right = i + 1, len(nums) - 1
        
        while left < right:
            sum = nums[i] + nums[left] + nums[right]
            
            if abs(sum - target) < abs(closest - target):
                closest =  sum
            
            if sum < target:
                left += 1
            elif sum > target:
                right -= 1
            else:
                return sum  
    
    return closest

print(threeSumClosest([-1, 2, 1, -4], 1))

# Q14. Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

    #0 <= a, b, c, d < n
    #a, b, c, and d are distinct.
    #nums[a] + nums[b] + nums[c] + nums[d] == target
    #You may return the answer in any order.

def fourSum(nums, target):
    nums.sort()
    result = []
    n = len(nums)

    for i in range(n - 3):

        if i > 0 and nums[i] == nums[i - 1]:
            continue

        for j in range(i + 1, n - 2):

            if j > i + 1 and nums[j] == nums[j - 1]:
                continue

            left = j + 1
            right = n - 1

            while left < right:

                total = nums[i] + nums[j] + nums[left] + nums[right]

                if total == target:

                    result.append([nums[i],nums[j],nums[left],nums[right]])

                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif total < target:
                    left += 1

                else:
                    right -= 1

    return result
print(fourSum([1, 0, -1, 0, -2, 2], 0))