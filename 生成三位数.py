#conding: utf-8-
#Author:'Jungang'
#Time:2019/4/26

#例子1 ：排列组合从四个数中抽取三个组成互不重复的数字

#程序分析：从百，十，个位，三个位置四个数字组合

for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if (i != k) and (i != j )and(j != k ):
                print(i,j,k)

