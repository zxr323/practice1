from bs4 import BeautifulSoup

html = '''
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
'''
soup = BeautifulSoup(html,'lxml')

#print(soup.prettify())    #标准格式 html
print(soup.a.attrs['class'])  #获取 a标签的class属性值
#soup.find/find_all 可以根据标签名，属性，内容查找文档
print(soup.find('a'))
print(soup.find(id='link3'))  #返回的是 目标属性所在标签的所有
print(soup.find_all(attrs={'class':"sister"})) #返回列表
print(soup.find(text='Elsie'))  # 返回 Elsie
print(soup.find('a').string) #获取第一个a标签的内容
