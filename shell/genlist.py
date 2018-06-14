#-*- coding:utf-8 -*- 
import random
import itertools

# plan 0

def genList0 (x):
    dic = [str(i+1) for i in range(x)]
    res = list(set(['-'.join(sorted(random.sample(dic,2))) for i in range(x*2)]))
    return genList(x) if len(res) < x else res[0:x]

def randomList (x):
    return [i if random.randint(1,2) == 1 else '-'.join(i.split('-')[::-1]) for i in genList0(x)]

# plan 1
def genList(x):
    return [i if random.randint(1,2) == 1 else '-'.join(i.split('-')[::-1]) for i in [str(i[0]) + '-' + str(i[1]) for i in random.sample(list(itertools.combinations(list(range(1,x+1)),2)),x)]]


# plan 2
def genList2(x):
    dic = list(range(1,x+1))
    random.shuffle(dic)
    return [str(i[0]) + '-' + str(i[1]) for i in random.sample(list(itertools.combinations(dic,2)),x)]
# plan 3
def genRanList(min, max = None):
    if not str(min).isdigit():
        print('Error: The parameters must be positive integers')
        exit()
    if max == None:
        max = min
        min = 1
    elif not str(max).isdigit():
        print('Error: The parameters must be positive integers')
        exit()
    if max <= 2:
        print('Error: The parameters must be more than 2')
        exit()
    dic = list(range(min, max + 1))
    random.shuffle(dic)
    res = random.sample(list(itertools.combinations(dic,2)),max - min + 1) 
    return [str(i[0]) + '-' + str(i[1]) for i in res]
if __name__ == "__main__":
    #print(randomList(10))
    #print(genList(10))
    #print(genList2(3))
    print(genRanList(3,15))
#def randnum(min_num,max_num=None):
#    '随机生成不重复俩俩对应数组'
#    '|--生成一个指定范围的数列'
#    '|--打乱数组排序' 
#    '|--生成无序排列组合'   
#    
#    '|--format函数'
#    '|--格式化排列组合的中间值 可选填符号 '
#    '|--添加指定符号 ' 
#    '|--返回格式化后的数列 ' 
#    
#    '判断传进的是否一个参数  是的话  min_num = 1'
#    if max_num==None:
#        max_num=min_num
#        min_num = 1
#    
#    list1=list(range(min_num,max_num))
#    random.shuffle(list1)
#    result=random.sample(list(itertools.combinations(list1,2)),len(list1))
#    
#    print(result)
#    def format(fmt='-'):
#        '格式转换 默认是 ‘-’'
#        '可以自定义格式 闭包概念'
#        fmtre=[]
#        for x in result:
#            fmtre.append(str(x[0])+fmt+str(x[1]))
#        return fmtre
#    return format
#
#temp=randnum(11)
#print(temp())
#print(temp(' '))
