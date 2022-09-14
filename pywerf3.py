import subprocess
from threading import Thread

def check_process(process):
    while process.stdout.readable():
        line = process.stdout.readline()
        if line:
            s_line = line.split()
            print(line.strip())
            subprocess.run("kubectl logs {pod} -n {ns} > log_{pod}-{ns}.txt".format(pod=s_line[1], ns=s_line[0]), shell=True)


process_pods = subprocess.Popen('kubectl get pods -A -o wide -w',
                shell=True,
                universal_newlines=True,
                encoding='utf-8',
                bufsize=1,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE)


t_pods = Thread(target=check_process, args=(process_pods,))
t_pods.start()

t_pods.join()
