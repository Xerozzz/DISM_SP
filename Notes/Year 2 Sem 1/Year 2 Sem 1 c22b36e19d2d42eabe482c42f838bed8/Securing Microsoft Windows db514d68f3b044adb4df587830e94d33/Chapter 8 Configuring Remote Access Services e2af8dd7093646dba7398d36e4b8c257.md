# Chapter 8: Configuring Remote Access Services

# Introduction to Remote Access

## Remote Access Services (RAS) Role

- Enables remote access through three means, virtual private networking, DirectAccess and Web Application Proxy

## Virtual Private Network (VPN)

- Like a tunnel through a larger network that is restricted to designated member clients only

## DirectAccess

- Establishes two "tunnels" for connecting to a Direct Access server used in remote access
- Transparent to users and always on

## Web Application Proxy

- Publishing applications so that users external to an organization can access those applications on the organization's servers

# Implementing a Virtual Private Network

![Chapter%208%20Configuring%20Remote%20Access%20Services%20e2af8dd7093646dba7398d36e4b8c257/Untitled.png](Chapter%208%20Configuring%20Remote%20Access%20Services%20e2af8dd7093646dba7398d36e4b8c257/Untitled.png)

- VPNs can use an Internet connection or an internal network connection as a transport medium to establish a connection with a VPN server
- A VPN uses LAN protocols as well as tunneling protocols to encapsulate the data as it is sent across a public network like the Internet
- VPNs create an encrypted tunnel between the client and the RAS server

## Benefits of a VPN

- Users can connect to a local ISP and connect through the ISP to the local network
- VPN is used to ensure that any data sent across a public network is secure

## How a VPN works

- VPN servers use two or more NICs for communication, one for connecting to the private network inside the organization and the other to the external public network
- To create this tunnel, the client first connects to the Internet by establishing a connection using a remote access protocol
- Once connected to the Internet, the client establishes a second connection with the VPN server
- The client and the VPN server agree on how the data will be encapsulated and encrypted across the virtual tunnel

## Caveats for VPNs

- Do not use any of your DCs as a VPN server
- VPN server is public facing and should be in DMZ segment

# Using Remote Access Protocols

## Remote Access Protocols

- Remote access protocol carries the network packets over a WAN link
- RAP encapsulates a packet such as an IP datagram, so that it can be transmitted from a point at one end of a WAN to another point

## Remote Access Tunneling Protocols

- Point-to-Point Tunneling Protocol
- Layer Two Tunneling Protocol
- Secure Socket Tunneling Protocol
- IKE v2 Protocol (IPsec, Tunnel Mode, IKE version 2)

### Point-to-Point Tunneling Protocol (PPTP)

- Used in legacy remote communications involving modems
- Enables the authentication of connections and encryptions for the network communications, but is not considered to be as secure as modern options
- Can automatically negotiate communications with several network communication layers at once
- Encrypts data carried using Microsoft Point-to-Point Encryption (MPPE)

### Layer Two Tunneling Protocol (L2TP)

- Works similarly to PPTP
- Uses Layer Two Forwarding that enables forwarding on the basis of MAC addresses
- Uses IPsec for additional authentication and for data encryption

### Secure Socket Tunneling Protocol (SSTP)

- Employs PPP authentication techniques
- Encapsulates the data packet in the Hypertext Transfer Protocol (HTTP) used through web communications
- Additionally uses a Secure Sockets Layer (SSL) channel for secure communications
- Viewed as more secure than PPTP or L2TP

### IKE v2 Protocol

- Employs IPsec in tunnel mode protocol over UDP port 500 and 4500
- Encapsulates datagrams using IPsec ESP or AH headers for transmission over the network
- Uses AES-256, AES-128, AES-192 and 3DES encryption algorithms
- Believed to be faster, more secure and more resilient to changing network connectivity
- However, it is proprietary software

![Chapter%208%20Configuring%20Remote%20Access%20Services%20e2af8dd7093646dba7398d36e4b8c257/Untitled%201.png](Chapter%208%20Configuring%20Remote%20Access%20Services%20e2af8dd7093646dba7398d36e4b8c257/Untitled%201.png)

# Configuring a VPN Server

![Chapter%208%20Configuring%20Remote%20Access%20Services%20e2af8dd7093646dba7398d36e4b8c257/Untitled%202.png](Chapter%208%20Configuring%20Remote%20Access%20Services%20e2af8dd7093646dba7398d36e4b8c257/Untitled%202.png)

## General Steps

1. Install the Network Policy and Access Services role
2. Configure a Microsoft WinServer 2016 server as network's VPN server, including configuring the right protocols to provide VPN access to clients
3. Configure a VPN server as a DHCP Relay Agent for TCP/IP communications
4. Configure the VPN server properties
5. Configure a remote access policy for security

## Configuring the Server's Firewall

- The VPN server must be able to send communications through the network
- An early configuration step is to make sure its communications can go through a firewall set up at the server
- By default on Windows Firewall, TCP and UDP ports used by VPN are unblocked auto weematically when configuring VPN server

## Configuring VPN Properties

- After VPN server is set up, you can further configure it from Routing and Remote Access Tool

## Configuring a DHCP Relay Agent

- A DHCP Relay Agent broadcasts IP configuration information between the DHCP server on a network and the client acquiring an address
- You can configure the VPN server as a DHCP Relay Agent using Routing and Remote Access Tool
- In basic terms:
    - The client contacts the VPN server to make a connection
    - The VPN server as a DHCP Relay Agent contacts the DHCP server for an IP address for the client
    - The DHCP server notifies the VPN server of the IP address
    - The VPN server relays this IP address assignment to the client

