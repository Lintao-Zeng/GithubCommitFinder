# python3
import urllib.request

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'}
page = 34

# 每页有35条数据，所以循环次数是commit总次数除以35取整,commit 5839次，除以35取整是167
for i in range(167):
    print('第' + str(i + 1) + '次开始：')
    with open("output.txt","wb") as f:
        url = 'https://github.com/coolsnowwolf/lede/commits/master?after=229ba8e4a3ace1ea298fdf493746d8994cf0c73a+' + str(page) + '&branch=master&qualified_name=refs%2Fheads%2Fmaster'
        request = urllib.request.Request(url=url, headers=headers)
        html= urllib.request.urlopen(request)
        f.write(html.read())
    page = page + 35
    print('第' + str(i + 1) + '次结束：')
f.close()
print("Finished!")
