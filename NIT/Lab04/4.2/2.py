import os
import requests
from bs4 import BeautifulSoup
base_url = 'http://www.pythontab.com/html/pythonjichu'
headersvalue = {
    'User-Agent':'Mozilla/5.0 (Windows NT 11.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
}
def get_onepage_url(url):
    url_list = []
    try:
        r= requests.get(url,headers=headersvalue)
    except:
        print('请求失败')
    else:
        soup = BeautifulSoup(r.text,'lxml')
        items = soup.select('#catlist li')
        for item in items:
            url1 = item.select('a')[0].attrs['href']
            url_list.append(url1)
        return url_list
def get_article(url):
    try:
        r = requests.get(url, headers=headersvalue)
    except:
        print('请求失败')
    else:
        soup = BeautifulSoup(r.text,'lxml')
        title = soup.select('#Article h1')[0].string
        content = soup.select('#Article .content')[0].text
        towrite(title,content)
def towrite(title,content):
    string = ['?','*',':','<','>','\\','/''|']
    for i in string:
        if i in title:
            title = title.replace(i,'#')
    try:
        with open(title+'.txt','w+',encoding='utf-8')as f:
            f.write(content.strip())
    except:
        print('写入文件失败：'+title)
    else:
        print('下载完成：'+title)
def main():
    path = os.getcwd()+'\\python基础教程'
    if not os.path.exists(path):
        os.mkdir(path)
    os.chdir(path)
    for i in range(1,31):
        if i>1:
            url = base_url+str(i)+'.html'
        else:
            url = base_url
        url_list = get_onepage_url(url)
        for url1 in url_list:
            get_article(url1)
main()
