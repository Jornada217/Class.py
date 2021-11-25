
#Multiprocessing = running tasks in parallel on different CPU cores, bypasses GIL used for threading
#Multiprocessing = better for CPU bound task (heavy CPU usage)

from multiprocessing import Process, cpu_count
import time

def counter(num):
    count = 0
    while count < num:
        count += 1

def main():
    print(cpu_count())
    a = Process(target=counter, args=(25000000,))
    b = Process(target=counter, args=(25000000,))
    c = Process(target=counter, args=(25000000,))
    d = Process(target=counter, args=(25000000,))
    a.start()
    b.start()
    c.start()
    d.start()
    a.join()
    b.join()
    c.join()
    d.join()
    print("Finished in {} seconds.".format(time.perf_counter()))

if __name__ == '__main__':  #if I am running Windows
    main()