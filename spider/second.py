#-*- coding = 'utf-8' -*-
import request
from bs4 import BeautifulSoup
from datetime import datetime

res = request.get('http://news.sina.com.cn/c/2016-11-16/doc-ifxxsmuu5832785.shtml')
res.encoding  = 'utf-8'
soup = BeautifulSoup(res.text,'html.parser')
timesource = soup.select('.time-source')[0].contents[0].strip()
# dt = datetime.strptime(timesource,u'%Y年%m月%d日%H:%M')
dt.strftime('%Y-%M-%d')
soup.select('.timesource span a')[0].text

soup.select('.article-editor')[0].text.lsstrip('责任编辑： ')