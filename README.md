# Remote Hardware and Network Information System
## Overview
The Remote Hardware and Network Information System is a tool designed to remotely monitor and manage hardware and network infrastructures. It allows IT administrators to securely retrieve hardware specifications and network configurations from remote devices using SSH. The system empowers users to monitor, troubleshoot, and optimize network and hardware resources, providing real-time insights into system components, network topology, and connectivity status.

## Key Features
- ### SSH Connectivity:
  Establish secure remote connections to retrieve hardware and network data.
  
- ### Hardware Information:
  Fetch CPU, memory, disk specifications, and more.
  
- ### Network Information:
  Retrieve network configurations like IP addresses, network interfaces, active connections, and ARP tables.
  
- ### Active Connections & Devices:
  List active network connections and connected devices.
  
- ### Ping Check:
  Perform and view results from a network ping test.
 
- ### Network Graph:
  Visual representation of the network topology.
  
- ### User-friendly GUI:
  Intuitive interface for easy interaction with system data.

## Technologies
- ### Python:
   The core language used for development.
- ### Libraries:
 - paramiko for SSH connections.
 - tkinter for the GUI.
 - psutil, os, and system commands for hardware and network data retrieval.
- ### SSH:
Secure access to remote systems.

## System Components
### User Interface Frames
- ### Input Frame:
  For entering SSH credentials and IP address.
  ![Screenshot (2)](https://github.com/user-attachments/assets/e2aa7ede-d57e-4086-ab0e-eb7bc7b6cc31)

- ### Hardware Frame:
  Displays fetched hardware details.
  ![Screenshot (3)](https://github.com/user-attachments/assets/834a7d30-ffa7-4d9c-ba85-d87324062fa5)

- ### Network Frame:
  Shows network-related data.
  ![Screenshot (5)](https://github.com/user-attachments/assets/0c252398-2a04-4648-ad9a-4d35e0606e72)

- ### Active Connections Frame:
  Lists active network connections.
  ![Screenshot (7)](https://github.com/user-attachments/assets/06897949-6b11-411d-8343-c130d7798ac4)

- ### Connected Devices Frame:
  Displays devices connected to the network.
  ![Screenshot (8)](https://github.com/user-attachments/assets/0b3589e9-424b-4ca4-af44-c2e7ea4c9652)

- ### Ping Check Frame:
  Shows ping test results.
  ![Screenshot (9)](https://github.com/user-attachments/assets/f28a138c-8449-4b20-a286-51758525e1b0)

- ### Network Graph Frame:
  Visual representation of network topology.
  ![Screenshot (6)](https://github.com/user-attachments/assets/d9428a92-df14-4ea1-9172-6c83c444e928)

## Project Workflow
- ### Input Collection: 
Users provide the remote machine's credentials and IP address.

- ### SSH Connection: 
The system establishes a secure SSH connection.

- ### Hardware Information Retrieval: 
Remote commands fetch CPU, memory, and disk specs.

- ### Network Information Retrieval: 
Commands gather network details like IP, interfaces, active connections, and ARP.

- ### Network Graph Generation: 
A visual graph of the network layout is generated.

- ### User Interaction: 
Simple navigation through frames with error handling and feedback.

## Conclusion
The Remote Hardware and Network Information System provides a comprehensive, easy-to-use tool for administrators to remotely monitor and manage system hardware and network infrastructure. The tool includes features like hardware and network information retrieval, active connection monitoring, device listing, and network graph visualization, all accessible through a simple and intuitive GUI.
