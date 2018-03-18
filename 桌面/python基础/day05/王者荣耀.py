print('欢迎来到召唤师峡谷')
msg = '欢迎来到召唤师峡谷'
print(msg)
name = 'wangzherongyao'
print(name.title())
print(name.upper())
print(name.lower())
first_name = '郑'
last_name = '开州'
full_name = first_name+last_name
print(full_name)
print('尊敬的召唤师：'+full_name+',欢迎来到召唤师峡谷！')
print('欢迎来到召唤师峡谷！')
print('\t欢迎来到召唤师峡谷！')
print('\n欢迎来到召唤师峡谷！')
msgq= '努力有用的话还要天才干什么?'
print(msgq)
msgq = msgq.strip()
print(msgq)
num = 2
msga = ('尊敬的召唤师，您在这句对战中的中和评价位于第'+str(num)+'位!')
print(msga)
heroes = ['安琪拉','李白','杨戬','貂蝉','孙悟空']
print(heroes)
print(heroes[0])
print(heroes[1])
heroes[0] = '狄人杰'
print(heroes)
heroes.append('兰铃王')
print(heroes)
heroes.insert(0,'兰陵王')
print(heroes)
del heroes[0]
print(heroes)
tail = heroes.pop()
print(heroes)
print(tail)
heroes.remove('李白')
print(heroes)
heroes.sort()
print(heroes)
heroes.sort(reverse=True)
print(heroes)
print(sorted(heroes))
print(heroes)
heroes.reverse()
print(heroes)
print(len(heroes))
for a in heroes:
    print('你的队伍中有此英雄：'+a)
for a in heroes:
    print(a+'是一个十分优秀的英雄'+'\n')
for a in range(1,5):
    print(a)
numa = list(range(1,6))
print(numa)
pingfangji = []
for shuzi in range(1,11):
    pingfang = shuzi**2
    pingfangji.append(pingfang)
print(pingfangji)
