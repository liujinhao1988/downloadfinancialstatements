import random,time,requests,os
a = 'http://money.finance.sina.com.cn/corp/go.php/vDOWN_ProfitStatement/displaytype/4/stockid/{}/ctrl/all.phtml'
b = 'sh{}_ProfitStatement.xls'

session = requests.Session()

headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5)AppleWebKit 537.36 (KHTML, like Gecko) Chrome","Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"}


#获取csv中的股票list 添csv文件名
csv_name = 'sh4'

def get_list(aaa):
    stock_csv = '/home/liujinhao/data/stocklist/{}.csv'
    f = open(stock_csv.format(aaa), 'r')
    content = f.read()
    list = []
    rows = content.split('\n')
    for row in rows:
        list.append(row.split(','))
    f.close()
    list = list[0:-1]
    return list

list = get_list(csv_name)





#xinde



while True:
    try:
        num = len(os.listdir('/home/liujinhao/data/week1')) - 1  # len（空文件夹）为1,不知
        list_download = list[num:]
        for i in list_download:
            i = i[0].strip('.csv').strip('sh')  # sh要改
            url = a.format(i)
            path = b.format(i)
            time.sleep(random.randint(3, 6))
            r = session.get(url, headers=headers)
            print('get'+str(i))
            time.sleep(random.randint(3, 6))
            with open(path, 'wb') as f:
                f.write(r.content)
            time.sleep(random.randint(5, 10))
    except requests.exceptions.ConnectionError:
        print('error')
        time.sleep(random.randint(10, 20))
        continue
    if len(os.listdir('/home/liujinhao/data/week1')) - 1 == len(list):
        break



