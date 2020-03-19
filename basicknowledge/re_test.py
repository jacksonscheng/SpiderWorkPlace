# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 10:56:07 2020

@author: Administrator
"""


import re

content = "Hello 1234567 World This is a Regex Demo"
print(len(content))
result = re.match('^Hello\s\d\d\d\s\d{4}\s\w{10}', content)
print(result)
print(result.group())# 输出匹配到的内容
print(result.span())# 输出匹配的范围

result1 = re.match('^Hello\s\d+\s\d+\sWorld', content)
print(result1.group())


# .*
# .表示任意字符，*表示匹配前面的字符0次多次，因此和一起的意思
# 就是匹配任意字符0次或多次
result2 = re.match('^Hello.*Demo$', content)
print(result2.group())


#贪婪匹配，尽可能匹配多的字符，因此、|d+匹配出来是7
result3 = re.match('^Hel.*(\d+).*Demo$', content)
print(result3.group(1))


#非贪婪匹配尽量少的匹配
result4 = re.match('^He.*?(\d+).*Demo$', content)
print(result4.group(1))



content2 = "http://www.weibo.com/comment/kEraCN"
result31 = re.match('^http.*?comment/(.*?)', content2)
result32 = re.match('^http.*?comment/(.*)', content2)
print(result31.group(1)) #无匹配，因为？是尽量少匹配
print(result32.group(1)) #有匹配

# 修饰符

content = '''Hello 123456 World_This
is a Regex Demo
'''
#  加上re.S表示可以匹配换行符
result = re.match('^He.*?(\d+).*?Demo$', content, re.S)
print(result.group())



# =============================================================================
# search（）
# =============================================================================
content ="dfagrgr Hello 1234567 World This is a Regex Demo"
result22 = re.search('Hello.*?(\d+).*Demo$', content)
print(result22.group())



# =============================================================================
# 提取练习
# =============================================================================
html = '''<div id="songs-list">
    <h2 class="title">经典老歌</h2>
    <p class="introduction">
        经典老歌列表
    </p>
    <ul id="list" class="list-group">
        <li data-view="2">一路上有你</li>
        <li data-view="7">
            <a href="/2.mp3" singer="任贤齐">沧海一声笑</a>
        </li>
        <li data-view="4" class="active">
            <a href="/3.mp3" singer="齐秦">往事随风</a>
        </li>
        <li data-view="6"><a href="/4.mp3" singer="beyond">光辉岁月</a></li>
        <li data-view="5"><a href="/5.mp3" singer="陈慧琳">记事本</a></li>
        <li data-view="5">
            <a href="/6.mp3" singer="邓丽君"><i class="fa fa-user"></i>但愿人长久</a>
        </li>
    </ul>
</div>'''




result99 = re.search('<li data-view="4".*?singer="(.*?)">(.*?)</a>', html, re.S)

print(result99.group())

if result99:
    print(result99.group(1),result99.group(2))



# =============================================================================
# findall() 返回所有符合要求的结果
# =============================================================================

result = re.findall('<li.*?href="(.*?)".*?singer="(.*?)">(.*?)</a>',
                    html,
                    re.S)

if result:
    print(result)

for info in result:
    print(info[0], info[1], info[2])

# =============================================================================
# sub 去掉不需要的东西
# =============================================================================

content= "3r34hjoj5 345343oh3434  34egfe"

# 去掉字符串的数字,
result = re.sub("\d+|\s", '', content) #这里的\有转义的意思不然就被当做其他普通字符了

if result:
    print(result)



#      这里的<a.*?>|</a>不能留空格写成<a.*?> | </a>
html2 = re.sub('<a.*?>|</a>', '', html)#
print(html2)


results = re.findall('<li.*?>(.*?)</li>', html2, re.S)

if results: print(results)

for result in results:
    print(result.strip())





