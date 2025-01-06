import re
import subprocess
import networkx as nx
import matplotlib.pyplot as plt
import concurrent.futures
import tempfile
import os

def scan_network(ip):
    try:
        result = subprocess.run(['nmap', '-sn', f'{ip}/24'], stdout=subprocess.PIPE)
        output = result.stdout.decode()
        ips = re.findall(r'Nmap scan report for ([\w.-]+) \(([\d.]+)\)', output)
        ips_list = [ip[1] for ip in ips]
        return ips_list
    except Exception as e:
        print(f"Error scanning network: {e}")
        return []

def create_data(network_ips, start_ip):
    ip_map_dict = {}
    ip_map_dict[start_ip] = network_ips

    def process_ip(ip):
        return ip, scan_network(ip)

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(process_ip, ip) for ip in network_ips]
        for future in concurrent.futures.as_completed(futures):
            ip, ips = future.result()
            ip_map_dict[ip] = ips

    return ip_map_dict

def create_network_graph(start_ip, ip_map_dict):
    G = nx.Graph()
    already_connected = set()

    for source_ip, target_ips in ip_map_dict.items():
        if source_ip == start_ip:
            G.add_node(source_ip, label=f"Start IP\n{source_ip}")
        else:
            G.add_node(source_ip, label=f"{source_ip}")

        for target_ip in target_ips:
            if target_ip == start_ip:
                G.add_node(target_ip, label=f"Start IP\n{target_ip}")
            else:
                G.add_node(target_ip, label=f"{target_ip}")
            
            if (source_ip, target_ip) not in already_connected and (target_ip, source_ip) not in already_connected:
                G.add_edge(source_ip, target_ip)
                already_connected.add((source_ip, target_ip))
                already_connected.add((target_ip, source_ip))

    return G

def draw_network_graph(G, filename, figsize=(10, 6)):
    pos = nx.spring_layout(G)
    
    plt.figure(figsize=figsize)
    nx.draw(G, pos, with_labels=True, node_size=1000, node_color='skyblue', font_size=7, font_color='black')
    
    plt.title("Network Diagram")
    plt.savefig(filename, bbox_inches='tight')
    plt.close()

def create_and_save_network_map(start_ip):
    try:
        network_ips = scan_network(start_ip)
        ip_map_dict = create_data(network_ips, start_ip)
        G = create_network_graph(start_ip, ip_map_dict)
        
        temp_dir = tempfile.gettempdir()
        image_path = os.path.join(temp_dir, 'network_graph.png')
        draw_network_graph(G, image_path)
        
        return image_path
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

