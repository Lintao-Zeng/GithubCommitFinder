# _*_ coding:utf-8 _*_

# import urllib2 (python2用)

import urllib.request # python3用

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36'}
page = 34

# 每页有35条数据，所以循环次数是commit总次数除以35取整，这里测试1000次
for i in range(1000):
    print('第' + str(i + 1) + '次开始：')
    with open("output.txt","a") as f:
        f.write(urllib.request.urlopen(urllib.request.urlopen('https://github.com/termux/termux-packages/commits/master?after=6b95718c6054c611ed07bbb8139e0d6ce6e7d593+' + str(page) + '&branch=master',headers=headers)).read())
    page = page + 35
    print('第' + str(i + 1) + '次结束：')
print("Finished!")
