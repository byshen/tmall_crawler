# -*- coding: utf-8 -*-
import xlrd
import xlwt
from datetime import date,datetime
import urllib2
import urllib
import cookielib
import requests
import re

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

"""
for i in range(41, len(goods_name)):
		print i
		if i == 42:
			break
		print goods_name[i].encode('utf-8')

		url = "https://s.taobao.com/search?q=%s&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.50862.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20161102" % urllib.quote(goods_name[i].encode('utf-8')) 
		
		response = opener.open(url)
		cj.save()
		# for i in FileCookieJar:
		# 	print i.name, i.value
		# FileCookieJar.save()

		file = open(goods_name[i].encode('utf-8'), 'w')
		file.write(response.read())

		file.close()

"""
if __name__ == '__main__':
	s = requests.Session()
	r = s.get('https://detail.tmall.com/item.htm?spm=a220m.1000858.1000725.1.2OcNMA&id=19281471459&areaId=310100&user_id=1603022933&cat_id=2&is_b=1&rn=cefd0a8a59f08bc66320c4c5387ef453')
	page = r.text
	# print page
	# pattern = re.compile(r'\"detail_url[\"]*#detail\"')
	# res = pattern.findall(page)
	# print res[0]
	f = open('page.html', 'w')
	f.write(page.encode('utf-8'))
	f.close()

	"""
	goods_name = read_excel()

	s = requests.Session()
	s.cookies = cookielib.LWPCookieJar('mycookie.txt')
	s.cookies.load('mycookie.txt') # 从文件加载
	for i in s.cookies:
		print i.name, i.value
	# r = s.get("https://s.taobao.com/search?q=%s&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.50862.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20161102" % urllib.quote(goods_name[41].encode('utf-8')))
	r = s.get('https://item.taobao.com/item.htm?spm=a230r.1.14.1.VWmIlf&id=2387540147&ns=1&abbucket=20#detail')
	# s.cookies.save(ignore_expires=True, ignore_discard=True)  # 已保存到 mycookie.txt
	# s.cookies.clear()   # 清除
	# print r.text


	file = open('res.html', 'w+')
	file.write(r.text.encode('utf-8'))
	file.close()
	""" 




	