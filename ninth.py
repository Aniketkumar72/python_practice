# Q1. Given the head of a linked list, remove the nth node from the end of the list and return its head.

class listnode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

def removenth(head, n):
    dummy = listnode(0)
    dummy.next = head

    fast = slow = dummy

    for i in range(n + 1):
        fast = fast.next

    while fast:
        fast = fast.next
        slow = slow.next

    slow.next = slow.next.next

    return dummy.next

value = list(map(int,input("enter a list:").split()))

n = int(input("enter n: "))

head = None
current = None

for v in value:
    node = listnode(v)

    if head is None:
        head = node
        current = node

    else:
        current.next = node
        current = node

newhead = removenth(head, n)

while newhead:
    print(newhead.val, end="->")
    newhead = newhead.next

print("None")

# Q2. Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

def isvalid(s):
    stack = []

    pair = {
        ")":"(",
        "]":"[",
        "}":"{"
    }

    for ch in s:
        if ch in "([{":
            stack.append(ch)

        else:
            if not stack:
                return False
            
            if stack[-1] != pair[ch]:
                return False
            
            stack.pop()

    return len(stack) == 0

s = input("enter brackets:")
print(isvalid(s))

# Q3. You are given the heads of two sorted linked lists list1 and list2. Merge the two lists into one sorted list. The list should be made 
    # by splicing together the nodes of the first two lists.

class listnode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

def buildlist(values):
    head = None
    current = None

    for v in values:

        node = listnode(v)

        if head is None:
            head = node 
            current = node 

        else: 
            current.next = node
            current = current.next

    return head

def mergeList(list1, list2):
    dummy = listnode()
    current = dummy 

    while list1 and list2:
        if list1.val < list2.val:
            current.next = list1
            list1 = list1.next

        else:
            current.next = list2
            list2 = list2.next

        current = current.next

    if list1:
        current.next = list1

    if list2:
        current.next = list2

    return dummy.next

def printlist(head):
    while head:
        print(head.val, end="->")
        head = head.next

    print("None")

v1 = list(map(int,input("enter node:").split()))
v2 = list(map(int,input("enter node:").split()))

list1 = buildlist(v1)
list2 = buildlist(v2)

newhead = mergeList(list1,list2)
printlist(newhead)

# Q4. You are given an array of k linked-lists lists, each linked-list is sorted in ascending order. 
    # Merge all the linked-lists into one sorted linked-list and return it.

class listnode:
    def __init__(self, val = 0, next = None):
        self.val = val 
        self.next = next

def buildlist(values):
    head = None
    current = None

    for v in values:
        node = listnode(v)

        if head is None:
            head = node
            current = node
        
        else:
            current.next = node
            current = current.next
    
    return head

def mergeklist(lists):
    values = []

    for head in lists:

        while head:
            values.append(head.val)
            head = head.next
    values.sort()

    dummy = listnode()
    current = dummy

    for v in values:
        current.next = listnode(v)
        current = current.next

    return dummy.next

def print_list(head):
    while head:
        print(head.val, end="->")
        head = head.next

    print("None")

k = int(input("enter number of linked list:"))

lists = []

for i in range(k):
    values = list(map(int,input("enter node:").split()))

    head = buildlist(values)
    lists.append(head)

merged_head = mergeklist(lists)

print("\n merged list:")
print_list(merged_head)

# Q5. Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes.

class listnode:
    def __init__(self,val = 0, next = None):
        self.val = val 
        self.next = next

def buildlist(values):
    head = None
    current = None

    for v in values:
        node = listnode(v)

        if head is None:
            head = node
            current = node

        else:
            current.next = node
            current = current.next
    
    return head

def swap(head):
    dummy = listnode(0)
    dummy.next = head

    prev = dummy

    while prev.next and prev.next.next:
        first = prev.next
        second = prev.next.next

        first.next = second.next
        second.next = first
        prev.next = second

        prev = first

    return dummy.next

def print_list(head):
    while head:
        print(head.val,end="->")
        head = head.next

    print("None")

