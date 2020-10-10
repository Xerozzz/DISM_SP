# Chapter 6: Planning and Deploying Security for Network Communications

# Part 1

# IPSec Concepts

## IPSec Definition

- A set of protocols used to ensure private, secure communications over IP networks by using cryptographic services based on
    - Protecting the contents of IP packets
    - Providing packet filtering
    - Enforcing trusted communication
    - Securing communication with encryption of the information traveling the network
    - Mostly used as an option for IPv4 implementation
- IPsec is an optional feature that the network administrators can use to protect the TCP/IP network traffic
- The protection is mainly based on the combinations of the various encryption and hashing schemes

## Issues that created IPsec

- Original TCP/IP network protocol was not created with security in mind, vulnerable to source spoofing, replay packets and no data integrity or confidentiality
- Subject to DOS attacks, Replay attacks, Spying and more

## IPSec Control Elements

- Internet key exchange (IKE) protocol for exchanging encryption keys
- Authentication Header (AH) to provide an authenticity guarantee for packets
- Encapsulating security payload (ESP) to provide confidentiality through encryption
- IP Compression is also used to compress raw IP data

### Flow

- IKE is the first one to be used when two parties want to communicate with each other
- If the IKE operations fails, there is no further communications possible
- Once the IKE is cleared, the two parties may use AH and/or ESP to protect data traffic

### IKE Module

- One of the key components of IPSec
- Responsible for initial security negotiation (Phase 1), based on the Authentication method(s) defined in the IPSec rule
- Responsible for determining secret keying material (Phase 2) to secure network communication and is related to Filter Action setting of the associate IPSec rule

## IP Security Implementation

### IPsec Communication

- When an IPsec communication begins between two computers, the computers first negotiate using IKE module and authenticate between receiver and sender using Microsoft AuthIP
- Next, extra hashing scheme will help ensure data integrity at packet header
- Finally, data is encrypted with integrity check at the NIC of the sending computer as it is formatted into an IP packet

### Configuring IPsec Security Policies

- IPsec can provide security for all TCP/IP-based application and communications protocols
- IPsec security policies can be established through the Group Policy in an AD
- IPsec security policies can also be configured through the IP Security Policies Management MMC snap-in

## Weighing IPsec Trade-offs

- Deploying IPsec can affect network performance and compatibility with other services and applications
- Do not deploy IPsec if the security it provides is not required

### Impacts of IPsec

- Time needed to establish connection, filter and encrypt packets is long
- Increased packet sizes
- Network inspection technologies used in routers, firewalls and IDS may not work on IPsec packets
- Application compatibility with other platforms
- Effect on AD and DC connections

## Planning an IPsec Deployment

### Configuration of IPSec is based on

- The way you are using IPsec
- Types of client OS in your network
- Type of network devices in your network

### IPsec not recommended for the following

- To secure communication between domain members and their DCs as it reduces network performance and configuration of IPsec policy is complicated
- To secure all traffic in a network due to reduced network performance and network tools that need to inspect packet headers may not work, IPsec also cannot support multicast and broadcast traffic

### IPsec Security Solutions

![Chapter%206%20Planning%20and%20Deploying%20Security%20for%20Netw%20bce5c9955465410daafcebd31cb977a1/Untitled.png](Chapter%206%20Planning%20and%20Deploying%20Security%20for%20Netw%20bce5c9955465410daafcebd31cb977a1/Untitled.png)

### Proper Uses Of IPsec

- Packet filtering such as using IPsec with the Routing and Remote Access service to permit or block inbound or outbound traffic
- Securing host-to-host traffic on specific paths
- Securing traffic to servers
- Combining L2TP and IPsec for securing VPN scenarios
- Incorporating site-to-site or gateway-to-gateway tunneling

### IPsec Windows Implementations

- In a simple network structure, one IPsec policy can be designed to contain multiple rules, in a one policy for all system
- In a large environment, many different IPsec policies may be designed

### Factors That Can Increase The Number of Policies

- Computer roles
- Sensitivity of data traveling over the network
- Computer OS
- Domain relationships and memberships
- Number of applications that require IPSec

# Part 2

## Elements That Make Up A Rule

- Each IPsec policy may consist of multiple rules
- Each rule contains 5 configurable elements, Connection Type, Mode, Filter List, Host-To-Host Authentication Method and Filter Action

### Connection Type

- The rule only applies for particular types of connections
- LAN, Remote or ALL

### Mode (Transport or Tunnel)

- IPsec has two security modes, Transport and Tunnel
- Transport mode is used to secure communications within a network and it can be server-to-server or server-to-client
- Tunnel mode is used to secure communications between networks or gateways and is primarily used for interoperability with gateways or end systems that do not support L2TP/IPsec or PPTP VPN site-to-site connections
- In the simplest case, the IPsec protection is catering for system within a LAN, choose Transport Mode
- When the connections involve the WAN, choose Tunnel Mode

### Filter List

- IPsec filter is a specification in the IPsec rule that is used to match IP packets, filters are grouped together in a system wide Filter List
- In the IPsec rule properties setting, the system wide filter list will be available for the choice of the filter
- Packets which match the filter will be applied with the associated filter actions such as permit, block or negotiate security
- However, if the traffic does not match with any IPsec filter, IPsec will just let the traffic through instead of blocking it

Managing IPsec Policies:

