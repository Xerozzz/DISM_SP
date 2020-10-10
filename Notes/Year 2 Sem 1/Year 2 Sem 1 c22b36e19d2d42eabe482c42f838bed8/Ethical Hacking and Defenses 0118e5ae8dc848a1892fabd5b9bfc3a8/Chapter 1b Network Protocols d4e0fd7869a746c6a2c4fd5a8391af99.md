# Chapter 1b: Network Protocols

# Learning Outcomes

- Remote Desktop
- Address Resolution Protocol (ARP)
- Domain Name System (DNS)
- Simple Network Management System (SNMP)
- Basic Ping Sweeps and Port Scans
- Banner Grabbing

---

# Remote Desktops

- Allows a computer's desktop environment to be viewed or controlled remotely
- Used by IT Support to troubleshoot computer problems
- Can also be used by hackers impersonating IT support staff and getting users to allow remote desktop access

## Remote Access Trojan (RAT)

- Malware that allows a hacker to control a computer remotely

## Remote Desktop Software

- TeamViewer
- TightVNC
- Remote Desktop Services by Microsoft

## Remote Desktop Services

- Microsoft's Remote Desktop Connection
- Allows users to connect remotely to Windows system
- Runs of TCP Port 3389
- Use network level authentication for more security

---

# Address Resolution Protocol (ARP)

- For a device to send a packet to another device on the same local network, it needs the MAC address of the destination
- ARP is the protocol used to find the MAC address

## To Find MAC Address from IP Address

- Sender looks at its ARP table
- If the IP Address not listed in ARP table, the sender will send an ARP broadcast to all devices in the local network to ask who hast htat IP Address
- The device with the IP address will send an ARP reply to the sender with its MAC Address
- Sender will send the packet to this MAC address and update its ARP table in case it is required again

## ARP Poisoning/Spoofing

- Attacker can poison victim's ARP table and cause devices to send packets to him instead of original recipient
- Attacker replies ARP broadcast with his own MAC address before original recipient can reply
- Sender records wrong MAC address in its ARP table and sends packets meant for original recipient to attacker instead

---

# Domain Name System (DNS)

- DNS resolves domain names to their IP addresses
- DNS Servers contain a database of domain names mapped to IP addresses

## DNS Poisoning/Spoofing

- Attacker can edit the DNS database or DNS cache to direct users to his own website
- Proper configuration of DNS can reduce risks of such attacks

![Chapter%201b%20Network%20Protocols%20d4e0fd7869a746c6a2c4fd5a8391af99/Untitled.png](Chapter%201b%20Network%20Protocols%20d4e0fd7869a746c6a2c4fd5a8391af99/Untitled.png)

---

# Simple Network Management Protocol (SNMP)

- For remote monitoring and management of network nodes
- SNMP Manager monitors a set of SNMP agents installed on network nodes
- Can check performance and make changes in configuration of monitored nodes
- SNMP Agent can send warning to SNMP manager of unusual situations

---

# Ping Sweeps

- Sends ping packets to a range of IP addresses to see which system will reply
- Can be used to see which system is alive
- Known as an ICMP sweep

---

# NMAP

- To test if a port is opened, a SYN packet can be sent to the port
- If a SYN/ACK packet is returned, the port is opened

---

# Banner Grabbing

- Many services return information like version number when a client connects to it
- Banner grabbing is a method hackers can use to find more information about a running service
- Usually telnet or netcat is used to do banner grabbing

![Chapter%201b%20Network%20Protocols%20d4e0fd7869a746c6a2c4fd5a8391af99/Untitled%201.png](Chapter%201b%20Network%20Protocols%20d4e0fd7869a746c6a2c4fd5a8391af99/Untitled%201.png)