def sum(arr):
  # baseline
  if len(arr) == 0:
    return 0
  if len(arr) == 1:
    return arr[0]
  # recursively line
  curr = arr.pop()
  return curr + sum(arr)

print sum([4,3,2,5])