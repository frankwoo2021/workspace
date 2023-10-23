#########################################################################
# 作者:李宁（蒙娜丽宁）
#
# 微信公众号：极客起源
#
# B站：https://space.bilibili.com/477001733
#
# Copyright © 2022 Lining. All rights reserved.
#
# 版本: 2.0
#########################################################################

# 从百度抓取金字塔图片
# pip install Pillow
from urllib3 import *
import os
import re
import json

from openpyxl import Workbook
from openpyxl.drawing.image import Image
wb = Workbook()
ws = wb.active
ws.title = '百度金字塔图片'

http = PoolManager(cert_reqs='CERT_NONE')

disable_warnings()

os.makedirs('download/images', exist_ok=True)


def str2Headers(file):
    headerDict = {}
    f = open(file, 'r')

    headersText = f.read()

    # Linux、Unix、Mac OS X：\n
    # Windows：\r\n
    headers = re.split('\n', headersText)
    for header in headers:
        result = re.split(':', header, maxsplit=1)
        headerDict[result[0]] = result[1]
    f.close()
    return headerDict



headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Connection': 'keep-alive',
    'Host': 'image.baidu.com',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'Cookie': 'BIDUPSID=C83C9894B9D0617F3499D7D7F8145D64; PSTM=1527692262; __yjs_duid=1_e6582616e119c654ee35a567c2e0a3691619437312887; BDUSS=NleGlQVUljMzBMQkZDZ1ZVbDBrbEhHb2E1N2FzRURHM2I3N2NHcjd5TFdOTmRnRVFBQUFBJCQAAAAAAAAAAAEAAACtLaUxYWJjZGRkZGQ2MAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAANanr2DWp69gWW; BDUSS_BFESS=NleGlQVUljMzBMQkZDZ1ZVbDBrbEhHb2E1N2FzRURHM2I3N2NHcjd5TFdOTmRnRVFBQUFBJCQAAAAAAAAAAAEAAACtLaUxYWJjZGRkZGQ2MAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAANanr2DWp69gWW; BAIDUID=4128DB79A4E357AF41A7D9B3F7A862E6:FG=1; H_WISE_SIDS=110085_127969_177895_178384_178639_179347_179461_180276_181485_181588_182234_182531_182847_183035_183329_183760_184012_184267_184320_184734_184793_184891_184892_185268_185306_185519_185635_185654_185879_186319_186411_186595_186682_186830_186841_186843_187023_187067_187189_187282_187292_187392_187432_187496_187533_187540_187669_187819_187828_187877_187929_187992_188031_188182_188295_188352_188427_188614_188665_188670_188714_188733_188794_188846_188872_188995_189041_189050_189326_189390_189430_189680_189722_8000076_8000104_8000120_8000142_8000143_8000145_8000149_8000162_8000172_8000178_8000185; BAIDUID_BFESS=49AF3EA955172B9953A3678B3FED803F:FG=1; ZFY=uH5BUveaftaStxjPXKL2fIGDa:AL6L6A1JUa69CqjO9Q:C; H_PS_PSSID=35410_34443_35104_31254_35436_34584_35490_35246_34871_35315_26350; BA_HECTOR=al0la4a12h85ak24qv1grud620r; BDRCVFR[X_XKQks0S63]=mk3SLVN4HKm; userFrom=www.baidu.com; firstShowTip=1; BDRCVFR[dG2JNJb_ajR]=mk3SLVN4HKm; BDRCVFR[-pGxjrCMryR]=mk3SLVN4HKm; ab_sr=1.0.1_ZDA5ODIwZGExYmNmNThiYjZiYWY0ZDM5ZjcxNDcwYzE1YTlhY2U5Yjk4MDllZGNlY2RkM2MwNjhiYTA5YTJlMjU1NTY3MjBkNzk2N2I5NDYyNTBiYzZlNjJhNWMyMzkzMjhmZDYwM2JmZjBlY2UyOGYzMTczNzExYTE1MGIwNTRlN2IyMDY4ZDUyYTY5N2YxN2M0Y2MyMDI5ZDg3ZWVlMTA0NGEzMTg2NTliY2Y1ZTkzYTFkYmJmY2UxYTcyMjk4'

}
headers1 = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Connection': 'keep-alive',
    'Host': 'img0.baidu.com',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'Cookie': 'BIDUPSID=C83C9894B9D0617F3499D7D7F8145D64; PSTM=1527692262; __yjs_duid=1_e6582616e119c654ee35a567c2e0a3691619437312887; BDUSS=NleGlQVUljMzBMQkZDZ1ZVbDBrbEhHb2E1N2FzRURHM2I3N2NHcjd5TFdOTmRnRVFBQUFBJCQAAAAAAAAAAAEAAACtLaUxYWJjZGRkZGQ2MAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAANanr2DWp69gWW; BDUSS_BFESS=NleGlQVUljMzBMQkZDZ1ZVbDBrbEhHb2E1N2FzRURHM2I3N2NHcjd5TFdOTmRnRVFBQUFBJCQAAAAAAAAAAAEAAACtLaUxYWJjZGRkZGQ2MAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAANanr2DWp69gWW; BAIDUID=4128DB79A4E357AF41A7D9B3F7A862E6:FG=1; H_WISE_SIDS=110085_127969_177895_178384_178639_179347_179461_180276_181485_181588_182234_182531_182847_183035_183329_183760_184012_184267_184320_184734_184793_184891_184892_185268_185306_185519_185635_185654_185879_186319_186411_186595_186682_186830_186841_186843_187023_187067_187189_187282_187292_187392_187432_187496_187533_187540_187669_187819_187828_187877_187929_187992_188031_188182_188295_188352_188427_188614_188665_188670_188714_188733_188794_188846_188872_188995_189041_189050_189326_189390_189430_189680_189722_8000076_8000104_8000120_8000142_8000143_8000145_8000149_8000162_8000172_8000178_8000185; BAIDUID_BFESS=49AF3EA955172B9953A3678B3FED803F:FG=1; ZFY=uH5BUveaftaStxjPXKL2fIGDa:AL6L6A1JUa69CqjO9Q:C; H_PS_PSSID=35410_34443_35104_31254_35436_34584_35490_35246_34871_35315_26350; BA_HECTOR=al0la4a12h85ak24qv1grud620r; BDRCVFR[X_XKQks0S63]=mk3SLVN4HKm; userFrom=www.baidu.com; firstShowTip=1; BDRCVFR[dG2JNJb_ajR]=mk3SLVN4HKm; BDRCVFR[-pGxjrCMryR]=mk3SLVN4HKm; ab_sr=1.0.1_ZDA5ODIwZGExYmNmNThiYjZiYWY0ZDM5ZjcxNDcwYzE1YTlhY2U5Yjk4MDllZGNlY2RkM2MwNjhiYTA5YTJlMjU1NTY3MjBkNzk2N2I5NDYyNTBiYzZlNjJhNWMyMzkzMjhmZDYwM2JmZjBlY2UyOGYzMTczNzExYTE1MGIwNTRlN2IyMDY4ZDUyYTY5N2YxN2M0Y2MyMDI5ZDg3ZWVlMTA0NGEzMTg2NTliY2Y1ZTkzYTFkYmJmY2UxYTcyMjk4'

}
def processResponse(response):
    global count
    if count > 100:
        return
    s = response.data.decode('utf-8')
    d = json.loads(response.data)
    n = len(d['data'])
    for i in range(n - 1):
        if count > 100:
            return
        imageUrl = d['data'][i]['hoverURL'].strip()
        if imageUrl != '':
            print(imageUrl)
            r = http.request('GET', imageUrl, headers=headers1)

            row = count // 26 + 1
            col = count % 26 + 1


            count += 1
            fn = 'download/images/%0.5d.jpg' % count
            print(fn)
            ws.column_dimensions[chr(64 + col)].width = 12
            ws.row_dimensions[row].height = 80

            imageFile = open('temp.webp', 'wb')
            imageFile.write(r.data)
            imageFile.close()
            from PIL import Image as PILImage
            im = PILImage.open('temp.webp').convert('RGB')
            im.save(fn, 'jpeg')
            image = Image(fn)
            image.width, image.height = (image.width // 5, image.height // 5)
            ws.add_image(image, chr(64 + col) + str(row))


count = 0
row = 0
col = 0
pn = 0
rn = 30
url = 'https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=%E9%87%91%E5%AD%97%E5%A1%94&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&word=%E9%87%91%E5%AD%97%E5%A1%94&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&pn={pn}&rn={rn}&gsm=1e&1512281761218='.format(
    pn=pn, rn=rn)


while count <= 100:
    r = http.request('GET', url, headers=headers)
    print(url)
    processResponse(r)
    pn += 30

wb.save('baidu_images.xlsx')