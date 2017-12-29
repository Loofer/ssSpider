# encoding:UTF-8
import uuid
import re
import urllib.request

from bs4 import BeautifulSoup
import StoreConfig
url = "https://global.ishadowx.net/"
data = urllib.request.urlopen(url).read()
html_doc = data.decode('UTF-8')
soup = BeautifulSoup(html_doc, 'html.parser')
containerDiv = soup.find('div', class_='portfolio-items')
hover_textList = containerDiv.find_all('div', class_='hover-text')

table1 = {}
table2 = {}
table3 = {}
table4 = {}
table5 = {}
table6 = {}
table7 = {}
table8 = {}
table9 = {}
table10 = {}
table11 = {}
table12 = {}
tables = [table1, table2, table3, table4, table5, table6, table7, table8, table9, table10, table11, table12]
for i in range(len(hover_textList)):
    ip = hover_textList[i].find('span', id='ipusa')
    port = hover_textList[i].find('span', id='portusa')
    password = hover_textList[i].find('span', id='pwusa')
    method = hover_textList[i].find('h4', text=re.compile(r'Method:'))
    if ip != None:
        table1['ip'] = ip.get_text()
    if port != None:
        table1['port'] = port.string.replace('\n', '')
    if password != None:
        table1['password'] = password.string.replace('\n', '')
    if method != None:
        table1['method'] = method.string.replace('Method:', '')
    ip = hover_textList[i].find('span', id='ipusb')
    port = hover_textList[i].find('span', id='portusb')
    password = hover_textList[i].find('span', id='pwusb')
    method = hover_textList[i].find('h4', text=re.compile(r'Method:'))
    if ip != None:
        table2['ip'] = ip.get_text()
    if port != None:
        table2['port'] = port.string.replace('\n', '')
    if password != None:
        table2['password'] = password.string.replace('\n', '')
    if method != None:
        table2['method'] = method.string.replace('Method:', '')

    ip = hover_textList[i].find('span', id='ipusc')
    port = hover_textList[i].find('span', id='portusc')
    password = hover_textList[i].find('span', id='pwusc')
    method = hover_textList[i].find('h4', text=re.compile(r'Method:'))
    if ip != None:
        table3['ip'] = ip.get_text()
    if port != None:
        table3['port'] = port.string.replace('\n', '')
    if password != None:
        table3['password'] = password.string.replace('\n', '')
    if method != None:
        table3['method'] = method.string.replace('Method:', '')

    ip = hover_textList[i].find('span', id='ipjpa')
    port = hover_textList[i].find('span', id='portjpa')
    password = hover_textList[i].find('span', id='pwjpa')
    method = hover_textList[i].find('h4', text=re.compile(r'Method:'))
    if ip != None:
        table4['ip'] = ip.get_text()
    if port != None:
        table4['port'] = port.string.replace('\n', '')
    if password != None:
        table4['password'] = password.string.replace('\n', '')
    if method != None:
        table4['method'] = method.string.replace('Method:', '')

    ip = hover_textList[i].find('span', id='ipjpb')
    port = hover_textList[i].find('span', id='portjpb')
    password = hover_textList[i].find('span', id='pwjpb')
    method = hover_textList[i].find('h4', text=re.compile(r'Method:'))
    if ip != None:
        table5['ip'] = ip.get_text()
    if port != None:
        table5['port'] = port.string.replace('\n', '')
    if password != None:
        table5['password'] = password.string.replace('\n', '')
    if method != None:
        table5['method'] = method.string.replace('Method:', '')

    ip = hover_textList[i].find('span', id='ipjpc')
    port = hover_textList[i].find('span', id='portjpc')
    password = hover_textList[i].find('span', id='pwjpc')
    method = hover_textList[i].find('h4', text=re.compile(r'Method:'))
    if ip != None:
        table6['ip'] = ip.get_text()
    if port != None:
        table6['port'] = port.string.replace('\n', '')
    if password != None:
        table6['password'] = password.string.replace('\n', '')
    if method != None:
        table6['method'] = method.string.replace('Method:', '')

    ip = hover_textList[i].find('span', id='ipsga')
    port = hover_textList[i].find('span', id='portsga')
    password = hover_textList[i].find('span', id='pwsga')
    method = hover_textList[i].find('h4', text=re.compile(r'Method:'))
    if ip != None:
        table7['ip'] = ip.get_text()
    if port != None:
        table7['port'] = port.string.replace('\n', '')
    if password != None:
        table7['password'] = password.string.replace('\n', '')
    if method != None:
        table7['method'] = method.string.replace('Method:', '')

    ip = hover_textList[i].find('span', id='ipsgb')
    port = hover_textList[i].find('span', id='portsgb')
    password = hover_textList[i].find('span', id='pwsgb')
    method = hover_textList[i].find('h4', text=re.compile(r'Method:'))
    if ip != None:
        table8['ip'] = ip.get_text()
    if port != None:
        table8['port'] = port.string.replace('\n', '')
    if password != None:
        table8['password'] = password.string.replace('\n', '')
    if method != None:
        table8['method'] = method.string.replace('Method:', '')

    ip = hover_textList[i].find('span', id='ipsgc')
    port = hover_textList[i].find('span', id='portsgc')
    password = hover_textList[i].find('span', id='pwsgc')
    method = hover_textList[i].find('h4', text=re.compile(r'Method:'))
    if ip != None:
        table9['ip'] = ip.get_text()
    if port != None:
        table9['port'] = port.string.replace('\n', '')
    if password != None:
        table9['password'] = password.string.replace('\n', '')
    if method != None:
        table9['method'] = method.string.replace('Method:', '')

    ip = hover_textList[i].find('span', id='ipssra')
    port = hover_textList[i].find('span', id='portssra')
    password = hover_textList[i].find('span', id='pwssra')
    method = hover_textList[i].find('h4', text=re.compile(r'Method:'))
    if ip != None:
        table10['ip'] = ip.get_text()
    if port != None:
        table10['port'] = port.string.replace('\n', '')
    if password != None:
        table10['password'] = password.string.replace('\n', '')
    if method != None:
        table10['method'] = method.string.replace('Method:', '')

    ip = hover_textList[i].find('span', id='ipssrb')
    port = hover_textList[i].find('span', id='portssrb')
    password = hover_textList[i].find('span', id='pwssrb')
    method = hover_textList[i].find('h4', text=re.compile(r'Method:'))
    if ip != None:
        table11['ip'] = ip.get_text()
    if port != None:
        table11['port'] = port.string.replace('\n', '')
    if password != None:
        table11['password'] = password.string.replace('\n', '')
    if method != None:
        table11['method'] = method.string.replace('Method:', '')

    ip = hover_textList[i].find('span', id='ipssrc')
    port = hover_textList[i].find('span', id='portssrc')
    password = hover_textList[i].find('span', id='pwssrc')
    method = hover_textList[i].find('h4', text=re.compile(r'Method:'))
    if ip != None:
        table12['ip'] = ip.get_text()
    if port != None:
        table12['port'] = port.string.replace('\n', '')
    if password != None:
        table12['password'] = password.string.replace('\n', '')
    if method != None:
        table12['method'] = method.string.replace('Method:', '')

table1['id'] = str(uuid.uuid4()).upper().replace('-', '')
table2['id'] = str(uuid.uuid4()).upper().replace('-', '')
table3['id'] = str(uuid.uuid4()).upper().replace('-', '')
table4['id'] = str(uuid.uuid4()).upper().replace('-', '')
table5['id'] = str(uuid.uuid4()).upper().replace('-', '')
table6['id'] = str(uuid.uuid4()).upper().replace('-', '')
table7['id'] = str(uuid.uuid4()).upper().replace('-', '')
table8['id'] = str(uuid.uuid4()).upper().replace('-', '')
table9['id'] = str(uuid.uuid4()).upper().replace('-', '')
table10['id'] = str(uuid.uuid4()).upper().replace('-', '')
table11['id'] = str(uuid.uuid4()).upper().replace('-', '')
table12['id'] = str(uuid.uuid4()).upper().replace('-', '')

StoreConfig.updateStr(tables)
# print(tables)

