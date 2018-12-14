import requests
from urllib.parse import urlencode
from requests.exceptions import RequestException
import json
from bs4 import BeautifulSoup
import re


def get_page_index(offset, keyword):
	data = {
		'offset': offset,
		'format': 'json',
		'keyword': keyword,
		'autoload': 'true',
		'count': '20',
		'cur_tab': 1
	}
	url = 'https://www.toutiao.com/search_content/?' + urlencode(data)
	try:
		heads = {}
		heads['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0'
		response = requests.get(url, headers=heads)
		if response.status_code == 200:
			return response.text
		return None
	except RequestException:
		print('请求索引页出错')
		return None

def parse_page_index(html):
	data = json.loads(html)
	if data and 'data' in data.keys():
		for item in data.get('data'):
			yield item.get('article_url')

def get_page_detail(url):
	try:
		heads = {}
		heads['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0'
		response = requests.get(url, headers=heads)
		if response.status_code == 200:
			return response.text
		return None
	except RequestException:
		print('请求详情页出错', url)
		return None

def parse_page_detail(html):
	soup = BeautifulSoup(html, 'lxml')
	title = soup.select('title')[0].get_text()
	print(title)
	images_pattern = re.compile('gallery: JSON\.parse\("(.*?)"\),\n', re.S)
	result = re.search(images_pattern, html)
	if result:
		data = json.loads(result.group(1))
		print(data)
		# if data and 'sub_images' in data.keys():
		# 	sub_images = data.get('sub_images')
		# 	images = [item.get('url') for item in sub_images]
		# 	return {
		# 		'title': title,
		# 		'image': images,
		# 		'url': url
		# 	}


def main():
	html = get_page_index(1, '萝莉')
	for url in parse_page_index(html):
		html = get_page_detail(url)
		if html:
			result = parse_page_detail(html)
			print(result)

if __name__ == '__main__':
	main()
