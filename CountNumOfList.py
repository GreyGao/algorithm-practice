def countNumOfList(arr):
  i = 0
  return count(arr, i)

def count(arr,i):
  if(i == len(arr)):
    return 0
  else:
    return count(arr, i + 1) + 1

print countNumOfList([1,2,3,4,5])