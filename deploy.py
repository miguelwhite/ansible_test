#!/usr/bin/env python3

import os
import subprocess

PLAYBOOK_MAPS = {
  'create_server': '/home/admin/.local/bin/ansible-playbook --vault-password-file /home/admin/.ansible_vault_pass -i inventories/localhost.ini playbooks/create_server.yaml -vvv'
}

command = '''
pwd;
ls -l;
pip install -r requirments.txt;
{playbook_run};
'''.format(playbook_run=PLAYBOOK_MAPS[os.environ.get('APPLICATION_NAME')])

try:
    subprocess.check_output(
      command,
      stderr=subprocess.STDOUT,
      cwd=os.getcwd(),
      shell=True
    )
except subprocess.CalledProcessError as e:
    print(e.output.decode("utf-8"))
    raise e
