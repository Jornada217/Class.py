import os
from os.path import sep, join
from os import path
# from selenium import webdriver

# srcc = 'C:\\Users\\joaopaulo\\PycharmProjects\\Learning_Projects'
# f = 'C:/Users/joaopaulo/PycharmProjects/Learning_Projects/'
#file = 'C:/Users/joaopaulo/PycharmProjects/Learning_Projects/GeoConvertTest.csv'

# def djoin(*args, **kwargs):
#     return join(*args,**kwargs).replace(sep, '/')

# def_dir = join('folder', 'Folder 2')
# print(def_dir)
# default_dir = path.abspath(def_dir)
# print(default_dir)
# dd = djoin(default_dir)
# print(dd)
# print()

src = join('Folder', 'Folder 2', 'GeoConvertTest.csv')
print(src)
# C:\Users\joaopaulo\PycharmProjects\Learning_Projects\Folder\Folder 2
folder = path.abspath('folder')
print(folder)
path1 = path.abspath(src)
print(path1)


def pjoin(*args, **kwargs):
    return join(*args,**kwargs).replace(sep, str('\\'))

path2 = pjoin(path1)
print(path2)

""" Geoconvert context"""
# print('Geoconvert')
# chromeOptions = webdriver.ChromeOptions()
# prefs = {'download.default_directory': 'C:\\Users\\joaopaulo\\PycharmProjects\\Learning_Projects'}
# chromeOptions.add_experimental_option('prefs', prefs)
# chromeOptions.add_argument('headless')
# """ Set the driver's directory """
# chromeDriver = 'C:/Users/joaopaulo/PycharmProjects/Learning_Projects/venv/Scripts/chromedriver.exe'
# driver = webdriver.Chrome(executable_path=chromeDriver, options=chromeOptions)
#
# url = 'http://geoconvert.mimas.ac.uk/index.html'
# """  file = 'C:/Users/joaopaulo/PycharmProjects/Learning_Projects/GeoConvertTest.csv' """
#
# file_src = join('data', 'src', 'GeoConvertTest.csv')
# file_path = path.abspath(file_src)
#
#
# def fjoin(*args, **kwargs):
#     return join(*args, **kwargs).replace(sep, '/')
#
#
# file = fjoin(file_path)
# print(os.getcwd())
# print(file_src)
# print(file_path)
# print(file)