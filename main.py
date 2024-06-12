from port_scanner.scanner import PortScanner
from port_scanner.utils import parse_arguments

def main():
    target, start_port, end_port, num_threads = parse_arguments()
    
    scanner = PortScanner(target, start_port, end_port, num_threads)
    open_ports = scanner.run()

    if open_ports:
        print(f"Open ports on {target}: {open_ports}")
    else:
        print(f"No open ports found on {target} in the range {start_port}-{end_port}.")

    print("Port scanning completed.")

if __name__ == "__main__":
    main()
