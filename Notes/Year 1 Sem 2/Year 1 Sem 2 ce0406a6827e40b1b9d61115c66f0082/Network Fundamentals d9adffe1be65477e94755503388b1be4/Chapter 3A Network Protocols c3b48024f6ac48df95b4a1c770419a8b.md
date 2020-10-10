# Chapter 3A: Network Protocols

Created: Jan 30, 2020 12:16 AM
Updated: Feb 16, 2020 10:51 AM

**Objectives:**

- Define what are network protocols
- Explain IPv4 and Ipv6 addressing
- Describe packets
- Describe ICMP protocol
- Describe TCP protocol and 3-way handshake
- Describe Hypertext Transfer Protocol (HTTP)
- Ports
- Describe File Transfer Protocol (FTP)

**What are Network Protocols?:**

- Communication between people need to follow some protocol
- Communication between device also follow protocols, called network protocols
- Network protocols set out rules on how devices communicate with one another

**TCP/IP Layered Architecture:**

- User goes to web browser and goes to [http://www.cengage.com](http://www.cengage.com/)
- The web browser formats a request for your home page by using the Application layer protocol HTTP
- Unit of information the Application layer works with is simply called data
- Application Layer protocol HTTP passes request down to Transport Layer Protocol TCP
- TCP adds a header to the request and passes the segment to the Internetwork Layer protocol IP
- The unit of information the Transport layer works with is called a segment
- IP places its header on the segment
- The unit of information is now called a packet
- Packet is passed down to the Network access layer, where the NIC operates
- Frame header and trailers are added
- Frame is then delivered to the network medium as bits
- The web server processes it and returns a web page

[Chapter%203A%20Network%20Protocols%20c3b48024f6ac48df95b4a1c770419a8b/untitled](Chapter%203A%20Network%20Protocols%20c3b48024f6ac48df95b4a1c770419a8b/untitled)

**MAC Address:**

- Media Access Control address
- Unique hardware physical address assigned to NICs
- Assigned by vendor of network card
- Represented as 6 groups of 2 hexadecimal digits

**Ethernet Frame (Layer 2):**

- Data Link Layer - Transmits frames between adjacent nodes
- For data travelling on Ethernet cables

[Chapter%203A%20Network%20Protocols%20c3b48024f6ac48df95b4a1c770419a8b/untitled%201](Chapter%203A%20Network%20Protocols%20c3b48024f6ac48df95b4a1c770419a8b/untitled%201)

**IP addressing v4 and v6:**

- IPv4 uses 32-bits, 4 octets addresses
- IPv6 uses 128-bit addresses, 8 chunks of 4 hex digits
- One of more consecutive zeros in IPv6 can be replaced by double colon, only once per address

[Chapter%203A%20Network%20Protocols%20c3b48024f6ac48df95b4a1c770419a8b/untitled%202](Chapter%203A%20Network%20Protocols%20c3b48024f6ac48df95b4a1c770419a8b/untitled%202)

Subnet Mask:

- IP address components
    - Network Address
    - Host Address
    - Subnet Mask
- The subnet mask determines which part of the address is for network and which part is for host
- Subnet masks can be used to divide the network into subnetworks

Loopback Address:

- Hostname "localhost" or IP "127.0.0.1" refers to local machine
- Packet addressed to the loopback never leaves the system
- Used for testing

**IP Packet (Layer 3):**

- Network Layer - Controls transmissions of packets along routers on network

**TCP and UDP (Layer 4):**

- Transport Layer - Provides transfer of data between end nodes
- TCP - Transmission Control Protocol
    - Connection-oriented
    - Monitoring receipt of frames and resends if necessary
    - Controls data flow
- UDP - User Datagram Protocol
    - Connectionless
    - Does not guarantee packets will be received
    - No flow control

TCP Flags:

- URG (Urgent)
- ACK (Acknowledge)
- PSH (Push function)
- RST (Reset function)
- SYN (synchronize sequence numbers)
- FIN (Finished)
- Request for Comments (RFC)

UDP Headers:

- UDP provides a transport service for IP
- Considered unreliable because connectionless and does not guarantee delivery
- Much faster than TCP as less overhead
- Used for broadcasting messages or for protocols that do not require the same level of service as TCP
- Attackers can also scan for open UDP services
- Common applications of UDP: DNS, DHCP, SNMP

-

**ICMP:**

- Internet Control Message Protocol
- Assists TCP/IP networks with troubleshooting communication problems
- Can tell if another host is alive through ping signal
- Firewalls and packet filters may be used to block ICMP packets

ICMP Payload:

- Echo Reply - 0
- Destination Unreachable - 3
- Destination Host Unknown - 7
- Echo Request - 8

**Time-To-Live (TTL):**

- When packets are created, the TTL is set to an initial value
- As the packet travels through the Internet, each time it passes through a router, the TTL is decremented
- When TTL reaches zero and the packet is not yet at its destination, the router discards it and sends an ICMP packet back to sender
- This prevents packet from staying on the Internet forever

Default TTLs:

- Different operating systems generally set different default TTL values for packets that they send
- By looking at the initial TTL values of packets, we can sometimes guess the operating system of the source

**Three-Way Handshake:**

- TCP uses a 3-way handshake to establish a connection between 2 computers

**Hypertext Transfer Protocol:**

- Protocol used to access data on the World Wide Web

Why HTTPS:

- In normal HTTP, client web requests and server responses are sent over the Internet in cleartext
- Anyone intercepting HTTP can see this data traffic

HTTPS:

- To transport HTTP data securely over the Internet
- HTTP over SSL (Secure Socket Layer) or HTTP over TLS (Transport Layer Security)
- A session key is set up to encrypt traffic between user and web server
- Anyone who intercepts the data will not be able to decrypt it

**TCP SEQ and ACK numbers:**

- TCP protocol uses the SEQ and ACK fields to check that all packets have been sent and received correctly
- A SEQ number is randomly allocated to the SYN packet
- SEQ is the sequence number given to the first data byte in a TCP packet
- ACK contains the sequence number of the next packet expected to be received

For what?:

- SEQ and ACK numbers used to re-order packets that arrive out of sequence
- SEQ and ACK numbers can help tell if a packet is missing in transit and can re-send the packet

**TCP and UDP Ports:**

- A virtual channel to applications that are sending and receiving network data
- Also called sockets
- Port numbers start at 0 and go up to 65535
- Well known port numbers
    - 21, 20 - File Transfer Protocol (FTP)
    - 25 - Simple Mail Transfer Protocol (SMTP)
    - 80 - Hypertext Transfer Protocol (HTTP)
    - 443 - Hypertext Transfer Protocol Secure (HTTPS)

**Netstat:**

- Used to display open ports and current network connections

**File Transfer Protocol (FTP):**

- Protocol for copying files between systems
- Two connections are used
    - Control connection for user authentication and other control info (Port 21)
    - Data connection for transfer of file data (Port 20)
- Old protocol with no encryption
- Alternatives like SFTP