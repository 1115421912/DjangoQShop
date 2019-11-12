import requests
import os
from lxml import etree
from settings import url, headers
from db import DBManage
from model import Shop
from settings import c_classify
# 网络访问
def request_content(url, headers):
    response = requests.get(url, headers=headers).content.decode('gbk')
    t = etree.HTML(response)
    # print(response)
    # with open('jd.html', 'w', encoding='utf-8') as f:
    #     f.write(response)
    return t
def request_content_x(url, headers):
    try:
        response = requests.get(url, headers=headers).content.decode('gbk')
        t = etree.HTML(response)

        return t
    except:
        pass
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
            return 'images'
    except:
        print("执行出错")

#分类选择


# 数据解析
def parse_content(tree):
    # print(type(tree))
    shop_info_list = tree.xpath('//div[@class="f-sort"]/a/@href')
    print(shop_info_list)
    # db = DBManage()
    # for shop_info in shop_info_list:
    #     c_price = shop_info.xpath('./div[@class="gl-i-wrap"]/div[@class="p-price"]/strong/i/text()')[0]
    #     url = shop_info.xpath('./div[@class="gl-i-wrap"]/div[@class="p-name p-name-type-2"]/a/@href')[0]
    #     print(url)
    #     print(c_price)
    #     p_url = shop_info.xpath("./div[@class='gl-i-wrap']/div[@class='p-img']/a/img/@source-data-lazy-img")[0]
    #     photo_url = 'https:' + p_url
        # c_picture = photo(photo_url)
        # if not 'https:' in url:
        #     full_url = 'https:'+url
        # else:
        #     full_url = url
        # tree = request_content_x(full_url, headers)
        # try:
        #     c_title = tree.xpath('//div[@class="sku-name"]//text()')[-1].strip()
        #     title = c_title.split(' ')
        #     print(c_title[:14])
        #     title = title[-1] if len(title[-1]) > 10 else c_title[:15]
        #     print(title[:15])
        #     print('*'*50)
            # xxxx = tree.xpath('//ul[@class="parameter2 p-parameter-list"]/li/text()')
            # print(xxxx)
            # for xx in xxxx:
            #     if '商品名称' in xx:
            #         lists = xx.split('：')
            #         c_title = lists[1]
            #     else:
            #         c_weight = ' '
            #     if '商品毛重' in xx:
            #         lists = xx.split('：')
            #         c_weight = lists[1]
            #     else:
            #         c_weight = ' '
            #     if '商品产地' or '国产/进口' in xx:
            #         lists = xx.split('：')
            #         c_CO = lists[1]
            #     else:
            #         c_CO = ' '
            #     if '口味' in xx:
            #         lists = xx.split('：')
            #         c_taste = lists[1]
            #     else:
            #         c_taste = ' '
            #
            # print(c_title, c_price, c_weight, c_CO, c_taste, c_classify, "images\\"+c_picture)
            # item = Shop(c_title, c_price, c_weight, c_CO, c_taste, c_classify, "images\\"+c_picture)
            # db.save_item(item)
        # except:
        #     pass

if __name__ == '__main__':
    tree = request_content(url, headers)
    parse_content(tree)
