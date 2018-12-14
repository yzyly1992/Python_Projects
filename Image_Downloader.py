import requests
import re
from requests.exceptions import RequestException
import os
import time

def get_index_page(url):
	try:
		response = requests.get(url)
		if response.status_code == 200:
			return response.text
		return None
	except RequestException:
		print('请求索引页面出错！')
		return None

def parse_index_page(html):
	pattern = re.compile('<tr.*?href="(.*?)".*?title="(.*?)".*?</a>', re.S)
	items = re.findall(pattern, html)
	for item in items:
		yield item[0]


def parse_detail_page(qhtml):
	pattern = re.compile('image-float-center.*?src="(.*?)".*?</div>', re.S)
	items = re.findall(pattern, qhtml)
	for img in items:
		yield img

def download_img(link, name_index):
	html = requests.get(link)
	with open(str(name_index) + '.jpg', 'wb') as f:
		f.write(html.content)
		f.flush()
	f.close()
	print('第%d张图片下载完成' %(name_index + 1))
	time.sleep(1)



def main():
	url = 'https://www.douban.com/group/haixiuzu/'
	html = get_index_page(url)
	links_pool = []
	name_index = 0
	for items in parse_index_page(html):
		dhtml = get_index_page(items)
		for img in parse_detail_page(dhtml):
			links_pool.append(img)
	for item in links_pool:
		name_index += 1
		download_img(item, name_index)


if __name__ == '__main__':
	main()