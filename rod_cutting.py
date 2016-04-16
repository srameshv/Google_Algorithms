
#recursion method
def rod_cutting(price,length):
  if length<=0:
    return length
  maxi=-1
  for i in range(length):
    maxi=max(maxi,price[i],length-i-1)
  return length
price=[12,4,5,78,1,15,10,2,1,36,45]
length=8
print(rod_cutting(price,length))
  
