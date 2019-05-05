#conding: utf-8-
#Author:'Jungang'
#Time:2019/4/23

if __name__=='__main__':
    import string
    fp = open('test1.txt')
    a = fp.read()
    fp.close()

    fp = open('test2.txt')
    b = fp.read()
    fp.close()

    fp = open('test3.txt','w')
    c = list(a+b)
    c.sort()
    s = ''
    s = s.join(c)
    fp.write(s)
    fp.close()


