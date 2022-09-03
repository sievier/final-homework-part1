import requests
import time
import time
import  jsonpath
from multiprocessing.pool import Pool



name = 1


def get_page(offset):
    global headers
    headers = {
        'cookie': 'tt_webid=6925326312953529869; s_v_web_id=verify_kkqm44un_jaeWrYZ1_CnOS_4Xuz_BNoi_lE3QmTQ37uHC; csrftoken=280e107c397cea753911229202dc0c3d; ttcid=45904355bfa4470f9543c9cdeb94869f30; tt_webid=6925326312953529869; csrftoken=280e107c397cea753911229202dc0c3d; __ac_signature=_02B4Z6wo00f01Coh3wgAAIDDmtAzwcHMKowqBduAAGqaWRSmr26jOpvMaDLR3MsdEfPZTRN9mxTbUMgGifTuVJdj6FgWrIu6yKXVS3Dsp.wz3Pxl9vgfeguqCWDdZ4ocFVxb4JgkNBJTefPR41; __tasessionId=pyia55cn11612433914121; MONITOR_WEB_ID=2264d055-a390-4e4b-9b1f-4a3e2a6ac47c; tt_scid=pcBhM4miMb3tReqLN21gkwPxqHE92TFulL0hVtP4mdhm0UL1X0v0T1r158U8hVOua37f',
        'referer': 'https://www.toutiao.com/search/?keyword=%E7%BE%8E%E5%A5%B3',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest'
    }
    params = {
        'aid':'24',
        'app_name':'web_search',
        'offset':offset,
        'format':'json',
        'keyword':'疫情',
        'autoload':'true',
        'count':'15',
        'en_qc':'2',
        'cur_tab':'2',
        'from':'search_tab',
        'pd':'synthesis',
        'timestamp':int(time.time())
    }
    url = 'https://www.toutiao.com/api/search/content/?'
    try:
        response = requests.get(url, headers=headers, params=params)
        response.content.decode('utf-8')
        if response.status_code == 200:
            return response.json()
    except requests.ConnectionError as e:
        print('连接失败', e)


def get_info(json):
    new_img_lists = []

    image_lists = jsonpath.jsonpath(json, '$.data[*].image_list..url')
    print(image_lists)
    for image_list in image_lists:
        new_img_list = image_list.replace('p1', 'p6').replace('p3', 'p6').replace('list','origin').replace('/190x124', '')
        new_img_lists.append(new_img_list)
    return new_img_lists


def save_img(new_image_lists):
    global name
    for image in new_image_lists:
        print('-------正在获取第{}张----------'.format(name))
        data = requests.get(image, headers=headers).content
        time.sleep(0.3)
        with open(f'../images/{name}.jpg', 'wb') as f:
            f.write(data)
        name += 1


def main(offset):
    json = get_page(offset)
    print((json['data'][0]['abstract']))
    print((json['data'][1]['abstract']))
    print(len(json['data']))
    print((json['data'][0]['datetime']))
    print((json['data'][1]['datetime']))
    #new_image_lists = get_info(json)
    #save_img(new_image_lists)


if __name__ == '__main__':
    pool = Pool()
    groups = [i * 20 for i in range(4)]
    pool.map(main, groups)
    pool.close()
    pool.join()