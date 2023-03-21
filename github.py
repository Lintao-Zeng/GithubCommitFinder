# python3
import urllib.request

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'}
page = 34

# 每页有35条数据，所以循环次数是commit总次数除以35取整，这里测试10次
for i in range(10):
    print('第' + str(i + 1) + '次开始：')
    with open("output.txt","wb") as f:
        url = 'https://github.com/termux/termux-packages/commits/master?after=6b95718c6054c611ed07bbb8139e0d6ce6e7d593+' + str(page) + '&branch=master'
        request = urllib.request.Request(url=url, headers=headers)
        html= urllib.request.urlopen(request)
        f.write(html.read())
    page = page + 35
    print('第' + str(i + 1) + '次结束：')
f.close()
print("Finished!")
