#!/bin/sh

#post-thaw-script

date >> '/scripts/post_root.log'
echo -e "\n attempting to run post-thaw script for MySQL as root user\n" >> /scripts/post_root.log
if [ "$(id -u)" -eq "0" ]; then
python '/scripts/unquiesce.py'
else
date >> '/scripts/post_root.log'
echo -e "not root useri\n" >> '/scripts/post_root.log'
fi


