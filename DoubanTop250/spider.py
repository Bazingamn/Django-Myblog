import json
from multiprocessing import Pool
import requests
from requests.exceptions import RequestException
import re
import pymysql

def get_one_page(url):
    try:
        respone=requests.get(url)
        if respone.status_code==200:
            return respone.text
        return None
    except RequestException:
        return None

def parse_one_page(html):
    pattern = re.compile('<li>.*?<em.*?>(\d+)</em>.*?src="(.*?)".*?"title">(.*?)</span>'
                         +'.*?<p class="">(.*?)&nbsp;&nbsp;&nbsp;(.*?)<br>(.*?)&nbsp;/&nbsp;'
                         +'(.*?)&nbsp;/&nbsp;(.*?)</p>.*?"v:average">(.*?)</span>.*?</li>',re.S)
    items = re.findall(pattern, html)
    for item in items:
        data = {
            'index': item[0],
            'title': item[2],
            'director': item[3].strip()[3:],
            'actor': item[4][3:],
            'time': item[5].strip(),
            'region': item[6],
            'type': item[7].strip(),
            'score': item[8],
            'images': item[1]
        }
        # write_to_mysql(data)
    # return items
        print(data)

def write_to_file(content):
    with open('result.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')
        f.close()

def write_to_mysql(data):
    db = pymysql.connect(host='localhost', user='root', password='123456', db='myblog', charset='utf8')
    cur = db.cursor()
    sqlc = '''
        insert into mymovie_movies
        values(null,%s,%s,%s,%s,%s,%s,%s,%s)
    '''
    try:
        if cur.execute(sqlc, (data["title"], data["director"], data["actor"], data["time"], data["region"], data["type"], data["score"], data["images"])):
            print('Successful')
            db.commit()
    except  Exception as e:
        print(e)
        print('Failed')
        db.rollback()
    cur.close()
    db.close()

def main(start):
    url = 'https://movie.douban.com/top250?start=' + str(start)
    html = get_one_page(url)
    # for item in parse_one_page(html):
    #     print(item)
    parse_one_page(html)

if __name__ == '__main__':
     # for i in range(10):
     #     main(i*25)
    # 多进程抓取
    pool = Pool()
    pool.map(main, [i*25 for i in range(10)])