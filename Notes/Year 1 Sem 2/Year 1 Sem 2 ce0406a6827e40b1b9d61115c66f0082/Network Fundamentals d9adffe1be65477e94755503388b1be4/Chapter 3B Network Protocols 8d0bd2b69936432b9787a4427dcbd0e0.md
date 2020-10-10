# Chapter 3B: Network Protocols

Created: Jan 28, 2020 7:07 PM
Updated: Jan 28, 2020 8:01 PM

**Objectives:**

- Describe Telnet and Secure Shell (SSH)
- Describe Simple Mail Transfer Protocol (SMTP)
- Describe Post Office Protocol (POP3)
- Describe Address Resolution Protocol (ARP)
- Describe Domain Name System (DNS)
- Describe Simple Network Management Protocol (SNMP)
- Describe Basic Ping sweeps and Port Scans
- Describe Banner Grabbing

**Telnet:**

- Allows a user to login remotely to another system
- Runs on Port 23
- Old protocol with no encryption
- SSH more secure now

**Secure Shell (SSH):**

- Popular application used for remote login
- Runs on Port 22
- Data sent is encrypted across the network

**Email Protocol:**

Simple Mail Transfer Protocol (SMTP):

- Used to transmit emails from one Mail Server to another
- From mail client to mail server
- Eg. Mail Server in ABC school sends to mail server in XYZ school

Post Office Protocol (POP3):

- Emails usually stored on the Mail Server
- Users use their own client computers to retrieve their emails from the Mail Server
- POP3 is used to retrieve these emails
- POP3S - Secured Version

Internet Message Access Protocol (IMAP4):

- Alternative to POP3
- IMAPS - Secured Version

**Address Resolution Protocol (ARP):**

Details:

- When a device sends a packet, it looks at the destination IP address
- If destination IP address is not local, the device will send packet to gateway
- If destination IP address is local, the device will send the packet to the destination
- To send the packet to local network, sender will require destination MAC address

To find MAC Address:

- Sender looks in its ARP table
- If IP address not listed in ARP table, sender will not send an ARP broadcast to all devices in the local network to ask who has that IP address
- Device with IP address will send an ARP reply to the sender with its MAC address
- sender will send the packet to this MAC address
- Sender will update its ARP table with this MAC address in case it is needed again

ARP Poisoning/Spoofing:

- Attacker can cause devices to send packets intended for others to him instead
- When sender asks for receiver's MAC address, attacker sends his own first
- Packet addressed to receiver goes to attacker instead

**Domain Name System (DNS):**

Details:

- DNS servers translate fully qualified domain names into IP addresses

    DNS is a distributed database system running on the Internet

- Each domain would have one or more DNS Servers in charge of it
- DNS Servers contain a database that holds a section of domain names mapped to IP addresses

How it works:

- User browses to [www.yahoo.com](http://www.yahoo.com/)
- Client sends a DNS query to local DNS server
- DNS Server may contact other DNS Servers around the world to get the IP Address of the domain name
- Once it has the IP address, DNS server returns results to client
- DNS Sever may keep the IP address in its cache

DNS Poisoning/Spoofing:

- Attacker can edit DNS database or cache to direct users to his own website instead

**Simple Network Management Protocol (SNMP):**

- Allows remote monitoring and management of network nodes
- SNMP manager monitors a set of SNMP agents installed on network nodes
    - Checks performance of monitored nodes
    - Makes changes in configuration of monitored nodes
- SNMP agent can send warning to SNMP manager of unusual situations

**Ping Sweeps:**

- Ping sweep sends ping packets to a range of IP addresses to see which system will reply
- Used to see which system is alive
- Also know as ICMP sweep

**Basic Port Scan:**

- When you send a SYN packet to a web server running on Port 80, it sends back a SYN/ACK packet as part of the 3-way handshake
- If Port 80 closed, no packet sent back
- Firewalls can be configured to block such port scans

**Banner Grabbing:**

- Many services return information like version number when a client connects to it
- Banner grabbing is used to find more information about a running service
- Usually telnet or netcat used to do banner grabbing