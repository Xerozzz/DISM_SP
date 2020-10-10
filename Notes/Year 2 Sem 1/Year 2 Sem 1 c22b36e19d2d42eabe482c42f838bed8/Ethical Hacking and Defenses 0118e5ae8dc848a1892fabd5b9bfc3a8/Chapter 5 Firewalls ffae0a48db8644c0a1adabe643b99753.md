# Chapter 5: Firewalls

# Learning Outcome

- Understand NAT
- Understand the use of proxy servers
- The Demilitarized Zone (DMZ), Bastion Hosts and Honeypots
- Explain what firewalls can and cannot do
- Describe common approaches to packet filtering
- Establish a set of rules and restriction for a firewall
- Explore common firewall configurations
- Compare hardware and software firewalls

---

# Network Address Translation

## Definition

- A network device hides its internal IP address from the outside world
- A public IP address is presented to outside world

## Why NAT?

- Reduces the number of public IP addresses required by an organization
- Hundreds or even thousands of internal computers can be behind a single public IP address
- Internal IP addresses are hidden from outside attackers

## How does NAT work?

- When an internal computer wants to request a web page from a web server on the Internet, its packets goes to the NAT device first
- The NAT device will replace the source IP with its public IP address and sends the packet to the web server on the Internet
- The web server only sees the public IP address, it sends its packets back to the NAT device
- NAT device will remember which internal computer requested for the web page and sends the packet accordingly

---

# Proxy Server

## Definition

- A proxy server intercepts internal user requests and processes that request on behalf of the user
- The proxy server keeps a cache of its retrieved web pages
- Other uses requesting for the same pages can retrieve them from the Proxy Server cache
- Faster retrieval time

## What can Proxy Server do?

- Block access to undesirable websites
- Keeps log of websites accessed by users
- Proxy servers can also be used to hide IP addresses

## How Do Proxy Servers Work?

- Proxy servers prevent direct connections between external computers and internal computers
- Proxy servers work at the application level
- It examines the data in the packet and decides to which application or system to forward the packet to
- It reconstructs the packet and forwards it and replaces the original header with a new header containing the proxy's own IP address

![Chapter%205%20Firewalls%20ffae0a48db8644c0a1adabe643b99753/Untitled.png](Chapter%205%20Firewalls%20ffae0a48db8644c0a1adabe643b99753/Untitled.png)

## How To Connect To Proxy Servers

### Client Programs

- Configured to connect to the Proxy server instead of the Internet

### Transparent Proxy Servers

- Do not require the client to be specially configured

## Advantages and Disadvantages of Proxy Servers

![Chapter%205%20Firewalls%20ffae0a48db8644c0a1adabe643b99753/Untitled%201.png](Chapter%205%20Firewalls%20ffae0a48db8644c0a1adabe643b99753/Untitled%201.png)

## Choosing a Proxy Server

### Freeware Proxy Server

- Often described as content filters
- May not have advanced features
- Eg. Squid

### Commercial Proxy Server

- Offer web page caching, source and destination IP addresses translation, content filtering and NAT
- Eg. Many hardware firewalls come with proxy server functionality

## Reverse Proxy

- Used to help the web server
- Offloads some of the load on the web server by caching static web content
- Can perform load balancing among multiple web servers
- Can handle the SSL encryption, freeing the web servers

![Chapter%205%20Firewalls%20ffae0a48db8644c0a1adabe643b99753/Untitled%202.png](Chapter%205%20Firewalls%20ffae0a48db8644c0a1adabe643b99753/Untitled%202.png)

![Chapter%205%20Firewalls%20ffae0a48db8644c0a1adabe643b99753/Untitled%203.png](Chapter%205%20Firewalls%20ffae0a48db8644c0a1adabe643b99753/Untitled%203.png)

---

## Demilitarized Zone (DMZ)

- Normally all internal computers are kept inaccessible from the Internet
- But public users will need to access some internal resources like web servers
- The DMZ is a section of the network that is visible to the outside world
- Public users can access the DMZ but cannot enter the internal secured network
- May also be called a service network or perimeter network

![Chapter%205%20Firewalls%20ffae0a48db8644c0a1adabe643b99753/Untitled%204.png](Chapter%205%20Firewalls%20ffae0a48db8644c0a1adabe643b99753/Untitled%204.png)

## Bastion Host

- Normally refers to a computer that has been specially protected through OS patches, authentication, encryption etc
- Such specially secured computers are usually those at the network perimeter in the DMZ
- Usually provides Web, FTP, email or other services typically running on a specially secured server

![Chapter%205%20Firewalls%20ffae0a48db8644c0a1adabe643b99753/Untitled%205.png](Chapter%205%20Firewalls%20ffae0a48db8644c0a1adabe643b99753/Untitled%205.png)

## Honeypot

