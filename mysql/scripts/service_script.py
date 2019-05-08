from subprocess import call
import os
import time

quiesce_state = "OFF"
lock_file = "/tmp/quiesce.lock"
while True:
	if os.path.exists(lock_file):
		if quiesce_state is "ON":
			pass
		else:
			quiesce_state="ON"
			call(["bash", "/scripts/pre_freeze.sh"])
	else:
		if quiesce_state is "OFF":
			pass
		else:
			call(["bash", "/scripts/post_thaw.sh"])
			quiesce_state = "OFF"
	time.sleep(0.2)