## Configuring VPN Security

- You can set up VPN security using a remote access policy which greatly reduces admin overhead and offers more flexibility and control for authorizing connection attempts

### Elements of Remote Access Policy

- Access Permission
- Conditions
- Constraints
- Settings

### Before Configuration

- First step in evaluating access is to determine if access permission is enabled at the VPN server
- Default permission for this policy is set to Deny access, you have to change the default permission to Grant Access in the default remote access policy
- The conditions of a remote access policy are a set of attributes that are compared with the attributes of the connection attempt
- If the connection attempt matches the conditions of a remote access policy, the constraints are evaluated
- Settings in the remote access policy are then examined such as IP filters, encryptions, IP settings

### Establishing a Remote Access Policy

- You can use the Routing and Remote Access tool to create and configure a remote access policy
- To create a new remote access policy, click to activate and then right-click the Remote Access Logging & Policies folder in the tree under the VPN server
- Click Launch NPS to launch the Network Policy Server Tool

## Monitoring VPN Users

- After you have configured the VPN server and placed it in production, you should periodically monitor the users who are connected
- Use the Routing and Remote Access tool to monitor connected users

# Part 2

# Troubleshooting VPN Installations

## Hardware Solutions

- Use Device Manager to make sure network adapter and WAN adapters are working properly and that there are no resource conflicts
- For an external DSL adapter or a combined DSL adapter and router, make sure the device is properly configured and connected, check monitor lights for problem
- Call ISP to determine if problems are present on the ISP's WAN

## Software Solutions

- Use the Services tool or server Manager to make sure required services are started
- Ensure that the Windows Firewall is set up to allow remote access
- Make sure that the VPN server is enabled and started
- Check the remote access policy to be sure that access permission is granted
- In the Routing and Remote Access tool, check the network interface
- Make sure that the IP parameters are correctly configured to provide an address pool for a VPN server
- Check to be sure that the remote access policy is consistent with the users' access needs
- Open the Remote Access Management Console and click Dashboard in the left pane
- If only certain clients but not all are having connection problems, try these solutions:
    - Make sure the clients are using the same communications protocol as the server
    - If your manage access to a VPN server by using security groups, make sure that each user account or computer account that needs access is in the appropriate group
- Basically check the overall hardware connections and system configurations

# Connecting Through Remote Desktop Services

## Remote Desktop Services

- Another viable option to offer remote access services to remote clients
- Unique function is that a remote desktop session will be created and run on the remote desktop server
- The remote client acts as viewer to allow the user to observe and operate the desktop session that runs on the remote desktop server
- RDS offers two additional remote access features that VPN does not support, thin client connections and enabling of server admins to know details of remote client activities

### Purposes of WinServer RDS

- To run applications on a server instead of the client
- To support thin clients
- To centralize program access

### Role Services That Can Be Installed with RDS

- Remote Desktop Session Host
- Remote Desktop Web Access
- Remote Desktop Virtualization Host
- Remote Desktop Licensing
- Remote Desktop Gateway
- Remote Desktop Connection Broker

## Thin Clients

- Downsized PCs that have minimal Windows-based OSs that access a WinServer2016 server so that most CPU-intensive operations are performed on the server
- Generally used to save money and reduce training and support requirements
- Also used for portable field or handheld remote devices

## Remote Desktop Services Server

- Enables clients to run sessions-based desktops, virtual desktops, and software applications on WinServer2016 instead of at the client
- Session-based desktop client accesses an RDS server to run applications on that server during a connection session

### Centralized Control of Program Usage

- Highly-classified or sensitive documents can be stored and modified only on the server
- Server can be configured to provide a high level or security

### Components to Enable Desktop Server Connectivity

- WinServer 2016 multiuser Remote Desktop Services
- Remote Desktop Services Client
- Remote Desktop Protocol
- Remote Desktop Services administration tools

### RemoteApp

- A feature that enables a client to run an application without loading a remote desktop on the client computer
- The program appears to be just another program in a windows running on the local computer

## Virtual Desktops

- Are used in association with accessing virtual machines on a virtual server through Hyper-V
- Multiple virtual desktops can be in a pool of desktops for different purposes

# Installing Remote Desktop Services

- When installing RDS role, you also need to install the RDS licensing role service to manage the number of terminal server user licenses you have obtained from Microsoft
- The RDS Licensing role server can be installed when you install the Remote Desktop Services role
- Licenses can be purchased either per user account or by client device
- When you install RDS role, you implement Network Level Authentication (NLA)
- Consider who will be allowed to access the RDS server using groups of user accounts and prep in advance before installing the RDS role

## Users Who Can Access RDS Server

- Consider creating a domain local group such as "RDS Users"
- Next, create different global groups of users, such as a global group for each department that will access the RDS server
- Add the appropriate user accounts for each department's global group
- Finally, add the global groups to the single domain local group

## Network Level Authentication

- NLA enables authentication to take place before the RDS connection is established
- Designed to eliminate MITM attacks

# Built-In Remote Desktop Services

- Installation of a full scale Remote Desktop Services may high demand on system resources
- For all Windows Servers, there are built-in Remote Desktop Services with limited number of connections, simplified configuration options and run on the same RDP

# Accessing an RDS Server From A Client

- Remote Desktop Services client computers can sign in using the Remote Desktop Connection (RDC) client