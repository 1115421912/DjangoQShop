import requests
import os
from lxml import etree
# 数据解析
def parse_content(tree):
    shop_info_list = tree.xpath('//div[@class="ml-wrap"]/div[2]/ul/li')
    # db = DBManage()
    for shop_info in shop_info_list:
        c_price = shop_info.xpath('./div[@class="gl-i-wrap"]/div[@class="p-price"]/strong/i/text()')[0]
        url = shop_info.xpath('./div[@class="gl-i-wrap"]/div[@class="p-name p-name-type-2"]/a/@href')[0]
        p_url = shop_info.xpath("./div[@class='gl-i-wrap']/div[@class='p-img']/a/img/@source-data-lazy-img")[0]
        photo_url = 'https:'+p_url
        c_picture = photo(photo_url)

def photo(url):
    root_path = r'E:\PythonFramework\DjangoQShop\ZhanLi\Buyer\static\buyer\images'
    #利用split()函数获取url最后的文件名
    img_name = url.split('/')[-1]
    img_path = root_path + r'\{0}'.format(img_name)
    try:
        if not os.path.exists(img_path):
            r = requests.get(url)
            with open(img_path, 'wb') as f:
                f.write(r.content)
                print("文件保存成功")
                return img_name
        else:
            print("文件已存在")
    except:
        print("执行出错")