#!/usr/bin/env python
# coding=utf-8
import sys
import setuptools
sys.argv=['setup.py','sdist','bdist_wheel'] #将sys.argv的外部参数改成setup.py。相当于是运行python
with open("README.md", 'r',encoding='UTF-8') as f:
    long_description=f.read()

setuptools.setup(
    name="test_xixi",#软件包名称
    version='1.0',
    author="许焕燃",
    author_email='527077832@qq.com',
    description="暂无软件简介信息",
    long_description=long_description,#详细描述
    long_description_content_type="text/markdown",#详细描述的格式
    # url="https://ssl.xxx.org/redmine/projects/RedisRun", #模块的github地址
    packages=setuptools.find_packages(),
    # py_modules=["Tool"],
    classifiers=[# 程序的所属分类列表
         "Development Status :: 3 - Alpha",
         "Topic :: Utilities",
         "License :: OSI Approved :: GNU General Public License (GPL)",
    ],
    python_requires='>=3'
)
