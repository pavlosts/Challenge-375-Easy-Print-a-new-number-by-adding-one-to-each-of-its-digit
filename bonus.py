def incNum(num):
  if num != 0:
    result = incNum(num//10)
  else:
    return 0

  if(num%10 == 9):
    return result*100 + (num%10)+1
  else:
    return result*10 + (num%10)+1


number = int(input())

if number == 0:
  result = 1
else:
  result = incNum(number)

print(result)