- Computer placed on network perimeter
- Attracts attackers away from real and critical servers
- Used to log attacker techniques so you can learn about it
- Legal issues, what if the attacker uses your purposely unsecured honeypot pot to harm other networks?

![Chapter%205%20Firewalls%20ffae0a48db8644c0a1adabe643b99753/Untitled%206.png](Chapter%205%20Firewalls%20ffae0a48db8644c0a1adabe643b99753/Untitled%206.png)

---

# Firewalls

## Overview

- Hardware or software
- To block unauthorized network access
- Earliest firewalls were packet filters

## Firewall Rules

- Configured by setting rule
- Rules for block traffic can be done case-by-case
    - Allow traffic
    - Block traffic
    - Customize access

## What Firewalls Can't Do

![Chapter%205%20Firewalls%20ffae0a48db8644c0a1adabe643b99753/Untitled%207.png](Chapter%205%20Firewalls%20ffae0a48db8644c0a1adabe643b99753/Untitled%207.png)

## Firewalls Are Not A Standalone Solution

- Firewalls cannot protect against internal threats
- Need strong security policy and employee education
- Firewalls must be combined with other security solutions like antivirus software and IDS

## Packet Filtering

- Only info in packet headers are checked
- Data in packet not checked

### Stateless Packet Filtering

- Decides whether to block or allow packets based on information only in protocol headers
- Filtering based on common IP header features
    - IP Addresses and Ports
    - Protocols
    - Flags and Options
- Advantage: Inexpensive and fast
- Disadvantage: Attackers nowadays are more complicated

![Chapter%205%20Firewalls%20ffae0a48db8644c0a1adabe643b99753/Untitled%208.png](Chapter%205%20Firewalls%20ffae0a48db8644c0a1adabe643b99753/Untitled%208.png)

### Stateful Packet Filtering

- Besides looking at information in protocol headers, keeps a record of connections the host computer has made with other computers
- Maintain a file called a state table containing a record of all current connections
- Allows incoming packets to pass through only from external hosts already connected

![Chapter%205%20Firewalls%20ffae0a48db8644c0a1adabe643b99753/Untitled%209.png](Chapter%205%20Firewalls%20ffae0a48db8644c0a1adabe643b99753/Untitled%209.png)

### Typical Locations of Packet Filters

- Between Internet and internal network
- Between proxy server and Internet
- At either end of DMZ

![Chapter%205%20Firewalls%20ffae0a48db8644c0a1adabe643b99753/Untitled%2010.png](Chapter%205%20Firewalls%20ffae0a48db8644c0a1adabe643b99753/Untitled%2010.png)

![Chapter%205%20Firewalls%20ffae0a48db8644c0a1adabe643b99753/Untitled%2011.png](Chapter%205%20Firewalls%20ffae0a48db8644c0a1adabe643b99753/Untitled%2011.png)

## Application Layer Firewall

- Inspects both header and data portions of packets
- Also known as content filtering
- Checks for malicious code contains in the packet data
- Combination of packet filters and application layer firewalls can be used in a network

## Configuring Firewall Rules

### Rule Base

- Tells firewalls what to do when a certain kind of traffic attempts to come
- Keep it short and simple to perform faster
- Firewalls process rules in an order from top to down
- Put more important and frequently used rules at the top
- Make the last rule a cleanup/catch-all rule (Any, Any, Any, Deny)

    ![Chapter%205%20Firewalls%20ffae0a48db8644c0a1adabe643b99753/Untitled%2012.png](Chapter%205%20Firewalls%20ffae0a48db8644c0a1adabe643b99753/Untitled%2012.png)

### Points To Consider

- Based on organization's security policy
- Determine what can be accessed from external network
- Logging and auditing requirements
- Network Address Translation (NAT) if used
- Simple and short as possible, firewall should not cause delay in network speed and be easy to maintain

### Common Security Policies

- Employees have access to Internet with no restrictions
- Public can access company's Web and Email server
- Only authenticated traffic can access the internal LAN
- Employees are not allowed to use instant-messaging
- Traffic from the company's ISP should be allowed
- Block external traffic by instant-messaging software
- Only network administrator should be able to access internal network directly from the Internet

### General Practices

- Most frequently matched rules should be near the top of the rule base for faster processing
- Nobody can connect to firewall except adminstrator
- Block direct access from the Internet to any computer behind the firewall
- Permit access to public services in DMZ

![Chapter%205%20Firewalls%20ffae0a48db8644c0a1adabe643b99753/Untitled%2013.png](Chapter%205%20Firewalls%20ffae0a48db8644c0a1adabe643b99753/Untitled%2013.png)

![Chapter%205%20Firewalls%20ffae0a48db8644c0a1adabe643b99753/Untitled%2014.png](Chapter%205%20Firewalls%20ffae0a48db8644c0a1adabe643b99753/Untitled%2014.png)

## Anti-Spoofing Rule

- The first rule is usually this rule
- Blocks packets coming from outside network pretending to be an internal system

