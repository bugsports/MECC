# Port Scanner with Multi Threading, comments for study
import socket #https://docs.python.org/3/library/socket.html
import threading #https://docs.python.org/3/library/threading.html
from queue import Queue #https://docs.python.org/3/library/queue.html

# thread number
THREAD_N = 200
print_lock = threading.Lock()

def main():
    host = input("Enter the IP address to scan: ")
    ports = range(1,1025) # range of sockets (up to 65535 + 1)

    def port_scanner(port):
        # creates socket (IPv4, TCP connection)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try: 
            # establishes connection
            con = sock.connect((host, port))
            # prevents printing the same port
            with print_lock:
                print("Port",port,"status: open")
            # closes connection when done
            con.close()
        except:
            pass

    def threader():
        while True:
            # receives worker from the queue
            worker = q.get()
            # calls port_scanner function, using the number of workers from
            # the queue as the port number (see line 44).
            port_scanner(worker)
            # after scanner is complete, queue is emptied
            q.task_done()
            
    # stores "tasks"
    q = Queue()
            
    # creates threads
    for t in range(THREAD_N):
        # creating a thread using threader() function as target
        t = threading.Thread(target=threader)
        # causes thread to die with the main thread completes
        t.daemon = True
        # starts thread
        t.start()
    
    # assigns number of jobs to queue according to number of ports
    for worker in ports:
        q.put(worker)
    
    q.join()
    
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram exiting...")
        quit()