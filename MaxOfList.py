def maxOfList(arr):
  i = 0
  return findMax(arr[0], i, arr)

def findMax(bigger,i, arr):
  if i == len(arr):
    return bigger
  else:
    return findMax(max(bigger, arr[i]), i + 1, arr)

print maxOfList([12,9,3,1,4])