## Firewall Rule Matching

- Firewalls with numbered rules match packets to rules in number order
- Some firewalls match deny first then match allow
- Windows lets block rule take precedence over allow

## Firewall Log

- Decide what to log
- Most firewalls generate logs in plain text files
- Sophisticated firewalls can save log files in other formats like excel or html
- Review log files regularly as it can indicate signatures of attack attempts
- Prepare log file summaries to generate reports
    - Show major events over a period of time
    - Contain raw data used to create reports
    - Some firewalls contain log file analysis tools
    - Reports display data in an easy-to-read format

## Ways To Deploy Firewall

### Screening Router

- Determines whether to allow or deny packets based on their source and destination IP address or other header information
- Does not stop many attacks especially spoofed or manipulated IP address information
- Should be combined with firewall or proxy server for additional protection

![Chapter%205%20Firewalls%20ffae0a48db8644c0a1adabe643b99753/Untitled%2015.png](Chapter%205%20Firewalls%20ffae0a48db8644c0a1adabe643b99753/Untitled%2015.png)

### Dual-Homed Host

- Computer that has been configured with more than one network interface
- Firewall software forwards packets from one network interface to another
- Provides limited security
- Host serves as a point of entry to the organization

![Chapter%205%20Firewalls%20ffae0a48db8644c0a1adabe643b99753/Untitled%2016.png](Chapter%205%20Firewalls%20ffae0a48db8644c0a1adabe643b99753/Untitled%2016.png)

### Screened Host

- Similar to a dual-homed host
- Adds a router between host and the internet to carry out IP packet filtering
- Combines a dual-homed host and screening router
- Can function as a gateway or proxy server

![Chapter%205%20Firewalls%20ffae0a48db8644c0a1adabe643b99753/Untitled%2017.png](Chapter%205%20Firewalls%20ffae0a48db8644c0a1adabe643b99753/Untitled%2017.png)

### Screened Subnet DMZ

- Firewall that protects the DMZ connected to the Internet and LAN
- Called a three-pronged firewall

![Chapter%205%20Firewalls%20ffae0a48db8644c0a1adabe643b99753/Untitled%2018.png](Chapter%205%20Firewalls%20ffae0a48db8644c0a1adabe643b99753/Untitled%2018.png)

### Multiple DMZ Firewall Configurations

- Server farm
    - Group of servers connected in their own subnet
    - Work together to receive requests with the help of load-balancing software
- Clusters of servers in DMZs help protect the network from being overloaded
- Each server farm/DMZ protected with its own firewall or packet filter

![Chapter%205%20Firewalls%20ffae0a48db8644c0a1adabe643b99753/Untitled%2019.png](Chapter%205%20Firewalls%20ffae0a48db8644c0a1adabe643b99753/Untitled%2019.png)

### Multiple Firewall Configurations

- Protecting a DMZ with two or more firewalls
- One firewall controls traffic between DMZ and Internet
- Second Firewall controls traffic between internal LAN and DMZ
- Advantage: Can control where traffic goes in the 3 networks you are dealing with
- Protecting branches offices with multiple firewalls while central office has a centralized firewall
    - Directs traffic for branch offices and their firewalls
    - Deploys security policy through this firewall using a security workstation

        ![Chapter%205%20Firewalls%20ffae0a48db8644c0a1adabe643b99753/Untitled%2020.png](Chapter%205%20Firewalls%20ffae0a48db8644c0a1adabe643b99753/Untitled%2020.png)

- Additional firewall placed inside internal network to protect network management systems
    - Extra level of protection
    - Intruders cannot gain control of network management system

    ![Chapter%205%20Firewalls%20ffae0a48db8644c0a1adabe643b99753/Untitled%2021.png](Chapter%205%20Firewalls%20ffae0a48db8644c0a1adabe643b99753/Untitled%2021.png)

### Summary

![Chapter%205%20Firewalls%20ffae0a48db8644c0a1adabe643b99753/Untitled%2022.png](Chapter%205%20Firewalls%20ffae0a48db8644c0a1adabe643b99753/Untitled%2022.png)

## Other Types of Firewalls

### Software-Based Firewall

- Free firewall programs
- Commercial firewall programs for personal use
- Commercial firewall programs for enterprise use
- Capable of managing multiple instances from a centralized location

### Hardware Firewalls

- Also called firewall appliances
- Advantages
    - Do not depend on conventional OSs
    - Generally more scalable than software firewalls
- Disadvantages
    - They do depend on nonconventional OSs
    - Tend to be more expensive than software

### Hybrid Firewalls

- Combines aspects of hardware and software firewalls
- Benefits from the strengths of both solutions

![Chapter%205%20Firewalls%20ffae0a48db8644c0a1adabe643b99753/Untitled%2023.png](Chapter%205%20Firewalls%20ffae0a48db8644c0a1adabe643b99753/Untitled%2023.png)