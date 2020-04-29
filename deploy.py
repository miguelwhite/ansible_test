#!/usr/bin/env python3

import os
import subprocess

PLAYBOOK_MAPS = {
  'create_server': 'ansible-playbook -i inventories/localhost.ini playbooks/create_server.yaml -vvv'
}

command = '''
pip install -r requirments.txt;
{playbook_run};
'''.format(playbook_run=PLAYBOOK_MAPS[os.environ.get('APPLICATION_NAME')])

try:
    subprocess.check_output(
      PLAYBOOK_MAPS[os.environ.get('APPLICATION_NAME')],
      stderr=subprocess.STDOUT,
      shell=True
    )
except subprocess.CalledProcessError as e:
    print(e.output.decode("utf-8"))
    raise e
