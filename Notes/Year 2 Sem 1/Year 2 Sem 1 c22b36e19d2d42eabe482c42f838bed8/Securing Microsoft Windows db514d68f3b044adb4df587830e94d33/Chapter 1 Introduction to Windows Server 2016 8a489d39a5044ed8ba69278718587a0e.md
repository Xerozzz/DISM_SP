# Chapter 1: Introduction to Windows Server 2016

## Objectives:

- Understand the need for secure computing
- Microsoft's Commitment to Security
- Introduction to Windows Server 2016
    - Identify key features of each Windows Server 2016 Edition
    - Understand hardware requirements for Windows Server 2016
    - Identify client systems that can be used with Windows Server 2016
    - Understand important general features of Windows Server 2016
    - Plan a Windows Server 2016 networking model

---

# Part 1

## The Need for Secure Computing

### Various Types of Threats

- Viruses
- Worms
- Programs that steal confidential information
- Hacking via System Vulnerabilities

### Source of Computer Security Problems

- Bad software design
- Bad implementation

### Law for Hold Management Responsible for Data Breaches

- California SB-1386
- PDPA 2012 (Singapore)
- Electronic Transactions Act 2010 (Singapore)

### Safer Computing Requirements

- Change in the behavior of management, programmers and users
- Make secure computing a priority
- Write secure operating systems and applications while not affecting productivity
- Train users to always keep security in mind

---

## Microsoft's Commitment to Security

### Different Areas of security where Microsoft decided to make significant investment

- Isolation and Resiliency
    - The idea is to split the computer system into smaller pieces so each piece is separated from the rest, so if one gets compromised or damaged, the others are not affected
    - Implementations: Firewalls, Object level access control etc
    - Automatically blocks unsolicited downloads and unwanted pop-ups from Web sites by Internet Explorer
    - Inclusion of better file attachment handling in outlook Express and Windows Messenger
    - Compilation of core Windows components with the most recent version of compiler technology
    - Introduction of Exchange Edge Services for email protection, enhanced security and management of junk email
    - An integrated set of protection technologies such as MSE (Microsoft Security Essentials)
    - Smart screening technologies like intelligent spam-filtering solution
    - Client inspection technologies like MSBA
- Software Updates
    - Primary way to protect against security vulnerabilities
    - Microsoft's monthly release of software updates
    - Various products incorporated by Microsoft to make the updates seamless
        - System Center Configuration Manager (SCCM)
        - Microsoft Baseline Security Analyzer (MBSA)
        - Windows Software Update Services (WSUS)
- Quality
    - Use of quality standards and processes
    - Use of best practices in all phases of software development
    - Development of new internal tools that automatically check code for common errors
    - Thorough testing of software before its release
- Access Control and Authentication
    - Passwords
    - Smart cards
    - Public key Infrastructure (PKI)
    - Internet Protocol Security (IPSec)
    - Active Directory Rights Management Services (AD RMS) (Will not come in exam)

### Trustworthy Computing

A way to safe and reliable computing

Requirements of trustworthy computing:

- Computers need to be reliable
- Software that operates those machines must be equally reliable
- Service components have to be dependable

Dimensions on which Microsoft's objective of trustworthy computing relies:

- Goals to deliver
    - Security
    - Privacy
    - Business Integrity
- Means
    - Security by design, by default and by deployment
    - Privacy information principles
    - Availability, Management, Accuracy
    - Usability, Responsiveness, Transparency

### Trusted Cloud

Trustworthy computing is a long term initiative that is currently expanding to the cloud

Based on four foundational principles:

- Security
- Privacy
- Compliance
- Transparency (Microsoft Trust Center)

### Secure Code

Various steps taken by Microsoft to implement and maintain security:

- Train Windows engineers in writing secure code, threat modeling, specialized testing techniques
- Write documentations with security in mind

### Common Language Runtime

Runtime environment for the .NET framework

Manages the running of .NET programs regardless of the programming languages they were written in

Goals for the Design:

- To simplify the development environment
- To get simpler and safer deployment by getting rid of concept of registry and zero-impact installation

---

# Part 2

## Using Windows Server 2016 with Client Systems

### Most compatible client workstation OS with Windows Server 2016

- Windows 7,8,8.1 and 10
- Windows 10 is the most compatible in terms of client management

### Client

- Computer that accesses resources on another computer via a network

### Workstation

- Computer that has its own CPU and can be used as a stand-alone or network computer

### Overall goal of Microsoft is to achieve a lower total cost of ownership (TCO)

- TCO is the full cost of owning a network, including hardware, software, training, maintenance and user support costs

### Domain

- A grouping of network objects such as computers, servers and user accounts that provides for easier management
- Computers and users in a domain can be managed to determine what resources they can access

### Advantages of using Windows Server 2016 and Windows Version 7 through 10

- Enhanced capabilities to recover from many types of network communication problems
- Computer code for more efficient network communications
- More network diagnostic capabilities
- Computer code for better use of network communication protocols
- Continuing upgrades for Windows Powershell commands and scripts in both Windows Server 2016 and Windows 7 through 10

### Active Directory

- Database of computers, users, groups of users, shared printers, shared folders and other network resources

### Linus Integration Services

- Windows Server 2016 support Linux and enables Linux clients to access a Linux VM in Hyper-V

---

## Windows Server 2016 Features

- **Server Manager**
- **Security**
- Clustering
- **Enhanced Web Services**
- **Windows Server Core and Nano Server**
- **Windows Powershell**
- Virtualization
- **Reliability**
- Multitasking and multithreading
- Physical and logical processors
- Containers

