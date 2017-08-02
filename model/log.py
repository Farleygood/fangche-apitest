#! /usr/bin/env python
# coding:utf-8
__author__ = 'Farley'

import logging
from logging.handlers import RotatingFileHandler
import threading
import configparser
import time

class LogSignleton(object):
    def __init__(self, log_config):
        self.log_filename = log_config
        # pass

    def __new__(cls, log_config):
        mutex=threading.Lock()
        mutex.acquire() # 上锁，防止多线程下出问题
        if not hasattr(cls, 'instance'):
            '''
               单例模式：
               将类LogSignleton的实例绑定到类变量instance上
               如果cls.instance为None说明该类还没有实例化过，实例化该类并返回
               如果cls.instance不为None，直接返回cls.instance
            '''
            cls.instance = super(LogSignleton, cls).__new__(cls)
            config = configparser.ConfigParser()
            config.read(log_config, encoding='utf-8')
            # cls.instance.log_filename = config.get('LOGGING', 'log_file')
            cls.instance.max_bytes_each = int(config.get('LOGGING', 'max_bytes_each'))
            cls.instance.backup_count = int(config.get('LOGGING', 'backup_count'))
            cls.instance.fmt = config.get('LOGGING', 'fmt')
            cls.instance.log_level_in_console = int(config.get('LOGGING', 'log_level_in_console'))
            cls.instance.log_level_in_logfile = int(config.get('LOGGING', 'log_level_in_logfile'))
            cls.instance.logger_name = config.get('LOGGING', 'logger_name')
            cls.instance.console_log_on = int(config.get('LOGGING', 'console_log_on'))
            cls.instance.logfile_log_on = int(config.get('LOGGING', 'logfile_log_on'))
            cls.instance.logger = logging.getLogger(cls.instance.logger_name)
            cls.instance.__config_logger()
        mutex.release()
        return cls.instance

    def get_logger(self):
        return  self.logger

    def __config_logger(self):
        # 设置日志格式
        fmt = self.fmt.replace('|','%')
        formatter = logging.Formatter(fmt)
        # 日志存储时间精确到分,每次运行都单独存储一份日志文件,如果闲太多精确到天即可
        # ftime = time.strftime('%Y%m%d_%H_%M',time.localtime(time.time()))
        ftime = time.strftime('%Y%m%d',time.localtime(time.time()))
        self.log_filename = ("E:/Pyscript/fangche/log/apitest_%s.log" % ftime)


        if self.console_log_on == 1: # 如果开启控制台日志
            console = logging.StreamHandler()
            console.setFormatter(formatter)
            self.logger.addHandler(console)
            self.logger.setLevel(self.log_level_in_console)

        if self.logfile_log_on == 1: # 如果开启文件日志
            rt_file_handler = RotatingFileHandler(self.log_filename, maxBytes=self.max_bytes_each, backupCount=self.backup_count)
            rt_file_handler.setFormatter(formatter)
            self.logger.addHandler(rt_file_handler)
            self.logger.setLevel(self.log_level_in_logfile)

# python3这里不能写相对路径 如./config/logconf.conf
logsignleton = LogSignleton('E:/Pyscript/fangche/config/log_config')
logger = logsignleton.get_logger()