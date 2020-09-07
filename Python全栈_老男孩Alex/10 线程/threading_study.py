import threading
import time

def run(n):
    print("task ", n)
    time.sleep(2)
    print("task done", n)

start_time = time.time()
t_objs = [] #存线程实例

for i in range(50):
    t=threading.Thread(target=run,args=("t-%s" %i ,))
    t.start()

    
print("----------all threads has finished...")
print("cost:",time.time() - start_time)