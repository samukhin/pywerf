from multiprocessing import Process
import subprocess

def check():
    subprocess.check_output("kubectl get events -A -o wide -w > events", shell=True).decode("utf-8").split('\n')
    
def check2():
    subprocess.check_output("kubectl get pods -A -o wide -w > pods", shell=True).decode("utf-8").split('\n')

p = Process(target=check, args=())
p1 = Process(target=check2, args=())
p.start()
p1.start()
p.join()
p1.join()
