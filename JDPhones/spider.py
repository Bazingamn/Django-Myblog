import re
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pyquery import PyQuery as pq
import time
import pymysql

keyword = '手机'

chrome_options = Options()
chrome_options.add_argument('--headless')
browser = webdriver.Chrome(options=chrome_options)
wait = WebDriverWait(browser, 10)

def search():
    try:
        browser.get("https://www.jd.com/")
        input = wait.until(EC.presence_of_element_located((By.ID, 'key')))
        submit = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#search > div > div.form > button')))
        input.send_keys(keyword)
        submit.click()
        total = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#J_bottomPage > span.p-skip > em:nth-child(1) > b')))
        get_products()
        return total.text
    except TimeoutException:
        return search()

def next_page(page_number):
    print('正在翻页', page_number)
    try:
        # 滑动到底部，加载出后三十个货物信息
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)

        input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#J_bottomPage > span.p-skip > input')))
        submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#J_bottomPage > span.p-skip > a')))
        input.clear()
        input.send_keys(page_number)
        submit.click()
        wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#J_bottomPage > span.p-num > a.curr'), str(page_number)))
        get_products()
    except TimeoutException:
        next_page(page_number)

def get_products():
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#J_goodsList > ul')))
    html = browser.page_source
    doc = pq(html)
    items = doc('#J_goodsList .gl-warp .gl-item .gl-i-wrap').items()
    images = browser.find_element_by_xpath('//div[@class="gl-i-wrap"]/div[1]/a/img')
    #获取商品信息列表
    for item in items:
        product = {
            'name': re.search('.*?\n', item.find('.p-name').text()).group(0)[:-1],
            'price': item.find('.p-price').text()[2:],
            'commit': re.sub('\n', '', item.find('.p-commit').text()),
            'shop': item.find('.p-shop').text(),
            'icons': re.sub('\n', ' ', item.find('.p-icons').text()),
            'image': images.get_attribute('src')
        }
        print(product)
        write_to_mysql(product)

def write_to_mysql(data):
    db = pymysql.connect(host='localhost', user='root', password='123456', db='myblog', charset='utf8')
    cur = db.cursor()
    sqlc = 'insert into mymovie_jdphone values(null,%s,%s,%s,%s,%s,%s)'
    try:
        if cur.execute(sqlc, (data["name"], data["price"], data["commit"], data["shop"], data["icons"], data["image"])):
            print('Successful')
            db.commit()
    except Exception:
        print('Failed')
        db.rollback()
    cur.close()
    db.close()

def main():
    try:
        total = search()
        total = int(re.compile('(\d+)').search(total).group(1))
        for i in range(2, total+1):
            next_page(i)
    except Exception:
        print('Failed')

if __name__ == '__main__':
    main()