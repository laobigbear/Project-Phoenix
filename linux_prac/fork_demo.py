import os
import time

pid = os.fork()
if pid == 0:
    print(f"Child PID={os.getpid()}, PPID={os.getppid()}")
    time.sleep(5)
else:
    print(f"Parent PID={os.getppid()}, PID={pid}")
    time.sleep(10)

