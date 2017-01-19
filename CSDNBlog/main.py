#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ""
__author__ = "altamob"
__mtime__ = "2016/9/1"
# code is far away from bugs with the god animal protecting
I love animals. They taste delicious.
┏┓ ┏┓
┏┛┻━━━┛┻┓
┃ ☃ ┃
┃ ┳┛ ┗┳ ┃
┃ ┻ ┃
┗━┓ ┏━┛
┃ ┗━━━┓
┃ 神兽保佑 ┣┓
┃　永无BUG！ ┏┛
┗┓┓┏━┳┓┏┛
┃┫┫ ┃┫┫
┗┻┛ ┗┻┛
"""
import sys

reload(sys)  # Python2.5 初始化后会删除 sys.setdefaultencoding 这个方法，我们需要重新载入   
sys.setdefaultencoding('utf-8')


from scrapy import cmdline
cmdline.execute("scrapy crawl CSDNBlog ".split())

# def fib(n):
#     count = 0
#     a = 1
#     b = 0
#     temp = 0
#     while count < n:
#         temp = a
#         b = a + b
#         a = b
#         b = temp
#         count += 1
#         yield b
#
#
# if __name__ == "__main__":
#     for i in fib(100):
#         print i
