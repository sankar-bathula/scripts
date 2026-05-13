from multiprocessing import Process

def task():
    print("Running process")

p = Process(target=task)
p.start()
p.join()