## Server Manager

- Enables the server administrator to manage critical configuration features from inside one tool

### Uses

- Configure a server from the beginning
- View computer configuration information
- Change server roles and system properties
- Configure networking
- Configure Remote Desktop
- Configure security, including the firewall
- Add and remove features
- Run diagnostics
- Manage storage and backups
- Manage multiple servers from one place

### New Features

- Local server option makes all of the local server properties available to manage
- Multiple servers are easier to manage from one place
- Servers can be grouped so all servers receive commands simultaneously
- Dashboard offers more quick-start guidance
- Server Manager GUI has a new look with added features and greater ability to add and manage remote servers

## Security

- Security by default
- File and Folder permissions
- Security policies
- Encryption of data
- Event auditing
- Various authentication methods
- Server management and monitoring tools

## Enhanced Web Services

- Transforms Windows Server 2016 into a versatile web server
- Includes over 40 modules
- Provide easier application of IIS patches
- Makes it easier for network programmers to write network applications and configure applications for the web

## Windows Server Core and Nano Server

### Windows Server Core

- Minimum server configuration
- Designed to function in a fashion similar to traditional UNIX and Linux servers
- Does not provide GUI or Graphical tools to configure your server
- Does not provide extra services you do not need and software like Microsoft Word

### Windows Nano Server

- A new installation option in Windows Server 2016
- Smaller footprint than Server Core
- Provides a basic foundation for server computing
- Intended to be faster and less maintenance
- Used by Microsoft to run:
    - DNS or DHCP server
    - Applications server from the cloud
    - Web Server
    - Database or file server

## Windows PowerShell

- Command line interface that offers a shell to execute commands and scripts
- Scripts are files that contain commands to be run by computer OS

### Can perform tasks

- Work with files and folders
- Manage disk storage
- Manage network tasks
- Set up local and network printing options
- Install,list and remove software applications
- View information about the local computer, including user accounts
- Manages services and processes
- Lock a computer or log off
- Manage IIS Web Services

## Reliability

- The operating system kernel runs in privileged mode to protect it from problems created by a malfunctioning program or process
- Kernel consists of core programs and the computer code of the operating system
- Privileged mode gives the OS kernel an extra level of security from intruders and prevents system crashes due to poorly written applications

### Process

- A computer program or portion of a program that is currently running

### Protected Process

- One for which outside influences are restricted

---

## Windows Server 2016 Networking Model

### Network

- A communications system enabling computer users to share computer equipment, application software, and data, voice and video transmissions
- Contains computers joined by communications cabling or sometimes by wireless devices

### Peer-to-Peer Networking

- Uses workstations to share resources such as files and printers and to connect to resources on other computers
- Can be effective for very small networks as it does not require server setup nor Active Directory services
- Disadvantages
    - Management of network resources is decentralized
    - As the network increases in size, administration becomes harder
    - Lack of security of resources

### Server-Based Networking

- Centralizes the network administration on one or more servers
- Can handle hundreds of users at once
- Fast response when delivering shared resource and less network congestion when multiple workstations access that resource
- Advantages
    - Users only need to log on once to gain access to network resources
    - Security is stronger
    - All members can share computer files
    - Printers and other resources can be shared
    - All members can have e-mail and send messages to other office members through an e-mail server
    - Software applications can be stored and shared in a central location
    - Important databases can be managed and secured from one computer
    - All computers can be backed up more easily
    - Computer resource sharing can be arranged to reflect the work patterns of groups within an organization
    - The server administrator can save time when installing software upgrades

## Protocols for Windows Server 2016 Networking Model

- Protocols consist of guidelines on how data is formatted into packets or frames ,transmitted across the network and interpreted at the receiving end

### Transmission Control Protocol (TCP)

- Provides for reliable end-to-end delivery of data by controlling data flow
- Computers agree on a "window" for data transmission that includes the number of bytes to be sent
- Window is constantly adjusted to account for existing network traffic
- Connection-oriented communication that ensures packets are delivered and in the right sequence with accurate contents

### Address Resolution Protocol (ARP)

- Used to acquire the physical addresses associated with a computer's NIC
- Every NIC has a physical address/MAC address
- Proper communication using TCP/IP relies on both IP and MAC addresses

### Automatic Private IP Addressing (APIPA)

- Used to automatically configure the TCP/IP settings for a computer without using a DHCP server
- Computer automatically assigns itself an IP address from the reserved range of 169.254.0.1 to 169.254.255.254
- Appropriate for small organizations that have only one network segment and do not need to access another network or the Internet

### Dynamic Addressing Through DHCP Server

- Common for medium and large networks
- A DHCP server must be installed and configured on the network
- DHCP server can also assign subnet mask, default gateway, DNS server and other IP settings
- Saves a great deal of administrative effort

## Summary

- The need for Secure Computing
- The Trustworthy Computing and Trustworthy Cloud
- Microsoft Security Initiatives and Commitment
- Windows Server 2016 main platforms include Essentials, Standard and Datacenter Edition
- Windows Server 2016 includes many vital features for security, networking, clustering, virtualization, cloud computing, reliability, database handling, multitasking and multithreading
- Peer-to-Peer and Server-Based networks
- TCP/IP is the default protocol installed with Windows Server 2016
- IPv4 and IPv6
- Every network device must have a unique IP address to ensure network connectivity and the delivery of data
- IP addresses can be manually configured using static addressing or automatically configured through APIPA or DHCP