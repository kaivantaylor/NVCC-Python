text = 'hello my name is hello my name is marty'

txtsplit = text.split()
#print(txtsplit)

txtdic = {}

for str in txtsplit:
    if str in txtdic:
        txtdic[str] = txtdic[str] + 1
    else:
        txtdic[str] = 1

list = []
for i in txtdic:
    list.append((txtdic[i],i))

list.sort()
list.reverse()
#print(list)

count = 0
final = []

while count < 3:
    a = list[count]
    final.append(a[1])
    count += 1

print(final)
