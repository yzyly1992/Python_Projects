#coding =utf-8  
import urllib.request  
import re  
  
def getHtml(url):  
    page = urllib.request.urlopen(url)  ##打开页面  
    html = page.read() ##获取目标页面的源码  
    return html  
  
def getImg(html):  
    reg = 'src="(.+?\.png)"'  ##正则表达式筛选目标图片格式，有些是'data-original="(.+?\.jpg)"'  
    img = re.compile(reg)  
    html = html.decode('utf-8')  ##编码方式为utf-8  
    imglist = re.findall(img, html) ##解析页面源码获取图片列表  
    #print(imglist)  
    x = 0  
    #length = len(imglist)  
    for i in range(6):  ##取前6张图片保存  
        imgurl = imglist[i]  
        #imgurl = re.sub('"(.*?)"',r'\1',imgurl) #取单引号里的双引号内容  
        #print(imgurl)  
        urllib.request.urlretrieve(imgurl,'%s.jpg' % x) ##将图片从远程下载到本地并保存  
        x += 1  
  
global Max_Num  
Max_Num = 1  
##有时候无法打开目标网页，需要尝试多次，这里设置为1次  
for i in range(Max_Num):  
    try:  
        html = getHtml("http://www.sina.com")  
        getImg(html)  
        break  
    except:  
        if i < Max_Num - 1:  
            continue  
        else:  
            print ('URLError: <urlopen error timed out> All times is failed ')  
