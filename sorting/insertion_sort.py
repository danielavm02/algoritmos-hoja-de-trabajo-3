def insertion_sort(arr):
  i=1
  while (i<len(arr)):
    j=i
    while (j>0 and arr[j-1]>arr[j]):
      arr[j], arr[j - 1] = arr[j - 1], arr[j]
      j=j-1
    i=i+1
  return arr