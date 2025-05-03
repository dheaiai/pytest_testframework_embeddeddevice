from threading import Thread

def run_in_thread(func, *args):
    thread = Thread(target=func, args=args)
    thread.start()
    return thread
