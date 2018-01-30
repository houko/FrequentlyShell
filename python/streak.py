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
 Date: 2018/1/30 16:01 
 Description:  给github 加commit
 Copyright(©) 2017 by xiaomo.
"""
import datetime
import os


def modify():
    file = open('test', 'r')
    flag = int(file.readline()) == 0
    file.close()
    file = open('test', 'w+')
    if flag:
        file.write('1')
    else:
        file.write('0')
        file.close()


def commit():
    os.system('git commit -a -m test_github_streak > /dev/null 2>&1')


def set_sys_time(year, month, day):
    os.system('date -s %04d%02d%02d' % (year, month, day))


def trick_commit(year, month, day):
    set_sys_time(year, month, day)
    modify()
    commit()


def daily_commit(start_date, end_date):
    for i in range((end_date - start_date).days + 1):
        cur_date = start_date + datetime.timedelta(days=i)
        trick_commit(cur_date.year, cur_date.month, cur_date.day)


if __name__ == '__main__':
    daily_commit(datetime.date(2015, 1, 1), datetime.date(2016, 1, 1))
