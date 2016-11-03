# -*- coding: UTF-8 -*-
# Navie crawler
import sys
import urllib
import urllib2
import cookielib
import string
import re
import time
import os
from bs4 import BeautifulSoup

import xlrd
import xlwt
from datetime import date,datetime

def read_excel():
    # 打开文件
    workbook = xlrd.open_workbook(r'goods.xls')
    # 获取所有sheet
    # print workbook.sheet_names() # [u'sheet1', u'sheet2']
    sheet2_name = workbook.sheet_names()[0]

    # 根据sheet索引或者名称获取sheet内容
    sheet2 = workbook.sheet_by_index(0) # sheet索引从0开始

    # sheet的名称，行数，列数
    # print sheet2.name,sheet2.nrows,sheet2.ncols

    # 获取整行和整列的值（数组）
    cols = sheet2.col_values(1) # 获取第三列内容
    cols = cols[2:]
    # for item in cols:
    # 	print item.encode('utf-8')

    
    # 获取单元格内容
    # print sheet2.cell(23,1).value.encode('utf-8')
    # print sheet2.cell_value(23,1).encode('utf-8')
    # print sheet2.row(23)[1].value.encode('utf-8')
    return cols


def down_imgs(no, name):
	save_path = str(no) + '-' + name.encode('utf-8') + '/'
	transstring = urllib.quote(name.encode('utf-8'))
	url = 'https://list.tmall.com/search_product.htm?q=%s' % transstring
	# url = 'https://s.taobao.com/search?q=%E8%90%A5%E5%85%BB%E5%93%81'
	# url = 'https://s.m.taobao.com/h5?q=%E8%90%A5%E5%85%BB%E5%93%81&search=%E6%8F%90%E4%BA%A4%E6%9F%A5%E8%AF%A2'
	sf = open(save_path + 'url.txt', 'w')
	sf.write(url)
	sf.close()

	request = urllib2.Request(url)
	response = urllib2.urlopen(request)
	page = response.read()

	with open(save_path + 'page.html', 'w') as f:
		f.write(page)
		f.close()


	bsObj = BeautifulSoup(page, 'html.parser')


	titles = bsObj.find_all('p', {'class': 'productTitle'})
	for title in titles:
		print title.get_text()
		link = title.find('a').attrs['href']
		link = 'https:' + link
		print link
		detail = urllib2.urlopen(link).read()
		
		pat = re.compile(r'\"httpsDescUrl\":\"(.*?)\"')
		imgMainUrl = re.search(pat, detail).group(1)
		imgMainUrl = 'https:' + imgMainUrl
		imgListPage = urllib2.urlopen(imgMainUrl).read()
		pat = re.compile(r'src=\"(.*?)\"')
		imgLinks = re.findall(pat, imgListPage)
		cnt = 0
		for imgLink in imgLinks:
			if imgLink[0] == '/':
				imgLink = 'https:' + imgLink
			filename = 'pic' + str(cnt) + '.jpg'
			print imgLink
			try:

				content = urllib2.urlopen(imgLink).read()
			except Exception as e:
				print e
				continue
			f = open(save_path + filename, 'wb')
			f.write(content)
			f.close()
			cnt = cnt + 1
		break

def main():
	goods_names = read_excel()
	print len(goods_names)
	N = 40
	for i, name in enumerate(goods_names):
		if i == N:
			break
		
		print '-----' + str(i) + '-----'
		path_name = str(i) + '-' + name.encode('utf-8')
		if not os.path.exists(path_name):
			os.makedirs(path_name)
		down_imgs(i, name)

		# time.sleep(2)
main()



