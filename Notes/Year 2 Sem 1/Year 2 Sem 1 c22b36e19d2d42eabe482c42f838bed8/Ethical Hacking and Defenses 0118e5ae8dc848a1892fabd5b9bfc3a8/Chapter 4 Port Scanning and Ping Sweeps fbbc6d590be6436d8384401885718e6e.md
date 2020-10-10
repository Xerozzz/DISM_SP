# Chapter 4: Port Scanning and Ping Sweeps

# Learning Outcome

- Describe port scanning
- Describe different types of port scans
- Explain what ping sweeps are used for

---

# Introduction to Port Scanning

## Port Scanning

- Finds out what services are offered by a host
- Identifies vulnerabilities

## Open Services can be used in attacks

- Identify a vulnerable port
- Launch an exploit

## Scan all ports when testing

- Not just well known ports
- UDP And TCP ports range from 0 to 65535

## Port Scanning can report

- Open ports
- Closed ports (Not blocked by firewall but not running any service)
- Filtered ports (possible behind a firewall
- Best-guess assessment of which OS is running

## Port Scanning Tools

### Nmap

- Command-line tool
- GUI version called Zenmap
- Open source tool for security professionals

### Others

- Unicornscan
- Nessus

# NMAP

## Types of NMAP Port Scans

### SYN Scan

- SYN packet is sent to victim
- If port is open, SYN/ACK returned to attacker and RST is returned to victim
- If closed, RST returned
- Quieter and more stealthy option than TCP connect as TCP 3 way handshake not completed, so connection is not logged

### TCP Connect Scan

- If port is open, full 3 way TCP Handshake is established
- If port closed, RST is returned

### FIN, XMAS and NULL Scans

- FIN Scan only sends packets with FIN flag
- XMAS Scan only sends packets with FIN, PSH and URG flags
- Null scan sends packets with no flags on, by right cannot exist
- If port open, nothing returned, if closed, RST returned
- Also known as stealth scans as only 1 packet is sent and returned
- Need to use other scans to confirm observation
- 3 problems with these scans
    - If firewall blocks the port, no reply is received so it can be open or filtered
    - Different OS may respond differently than others

### ACK Scan

- Only reply "filtered" or "unfiltered"
- Used for traversing through firewall
- If no response, firewall MAY be present (filtered), if RST received, there is no firewall or the firewall allowed ACK packet through (RARELY)

### Default NMAP Ports Scanned

- Determines most common 1000 ports in /usr/share/nmap/nmap-services file
- NMAP by default only scans the most common 1000 ports for each protocols
- Can use -p to specify your own port

## NMAP Syntax

![Chapter%204%20Port%20Scanning%20and%20Ping%20Sweeps%20fbbc6d590be6436d8384401885718e6e/Untitled.png](Chapter%204%20Port%20Scanning%20and%20Ping%20Sweeps%20fbbc6d590be6436d8384401885718e6e/Untitled.png)

## Avoiding Detection

- Port scans are usually noisy and can generate a lot of traffic suddenly and can slow down network
- Attacks may try to avoid sending large number of packets in a short burst of time

### Scan Throttling

- Delay the progression of a scan over hours, days and even weeks
- Eg. One SYN packet sent to one port once every 30 mins, makes it harder to detect

### NMAP Options for Timing

- --scan-delay *<number of seconds between probes>*
- --max-rate *<number of packets per second>*
- -T *2* or -T *polite* to slow down the scan
- -T *3* or -T *normal* to scan at normal speeds
- -T *4* or -T a*ggressive* to speed up the scan

## Host Discovery in NMAP

- By default, NMAP will try to discover if the host is alive before scanning ports
- NMAP uses an ARP Broadcast to check this

### NMAP Options for Host Discovery

- -sn Do host discovery only, no port scan
- -Pn Do port scanning only and no host discovery

# Unicornscan

- Ideals for large networks
- Handles port scnaning using TCP, ICMP and IP
- Optimizes UDP Scanning
- Unix-Based

# Ping Sweeps for Host Discovery

## Definition

- Identify which IP addresses belong to active hosts
- Ping a range of IP addresses

## Problems

- Computers that are shut down cannot respond
- Networks may be configured to block ICMP Echo Requests
- Firewalls may filter out ICMP traffic

## Fping

- Ping multiple IP addresses at the same time
- Command-line tool
- -g for range in CLI
- -f for input file with addresses
- Same as nmap -sP

![Chapter%204%20Port%20Scanning%20and%20Ping%20Sweeps%20fbbc6d590be6436d8384401885718e6e/Untitled%201.png](Chapter%204%20Port%20Scanning%20and%20Ping%20Sweeps%20fbbc6d590be6436d8384401885718e6e/Untitled%201.png)

## ARP Broadcasts

- Send ARP Broadcast requests for a range of IP addresses to see which hosts reply
- Can only discover hosts on same network
- Same as using Nmap -sn

## Hping

- Used to bypass filtering devices and allows users to fragment and manipulate IP packets
- Powerful tool and supports many parameters

![Chapter%204%20Port%20Scanning%20and%20Ping%20Sweeps%20fbbc6d590be6436d8384401885718e6e/Untitled%202.png](Chapter%204%20Port%20Scanning%20and%20Ping%20Sweeps%20fbbc6d590be6436d8384401885718e6e/Untitled%202.png)

![Chapter%204%20Port%20Scanning%20and%20Ping%20Sweeps%20fbbc6d590be6436d8384401885718e6e/Untitled%203.png](Chapter%204%20Port%20Scanning%20and%20Ping%20Sweeps%20fbbc6d590be6436d8384401885718e6e/Untitled%203.png)

![Chapter%204%20Port%20Scanning%20and%20Ping%20Sweeps%20fbbc6d590be6436d8384401885718e6e/Untitled%204.png](Chapter%204%20Port%20Scanning%20and%20Ping%20Sweeps%20fbbc6d590be6436d8384401885718e6e/Untitled%204.png)