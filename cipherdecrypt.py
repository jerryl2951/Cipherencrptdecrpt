#alphabet-number dictionary creation
dic = {}
c = 0
ch = "abcdefghijklmnopqrstuvwxyz"
for i in ch:
    dic[i] = c
    c += 1
print(dic)
#reading cipher text from user
lii = []
cha = input("Enter the string:")
for w in cha.split(' '):
    li = []
    for i in w:
        for j in dic:
            if (i == j):
                li.append(dic[j])
    print(li)
    lii.append(li)
print(lii)
#reading key from user
li1 = []
key = input("enter the key:")
for i in key:
    for j in dic:
        if (i == j):
            li1.append(dic[j])
print(li1)
#conversion of cipher text to plain text
li2i = []
for a in lii:
    li2 = []
    for k in range(len(a)):
        if ((a[k] - li1[k]) < 0):
            li2.append(26 + (a[k] - li1[k]))
        else:
            li2.append(a[k] - li1[k])
    print(li2)
    li2i.append(li2)
print(li2i)
#displaying plain text    
plain=''
for a in li2i:
    plai = ''
    for i in a:
        for j in dic:
            if (i == dic[j]):
                plai = plai + j
    print(plai, end=" ")
    plain=plain+" "+plai
print('\n'+'Plain text after decryption is :'+plain)

