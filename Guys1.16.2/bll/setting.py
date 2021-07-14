# encoding: utf-8
# author: QiFuMin
# contact: 1248227761@qq.com
# site: https://www.jianshu.com/u/eaaae8e04a35
# software: PyCharm
# file: setting.py
# time: 20-1-4 上午10:04
import os
SERVER_ADDR = ("0.0.0.0", 8026)
CLIENT_ADDR = ("127.0.0.1", 8026)

CLIENT_FILE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+'/static/client_received_file'
SERVER_FILE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+'/static/server_received_file'
AUTO_LOGIN_STATE_FILE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+'/static/auto_login_state_file'
# print(BASE_DIR)