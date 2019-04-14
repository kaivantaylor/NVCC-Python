a=2
num=4

while num > a :
  if num%a==0 & a!=num:
    print('not prime')
    break
  a += 1
else: # loop not exited via break
  print('prime')
