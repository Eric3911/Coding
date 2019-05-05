#conding: utf-8-
#Author:'Jungang'
#Time:2019/4/26

import datetime

if __name__ == '__main__':

#输出今日日期格式为dd/mm/yyyy。更多选项可以查看strftime()
print(datetime.date.today().strftime('%d/%m/%Y'))

#创建日期对象
miyazakiBirthDate = datetime.date(1941,1,5)

print(miyazakiBirthDate.strftime('%d/%m/%Y'))

