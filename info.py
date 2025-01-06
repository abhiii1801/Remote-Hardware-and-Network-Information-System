import paramiko

def get_hardware_info_via_ssh(ip, username, password):
    try:
        # Create an SSH client
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # Connect to the server
        client.connect(ip, username=username, password=password)

        # Commands to fetch hardware information
        commands = [
            'systeminfo',
            'wmic diskdrive get Model,Size',
            'wmic cpu get Name'
        ]

        hardware_info = {}

        for command in commands:
            stdin, stdout, stderr = client.exec_command(command)
            output = stdout.read().decode().strip()  # Read and decode output
            hardware_info[command] = output

        info_dict = {}

        lines = hardware_info['systeminfo'].strip().split("\n")

        # Parse each line and add to dictionary
        for line in lines:
            if ':' in line:
                key, value = line.split(':', 1)  # Split only once
                key = key.strip()  # Remove leading/trailing whitespace
                value = value.strip()  # Remove leading/trailing whitespace
                info_dict[key] = value

        lines2 = hardware_info['wmic diskdrive get Model,Size'].strip().splitlines()
        drive_dict = {}

        # Process each line and create key-value pairs in the dictionary
        for line in lines2[1:]:
            parts = line.split()
            if len(parts) >= 2:
                model = " ".join(parts[:-1])  # Join all parts except the last one as model
                size = parts[-1]         # Convert the last part to an integer (assuming size is in bytes)
                drive_dict[model] = size      # Store in dictionary

        info_dict['Storage Info'] = drive_dict
        
        lines3 = hardware_info['wmic cpu get Name'].strip().splitlines()[-1]
        
        info_dict['Processor Name'] = lines3

        client.close()
        return info_dict

    except paramiko.AuthenticationException as auth_error:
        print(f"Authentication failed: {auth_error}")
    except paramiko.SSHException as ssh_error:
        print(f"SSH connection failed: {ssh_error}")

def get_network_info_via_ssh(ip, username, password):
    try:
        # Create an SSH client
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # Connect to the server
        client.connect(ip, username=username, password=password)

        # Commands to fetch hardware information
        ping_cmd = f'ping {ip}'
        commands = [
            'ipconfig',
            'netstat -n',
            'arp -a',
            ping_cmd
        ]

        hardware_info = {}

        for command in commands:
            stdin, stdout, stderr = client.exec_command(command)
            output = stdout.read().decode().strip()  # Read and decode output
            hardware_info[command] = output

        network_dict = {}

        # Split the string into lines and process each line
        lines = hardware_info['ipconfig'].strip().splitlines()
        for line in lines:
            # Look for lines containing IPv4 Address, Subnet Mask, and Default Gateway
            if "IPv4 Address" in line:
                parts = line.split(':')
                if len(parts) == 2:
                    key = parts[0].strip()
                    value = parts[1].strip()
                    network_dict[key] = value
            elif "Subnet Mask" in line:
                parts = line.split(':')
                if len(parts) == 2:
                    key = parts[0].strip()
                    value = parts[1].strip()
                    network_dict[key] = value
            elif "Default Gateway" in line:
                parts = line.split(':')
                if len(parts) == 2:
                    key = parts[0].strip()
                    value = parts[1].strip()
                    network_dict[key] = value


        lines2 = hardware_info['netstat -n'].strip().splitlines()
        netstat_list = []

        for line in lines2[3:]:
            # Split each line by whitespace and filter out empty strings
            fields = line.split()
            if fields:
                netstat_list.append(fields)
    
        lines3 = hardware_info['arp -a'].strip().splitlines()
        arp_list = []

        for line in lines3[2:]:
            fields = line.split()
            if fields:
                arp_list.append(fields)


        return network_dict, netstat_list, arp_list, hardware_info[ping_cmd]
        

    except paramiko.AuthenticationException as auth_error:
        print(f"Authentication failed: {auth_error}")
    except paramiko.SSHException as ssh_error:
        print(f"SSH connection failed: {ssh_error}")
