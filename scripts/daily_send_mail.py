# -*- coding: utf-8 -*-
'''
Created on 8/25/2016

@author: ghou
'''

import os
import subprocess
import logging
import datetime
import traceback
from django.core.mail import send_mail
os.environ['DJANGO_SETTINGS_MODULE']='g11nRepository.settings'
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "g11nRepository.settings")


def test_get_logger():
    logger = logging.getLogger()
    #set loghandler
    file = logging.FileHandler("daily_send_mail.log")
    logger.addHandler(file)
    #set formater
    formatter = logging.Formatter("%(asctime)s %(levelname)s %(message)s")
    file.setFormatter(formatter)
    #set log level
    logger.setLevel(logging.NOTSET)
    return logger


def daily_send_mail(logger):
    supervisor_status = "sudo supervisorctl status"
    p = subprocess.Popen(supervisor_status, shell=True)
    stdout, stderr = p.communicate()
    content = 'Hi All, \n'
    content += 'This is %s report' % datetime.date.today() +'\n\n'
    if stdout or stderr:
        supervisor_message = '1 supervisor process is down'
        logger.info("supervisor process is down out %s, err %s" % (stdout, stderr))
    else:
        supervisor_message = '1 supervisor process is success'
    content += supervisor_message + '\n'
    rabbitmq_status = "sudo rabbitmqctl status"
    p1 = subprocess.Popen(rabbitmq_status, shell=True)
    stdout, stderr = p1.communicate()
    if stdout or stderr:
        rabbitmq_message = '2 rabbitmq process is down'
        logger.info("rabbitmq process is down out %s, err %s" % (stdout, stderr))
    else:
        rabbitmq_message = '2 rabbitmq process is success'
    content += rabbitmq_message + '\n'
    memory_status = "free -m | awk '{print $3}' | head -2"
    p2 = subprocess.Popen(memory_status, shell=True, stdout=subprocess.PIPE)
    stdout, stderr = p2.communicate()
    if stderr:
        memory_free = '3 memory command is err'
        logger.info("memory command err message is %s" % stderr)
    else:
        stdout = stdout.replace('\n', ' ')
        memory_free = '3 memory is %sM' % stdout
    content += memory_free + '\n'
    cpu_status = "/usr/bin/top -bcn 1 |grep Cpu | awk -F 'us,' '{print $1}' | awk -F ':' '{print $2}'"
    p3 = subprocess.Popen(cpu_status, shell=True, stdout=subprocess.PIPE)
    stdout, stderr = p3.communicate()
    if stderr:
        cpu_use_rate = '4 cpu command is err'
        logger.info("cpu command err message %s" % stderr)
    else:
        try:
            cpu_rate = stdout.split(' ')[1]
        except:
            print(traceback.format_exc())
        cpu_use_rate = '4 cpu use rate is %s%%' % cpu_rate
    content += cpu_use_rate
    send_mail("GRM daily maintenance information", content, 'ghou@vmware.com', ['g11n-grm-project@vmware.com'], auth_user='ghou@vmware.com', auth_password='Donga@123')


def main():
    logger = test_get_logger()
    daily_send_mail(logger)


if __name__ == '__main__':
    main()