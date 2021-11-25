# GIL = Global interpreter lock.
# Allows only one thread to hold control of the Phyton interpreter.
#  cpu bound = program/task spends most of its time waiting for internal events – use multiprocessing
#  io bound = program/tas spend most of its time waiting for external events. – Use multithreading


import threading
import time

def eat_breakfast():
    time.sleep(1)
    print("You have eat breakfast")

def drink_coffee():
    time.sleep(2)
    print("You have drank coffee")


def study():
    time.sleep(3)
    print("You finished studing")

print(threading.active_count())
print(threading.enumerate())
print(time.perf_counter())

x = threading.Thread(target=eat_breakfast, args=())
x.start()

y = threading.Thread(target=drink_coffee, args=())
y.start()

z = threading.Thread(target=study, args=())
z.start()

# eat_breakfast()
# drink_coffee()
# study()

print(threading.active_count())
print(threading.enumerate())
x.join()
y.join()
z.join()
print()
print("Now you have finished your morning routine!")

#Daemon threading
# They stay alive until all non daemon threads are finished.
def timer():
    print()
    count = 0
    while True:
        time.sleep(1)
        count += 1
        print("Logged in for: {} seconds".format(count))
w = threading.Thread(target=timer(), daemon=True)
w.start()
w.daemon(True)
#w.isDaemon()
answer = input("Do you wish to exit?")