# task 3.1

def binarySearchRecursive(sequance, x, left, right):
    if left > right:
        return False
    mid = (left+right)//2
    print('mid', sequance[mid])

    if x == sequance[mid]:
        return mid
    elif x < sequance[mid]:
        return binarySearchRecursive(sequance, x, left, mid - 1)
    elif x > sequance[mid]:
        return binarySearchRecursive(sequance, x, mid + 1, right)

if __name__ == "__main__":
    sample = [1, 2, 5, 6, 8, 10, 50, 70, 75, 77, 78, 79, 80, 81, 82, 85]
    x = 77
    print('Index of number', x,'is equal to', binarySearchRecursive(sample, x, 0, len(sample)-1))


# task 3.2

def binarySearchIterative(sequance, x):
    left = 0
    right = len(sequance)-1
    mid = 0

  while left <= right:
      mid = ((left + right) // 2)
      print('mid', sequence[mid])
      if x == sequence[mid]:
          return mid
      elif x < sequence[mid]:
          right = mid - 1

      elif x > sequence[mid]:
          left = mid + 1


if __name__ == "__main__":
    sample = [1, 2, 5, 6, 8, 10, 50, 70, 75, 77, 78, 79, 80, 81, 82, 85]
    x = 77
    print('Index of number', x,'is equal to', binarySearchRecursive(sample, x)