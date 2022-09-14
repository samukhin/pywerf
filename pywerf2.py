import subprocess
from threading import Thread

def check_process(process):
    while process.stdout.readable():
        line = process.stdout.readline()
        if line:
            print(line.split())


process_events = subprocess.Popen('kubectl get events -A -o wide -w',
                shell=True,
                universal_newlines=True,
                encoding='utf-8',
                bufsize=1,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE)

process_pods = subprocess.Popen('kubectl get pods -A -o wide -w',
                shell=True,
                universal_newlines=True,
                encoding='utf-8',
                bufsize=1,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE)



t_pods = Thread(target=check_process, args=(process_pods,))
t_pods.start()

#t_events = Thread(target=check_process, args=(process_events,))
#t_events.start()


#process_pods.wait()
t_pods.join()

#process_events.wait()
#t_events.join()

