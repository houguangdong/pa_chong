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
import jenkins
from django.core.mail import send_mail
os.environ['DJANGO_SETTINGS_MODULE']='g11nRepository.settings'
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "g11nRepository.settings")


product_dict = {
    '133': 'ts', '132': 'cls', '131': 'vapi', '130': 'vimclients', '137': 'vmrc', '136': 'daas', '135': 'integrity', '134': 'vdcs', '139': 'vcops-vmware-om-adapter', 
    '138': 'vrops', '166': 'viewusbcart', '167': 'view', '160': 'viewportalwar', '161': 'crtbora', '162': 'viewcrt', '163': 'viewclientweb', '121': 'tools(bora)', 
    '122': 'tools(bora-vmsoft)', '124': 'vcoserver-ng', '125': 'hws-desktop-client', '128': 'vimclients-platform', '129': 'Vsphere-client-modules', '58': 'ciswin', 
    '54': 'marvin2.0.1', '57': 'BDE', '56': 'vIDM', '51': 'Host client', '50': 'VUM', '53': 'vRB', '52': 'loginsight', '164': 'viewportalwar', '115': 'SV_Agent', 
    '114': 'wem-agent-installer', '116': 'srm', '110': 'vshield-mgmtplatform', '113': 'hydra', '112': 'hms-va', '82': 'vimclients', '83': 'vsphere-ui-useless', 
    '80': 'vsphere-client-modules', '81': 'vsphere-ui-modules-useless', '86': 'vsphere-ui', '87': 'vcloud', '85': 'vsphere-ui-modules', '108': 'vsmva', '109': 'vseva', 
    '102': 'WorkStation', '103': 'HvRO', '100': 'vsaniscsingc', '106': 'Astro', '107': 'vshield-sslvpn-client-win', '104': 'Mirage', '105': 'AccessPoint', '38': 'Marvin2.0.0', 
    '37': 'VIO', '60': 'licenseservice', '61': 'rd-identity-server', '62': 'ciswin_standalone', '63': 'fusion', '65': 'vcsa_installer', '66': 'licenseservice', 
    '67': 'appliance-mgmt-ui', '68': 'vcsa-ui-installer', '69': 'cls', '173': 'vIDM', '172': 'rde-rft-all', '171': 'rde-rft-all', '154': 'vseva', '2': 'vRA', 
    '99': 'vsan-health-ui', '98': 'vsan', '168': 'cafe-container', '169': 'admiral', '91': 'vsphere-ui-modules', '90': 'phonehome', '93': 'vsphere-client-modules', 
    '92': 'vsphere-ui', '95': 'vsanhealth', '94': 'vimclients', '97': 'vsanvit', '96': 'vsanmgmt', '89': 'rd-identity-server', '150': 'viewusbcart', '153': 'vsmva', 
    '152': 'vshield-sslvpn-client-win', '155': 'vshield-mgmtplatform', '41': 'client-module', '157': 'view', '159': 'v4c (v4pa)', '158': 'v4v(v4h)', '48': 'VAMI', 
    '46': 'vapi', '119': 'srm_vrops', '44': 'vcenter', '43': 'vpxwin', '40': 'vimclients', '118': 'hws-desktop-client', '146': 'vsphere-ui', '147': 'crtbora', 
    '145': 'vsphere-ui-modules', '142': 'view', '143': 'installkit', '140': 'vcopssuitevm', '148': 'viewcrt', '149': 'viewclientweb', '77': 'vsphere-client-modules', 
    '76': 'vimclients', '75': 'ciswin_standalone', '74': 'vcenter', '73': 'iso', '72': 'ts', '71': 'ovfs', '70': 'vmsyslogcollector', '79': 'cls', '78': 'vapi'
}


user_info = {
    'username': 'ghou',
    'password': 'Donga@123'
}


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
    content += 'GRM font-end:\n'
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
    content += '\n\nGRM back-end:\n'
    #　sudo pip install python-jenkins (need setup jenkins package)
    server=jenkins.Jenkins("http://gabi.eng.vmware.com:8080", username=user_info['username'], password=user_info['password'])
    jobs_list = server.get_all_jobs('/api/python')
    i = 1
    for item in jobs_list:
        if item['color'] == 'red':
            item_number = item['name'].split('-')[0].strip()
            product_name = product_dict.get(item_number)
            if item_number and product_name:
                content += '%s %s product(release_%s) is build fail' % (i, product_name, item_number)
            elif item_number:
                content += '%s release_%s is build fail' % (i, item_number)
            content += '\n'
            i+=1
    #　g11n-grm-project@vmware.com
    send_mail("GRM daily maintenance information", content, 'ghou@vmware.com', ['g11n-grm-project@vmware.com'], auth_user=user_info['username'], auth_password=user_info['password'])


def main():
    logger = test_get_logger()
    daily_send_mail(logger)


if __name__ == '__main__':
    main()