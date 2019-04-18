from bs4 import BeautifulSoup
import requests
import pymysql

def get_one_page(url):
    response = requests.get(url)
    response.encoding = 'utf-8'
    html = response.text
    return html

def parse_one_page(html):
    soup = BeautifulSoup(html, 'lxml')
    i = 0
    for tag in soup.find(attrs={'class': 'c15d'}).find_all('li'):
        i += 1
        #获取每日日期
        w_date = tag.find(attrs={'class': 'time'}).get_text()
        #获取天气情况
        w_weather = tag.find(attrs={'class': 'wea'}).get_text()
        #获取温度
        w_temp = tag.find(attrs={'class': 'tem'}).get_text()
        # 获取风向情况
        w_wind = tag.find(attrs={'class': 'wind'}).get_text()
        # 获取风力大小
        w_strength = tag.find(attrs={'class': 'wind1'}).get_text()
        data = {
            'id': i,
            'date': w_date,
            'weather':w_weather,
            'temp': w_temp,
            'wind': w_wind,
            'strength': w_strength
        }
        print(data)
        write_to_mysql(data)

def write_to_mysql(data):
    db = pymysql.connect(host='localhost', user='root', password='123456', db='myblog', charset='utf8')
    cur = db.cursor()
    sqlc = '''
        insert into mymovie_weathers(id,date,weather,temp,wind,strength) 
        values(%s,%s,%s,%s,%s,%s)
    '''
    try:
        if cur.execute(sqlc, (data["id"], data["date"],data["weather"],data["temp"],data["wind"],data["strength"])):
            print('Successful')
            db.commit()
    except:
        print('Failed')
        db.rollback()
    cur.close()
    db.close()

def main():
    url = 'http://www.weather.com.cn/weather15d/101210701.shtml'
    html = get_one_page(url)
    parse_one_page(html)

if __name__ == '__main__':
    main()