a = [4,8,6,3,2]
i = 0
largest = a[0]

while i<len(a):
  if largest < a[i]:
    largest = a[i]
    largest_index = i
  i = i+1
print (largest_index)
sec_largest =  a[0]
i = 0


while i<len(a):
  if largest != a[i] and sec_largest < a[i]:
    sec_largest = a[i]
  i = i+1
diff = largest - sec_largest

print ( a[:largest_index] +[sec_largest,diff]+a[largest_index+1:])