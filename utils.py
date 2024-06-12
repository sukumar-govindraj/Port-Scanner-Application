import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description="Simple Port Scanner")
    parser.add_argument("target", type=str, help="Target IP address or hostname")
    parser.add_argument("-p", "--ports", type=str, default="1-1024", help="Port range to scan, e.g., 1-1024")
    parser.add_argument("-t", "--threads", type=int, default=100, help="Number of threads to use")
    args = parser.parse_args()

    port_range = args.ports.split('-')
    start_port = int(port_range[0])
    end_port = int(port_range[1])

    return args.target, start_port, end_port, args.threads
