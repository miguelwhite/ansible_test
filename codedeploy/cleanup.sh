#!/bin/bash -l

date=`date '+%Y%m%d%H%M%S'`

mkdir -p /home/admin/backups/
mv /home/admin/ansible_test /home/admin/backups/ansible_test_${date}
