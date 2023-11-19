import math
import re


def exgcd(a, b, x = 1, y = 0): 
    # 當b=0的時候return 
    if b == 0: return a, x, y 
    # 獲取b, a%b時的gcd與通項解 
    gcd, x, y = exgcd(b, a%b, x, y) 
    # 代入，得到新的通項解 
    x, y = y, x - a//b*y 
    return gcd, x, y

dic = {'A':'00','B':'01','C':'02','D':'03','E':'04','F':'05','G':'06',
       'H':'07','I':'08','J':'09','K':'10','L':'11','M':'12','N':'13',
       'O':'14','P':'15','Q':'16','R':'17','S':'18','T':'19',
       'U':'20','V':'21','W':'22','X':'23','Y':'24','Z':'25',' ':'26'}

print("輸入公鑰(e):")
e = int(input())

print("輸入(p):")
p = int(input())

print("輸入(q):")
q = int(input())

print('Plain text:')
text = input('')
textlist = []

for i in text:  
    textlist.append(dic[i])
textlist = "".join(textlist)

if len(textlist) % 4 == 2: 
    textlist+="26"    

textlist=re.findall(".{4}", textlist) 

for i in range(len(textlist)): 
    textlist[i] = str(pow(int(textlist[i]),e,p*q))

textlist = " ".join(textlist)

d = exgcd(e,((p - 1) * (q - 1)))[1] 
d = d % ((p - 1) * (q - 1))
print('C = ' ,textlist) 
print('\n') 
print('d = ',d) 
print('\n')

textlist = textlist.split()

for i in range(len(textlist)): 
    textlist[i] = str(pow(int(textlist[i]),d,p * q))

textlist = " ".join(textlist)
print('M = ',textlist)
print('\n')
print('After decoding:')
print(textlist)