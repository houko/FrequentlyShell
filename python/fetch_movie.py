#! /usr/bin/python3
# coding=utf-8
"""
 把今天最好的表现当作明天最新的起点．．～
 いま 最高の表現 として 明日最新の始発．．～
 Today the best performance  as tomorrow newest starter!
 Created by IntelliJ IDEA.
 author: xiaomo
 github: https://github.com/syoubaku
 email: xiaomo@xiamoo.info
 QQ_NO: 83387856
 Date: 2018/1/29 13:58 
 Description: 拉取猫眼电影的排行
 Copyright(©) 2017 by xiaomo.
"""
import json
import re
from multiprocessing import Pool

import requests
from requests import RequestException


# 拉取html
def get_one_page(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException as e:
        print(e)
        return None


def parse_html(html):
    pattern = re.compile(
        '<dd>.*?board-index.*?">(.*?)</i>.*?name"><a.*?>(.*?)</a>.*?data-src="(.*?)".*?star">(.*?)</p>.*?releasetime">(.*?)</p>.*?</dd>', re.S)
    items = re.findall(pattern, html)
    for item in items:
        yield {
            'title': item[1],
            'image': item[2],
            'actor': item[3].strip()[3:],
            'time': item[4].strip()[5:]
        }
    return items


def write_to_file(content):
    with open('movie.txt', 'a+', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + "\n")
        f.close()


def main(offset):
    page = get_one_page("http://maoyan.com/board/4?offset=" + str(offset))
    for item in parse_html(page):
        write_to_file(item)


if __name__ == '__main__':
    pool = Pool()
    pool.map(main, [i * 10 for i in range(10)])


class Item(object):
    author = ""
    content = ""
