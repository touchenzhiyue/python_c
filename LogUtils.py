# -*- coding:utf-8 -*-
#日志输出工具类
#createdate 20181217
#version 1.0

import logging

def console_out(logFilename):
    logging.basicConfig(
        level = logging.DEBUG,  #定义日志输出的级别
        format = '%(asctime)s %(filename)s : %(levelname)s %(message)s', #定义输出日志格式
        datefmt = '%Y-%m-%d %A %H:%M:%S', #定义时间格式
        filename = logFilename,   #日志文件名
        filemode = 'a'  #写入的模式‘w’或者‘a’
    )
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)  #定义该handler级别
    formatter = logging.Formatter('%(asctime)s %(filename)s : %(levelname)s %(message)s')
    console.setFormatter(formatter)
    logging.getLogger().addHandler(console)

if __name__ == "__main__":
    console_out('loggine.log')