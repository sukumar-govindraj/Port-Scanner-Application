import socket
from queue import Queue
from tqdm import tqdm
import threading

class PortScanner:
    def __init__(self, target, start_port, end_port, num_threads):
        self.target = target
        self.start_port = start_port
        self.end_port = end_port
        self.num_threads = num_threads
        self.queue = Queue()
        self.open_ports = []

    def port_scan(self, port, progress_bar):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((self.target, port))
            if result == 0:
                self.open_ports.append(port)
            sock.close()
        except socket.error:
            pass
        finally:
            progress_bar.update(1)

    def worker(self, progress_bar):
        while not self.queue.empty():
            port = self.queue.get()
            self.port_scan(port, progress_bar)
            self.queue.task_done()

    def run(self):
        for port in range(self.start_port, self.end_port + 1):
            self.queue.put(port)

        progress_bar = tqdm(total=self.queue.qsize(), desc="Scanning Ports", unit="port")

        threads = []
        for _ in range(self.num_threads):
            thread = threading.Thread(target=self.worker, args=(progress_bar,))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

        progress_bar.close()

        return sorted(self.open_ports)