values = list(map(int,input("enter a list:").split()))

head = buildlist(values)
new_head = swap(head)

print("\n after swapping:")
print_list(new_head)

# Q6. Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.
    # k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then 
    # left-out nodes, in the end, should remain as it is.
    # You may not alter the values in the list's nodes, only nodes themselves may be changed.

class listnode:
    def __init__(self, val = 0, next = None):
        self.val = val 
        self.next = next

def buildlist(values):
    head = None
    current = None

    for v in values:
        node = listnode(v)

        if head is None:
            head = node
            current = node

        else:
            current.next = node
            current = current.next

    return head

def print_list(head):
    while head:
        print(head.val, end="->")
        head = head.next
    print("none")

def reversekgroup(head, k):
    dummy = listnode(0)
    dummy.next = head
    group_prev = dummy

    while True:
        kth = group_prev

        for _ in range(k):
            kth = kth.next

            if not kth:
                return dummy.next
            
        group_next = kth.next

        prev = group_next
        curr = group_prev.next

        while curr != group_next:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        temp = group_prev.next
        group_prev.next = kth
        group_prev = temp

values = list(map(int,input("enter list:").split()))
k = int(input("enter k:"))

head = buildlist(values)
print("\n original list:")
print_list(head)

new_head = reversekgroup(head, k)
print("\n revese in k group:")
print_list(new_head)

# Q7. Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once.
    #  The relative order of the elements should be kept the same.
    # Consider the number of unique elements in nums to be k​​​​​​​​​​​​​​. After removing duplicates, return the number of unique elements k.
    # The first k elements of nums should contain the unique numbers in sorted order. The remaining elements beyond index k - 1 can be ignored.

def removeduplicates(num):
    if not num:
        return 0
    
    i = 0

    for j in range(1, len(num)):
        if num[j] != num[i]:
            i += 1
            num[i] = num[j]

    return i + 1

num = list(map(int, input("enter sorted array:").split()))

k = removeduplicates(num)

print("\n number of unique elements:", k)
print("\n after removing duplicates:", num[:k])

# Q8. Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. 
    # Then return the number of elements in nums which are not equal to val.
    # Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:
    # Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of 
    # nums are not important as well as the size of nums.Return k.

def removeelements(num, val):
    k = 0

    for i in range(len(num)):
        if num[i] != val:
            num[k] = num[i]
            k += 1

    return k

num = list(map(int, input("enter array: ").split()))
val = int(input(" enter remove value:"))

k = removeelements(num, val)

print("\n number of remaining elements:",k)
print("\n updated array:", num[:k])

# Q9. Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.
    # The integer division should truncate toward zero, which means losing its fractional part. For example, 8.345 would be truncated to 8, and 
    # -2.7335 would be truncated to -2.
    # Return the quotient after dividing dividend by divisor.

def divide(dividend, divisor):

    if dividend == -22**31 and divisor == -1:
        return 22**31 - 1

    negative = (dividend < 0) != (divisor < 0)

    dividend = abs(dividend)
    divisor = abs(divisor)

    quotient = 0

    while dividend >= divisor:

        temp = divisor
        multiple = 1

        while dividend >= (temp << 1):
            temp <<= 1
            multiple <<= 1

        dividend -= temp
        quotient += multiple

    if negative:
        return -quotient

    return quotient


dividend = int(input("Enter dividend: "))
divisor = int(input("Enter divisor: "))

print("Quotient =", divide(dividend, divisor))

# Q10. A permutation of an array of integers is an arrangement of its members into a sequence or linear order.
    #Given an array of integers nums, find the next permutation of nums.

def nextPermutation(nums):

    n = len(nums)
    i = n - 2

    while i >= 0 and nums[i] >= nums[i + 1]:
        i -= 1

    if i >= 0:

        j = n - 1

        while nums[j] <= nums[i]:
            j -= 1

        nums[i], nums[j] = nums[j], nums[i]

    left = i + 1
    right = n - 1

    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1

    return nums


nums = [1,2,3]

print(nextPermutation(nums))