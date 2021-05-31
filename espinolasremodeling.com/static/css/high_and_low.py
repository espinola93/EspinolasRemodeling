number= "1 2 3 4 5"

num=[int(x) for x in number.split()]

max_number=max(num)
min_number=min(num)

array_result=[]
array_result.append(max_number)

array_result.append(min_number)

s=[str(i) for i in array_result]

numbers=' '.join(s)

return numbers

