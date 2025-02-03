import socket 
import ipadress

def is_port_open(host,port):
    """Check if a port is open on the give host."""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5) 
        result = sock.connect_ex((host,port))
        sock.close()
        return result == 0
    except socket.error:
        return False

def scan_host(host,ports):
    """Scan a host for open ports."""
    print(f"Scanning {host}")
    for port in ports:
        if is_port_open(host,port):
            print(f"Port {port} is open on {host}")
            
        

def scan_network(network,Ports):
    """Scan a network for active host and open ports"""
    for ip in ipaddress.IPv4Network(network):
        scan_host(str(ip),ports)

network = " "

ports_to_scan = []

scan_network(network,ports_to_scan)
