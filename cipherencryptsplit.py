#alphabet-number dictionary creation
dic = {}
c = 0
ch = "abcdefghijklmnopqrstuvwxyz"
for i in ch:
    dic[i] = c
    c += 1
print(dic)
#Reading plain text from user
lii = []
cha = input("Enter the string:")

#reading key from user
li1 = []
key = input("Enter the key:")
for i in key:
    for j in dic:
        if (i == j):
            li1.append(dic[j])
print(li1)
#plain text letters to matching numbers in dictionary
for w in cha.split(' '):
    if(len(w)>len(key)):

        for z in range(0, len(w), len(key)):

          print(w[z:z+len(key)])

          li = []
          for i in w[z:z+len(key)]:
              for j in dic:
                  if (i == j):
                      li.append(dic[j])
          print(li)
          lii.append(li)
    else:
     li = []
     for i in w:
         for j in dic:
             if (i == j):
                 li.append(dic[j])
     print(li)
     lii.append(li)
print(lii)
#conversion of plain text to cipher text
li2i = []
for a in lii:
    li2 = []
    for k in range(len(a)):
        if ((a[k] + li1[k]) < 26):
            li2.append(a[k] + li1[k])
        else:
            li2.append((a[k] + li1[k]) - 26)
    print(li2)
    li2i.append(li2)
print(li2i)
#display cipher text
cipp=''
for a in li2i:
    cip = ''
    for i in a:
        for j in dic:
            if (i == dic[j]):
                cip = cip + j
    print(cip, end=" ")
    cipp=cipp+" "+cip
print('\n'+'Cipher text is: '+cipp)
