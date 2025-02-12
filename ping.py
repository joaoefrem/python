import subprocess,os,threading,time
from queue import Queue
lock=threading.Lock()
_start=time.time()
def check(n):
    with open(os.devnull, "wb") as limbo:
                ip="192.168.101.{0}".format(n)
                result=subprocess.Popen(["ping", "-n", "1", "-w", "100", ip],stdout=limbo, stderr=limbo).wait()
                with lock:                    
                    if not result:
                        print (ip, " > Active" + " OK")   
                    else:
                        print (ip, " - Inactive" + " OFF")                    
    
def threader():
    while True:
        worker=q.get()
        check(worker)
        q.task_done()
q=Queue()

for x in range(50):
    t=threading.Thread(target=threader)
    t.daemon=True
    t.start()
for worker in range(1,50):
    q.put(worker)
q.join()
print("Process completed in: ",time.time()-_start)