- Create a new policy and define the set of rules for the policy, adding filter lists and filter actions as required
- First create the set of filter lists and filter actions, then create the policies and add rules that combine the filter lists with filter actions

### Host to Host Authentication Method used by IKE in phase 1

- If the connection matches the Filter IKE (Phase 1) will be invoked for initial authentication
- Available authentication methods include Kerberos V5, Certificates with PKI and Pre-shared key
- The authentication process is does using Diffie-Hellman asymmetric key encryption for data exchange

Keberos V5:

- Default authentication method for Windows 2000 servers or later
- Based on mutual authentication and is used when all your clients can authenticate using KerberosV5
- A method that requires the least administrative effort

Certificates:

- A method of granting access to users based on their unique identification
- Used in situations that include access to corporate resources, external business partner communications or computers that do not run the KeberosV5

Pre-shared key:

- Used when other methods are not available
- Is a shared secret key

Choosing IPsec Authentication Method

- More than one can be selected with designated priority level
- IKE (Phase 1) will sort out if two parties share one common authentication method

![Chapter%206%20Planning%20and%20Deploying%20Security%20for%20Netw%20bce5c9955465410daafcebd31cb977a1/Untitled%201.png](Chapter%206%20Planning%20and%20Deploying%20Security%20for%20Netw%20bce5c9955465410daafcebd31cb977a1/Untitled%201.png)

### Filter Action

- Only be triggered when the incoming or outgoing connections match the filter
- Available types of actions are Permit, Block and Negotiate Security
- Negotiate Security to be carried out at Phase 2 of IKE

## Encryption Levels

- Two basic categories, symmetric key and public key encryption
- Lifetime settings determine when a new key is generated
- During IKE phase 2, both parties will try to negotiate for a commonly available encryption scheme
- Once it is determined, the filter action will base on it to encrypt data packets

### Methods of Hashing

- SHA
- MD5
- Hashing method is used to support AH authentication traffic

### Methods of Encryption

- DES
- 3DES
- AES
- Encryption method used to support ESP in encapsulating security payload traffic

### Types of Solutions for Respective IPsec Requirements

![Chapter%206%20Planning%20and%20Deploying%20Security%20for%20Netw%20bce5c9955465410daafcebd31cb977a1/Untitled%202.png](Chapter%206%20Planning%20and%20Deploying%20Security%20for%20Netw%20bce5c9955465410daafcebd31cb977a1/Untitled%202.png)

- AH provides authentication only
- ESP provides authentication & encryption

### Tunnel Modes

- AH Tunnel Mode encapsulates an IP packet by placing an AH header between internal and external IP headers
- ESP Tunnel Mode first encapsulates the IP packet with an ESP header and the result is further encapsulated with an additional IP header

### Putting Everything Together

![Chapter%206%20Planning%20and%20Deploying%20Security%20for%20Netw%20bce5c9955465410daafcebd31cb977a1/Untitled%203.png](Chapter%206%20Planning%20and%20Deploying%20Security%20for%20Netw%20bce5c9955465410daafcebd31cb977a1/Untitled%203.png)

## Deploying IPsec Policies

### Deployment Methods

- Local Policy Objects, a way to enable IPsec for computers that are not members of a domain
- Group Policy Objects, where IPsec policy is propagated to any computer accounts affected by the GPO
- Command-Line Tools, "netsh" IPsec command in WinServer 2003/2008

### Factors To Consider When Using Group Policy Objects

- The assignment precedence for IPsec policies, from lowest to highest is LSDOU
- Persistent IPsec Policy has the highest precedence of all, even though it is stored on the local computer and is effective and other policies cannot be applied
- IPsec policies from different OUs are never merged
- For domain-based IPsec policy, limit the number of rules to 10 or less
- Create and apply an IPsec policy at the domain level to provide a baseline of IPsec protection
- Use the Export and Import Policies commands in the IP Security Policy Management console to backup and restore the IPsec policy objects
- Be sure to adequately test the impact of new IPsec policies before assigning them in the domain

## Understanding Default IPSec Policies

- Client (Respond Only) will secure communications only if the other computer requests for it
- Server (Request Security) accepts initial incoming communication that is unsecured, requests for communication to be secured and will carry on with unsecured connection if client does not support
- Secure Server (Require Security) accepts initial inbound unsecured communication but requires that all communications be secured

## Understanding IPsec Policy Precedence

- Possible to configure Ipsec for multiple containers that will affect a computer
- Only one IPsec policy can be assigned to a computer at a time
- If there are multiple IPsec policies assigned at different levels, the last one takes effect
- Precedence sequences from lowest to highest is  LSDOU like GPO
- Default order can be overridden using Enforced and Block Policy Inheritance like GPOs

### What To Remember When Troubleshooting IPsec Policies

- Only a single IPsec policy can be assigned at a specific level in AD
- An IPsec policy assigned to an OU takes precedence over a domain-level policy for members of that OU
- IPsec policies from different organizational units are never merged

### Procedure for Deleting Policy Objects

- Unassign the IPsec policy in the GPO
- Wait 24 hours to ensure that change is propagated
- Delete the GPO

### Persistent/Static IPsec Policies

- Provides maximum protection against attacks during computer startup
- Adds to or overrides local or AD policy
- Remains in effect regardless of whether other policies are applied
- Provides backup security in case IPsec policy gets corrupted or if errors occur
- Can be set using command line tools like "netsh"at the local station