# Chapter 4: Deploying and Managing DNS & Group Policy

# Part 1

# Implementing Microsoft DNS

- DNS Servers provide the DNS namespace for an enterprise
- One of the requirements for using AD is to have DNS servers setup for its domains
- Windows Server DNS is most compatible with AD
- Other non-microsoft servers can be used but must be compatible with AD

## DNS Zones

- DNS name resolution is enabled through the use of tables of information that link computer names with IP addresses
- The tables are associated with partitions in a DNS server called zones, which contain resource records

### Forward Lookup Zone

- The zone that links computer names to IP addresses
- Holds host name records called address records
- Most of the DNS queries are handled based on the resource records from this Zone
- When you install DNS on a DC, a forward lookup zone is automatically created for the domain with the DNS server's address record already entered

## Using the DNS Dynamic Update Protocol

- Microsoft DNS is also called Dynamic DNS (DDNS), a modern form of DNS that enables client computers and DHCP servers to automatically register IP addresses

### DNS dynamic update protocol

- Enables information in a DNS server to be automatically updated in coordination with DHCP

### After Configuring DNS

- Always make sure that it is configured to secure the DNS dynamic update protocol
- Saves admin time because they no longer have to manually register each new workstation each time a new IP lease is issued

## DNS Replication

### Primary DNS server

- The DNS Server that is the main administrative server for a zone

### Secondary DNS server

- Contains a copy of the primary DNS server's zone database, but is not used for administration
- Uses zone transfer over the network to obtain copy of zone database
- Vital services performed by secondary DNS servers:
    - Make sure there is always a copy of primary DNS server's data
    - To enable DNS load balancing among primary DNS server and its secondary servers
    - To let a secondary DNS face to and answer to queries from the public network
    - To reduce congestion on one part of the network

### If you use AD and have 2 or more DCs

- Aim to set up Microsoft DNS services on at least two of the DCs

## How DNS Query Works

- Client requests the local DNS for a name to IP address resolution
- Local DNS gives immediate answer when it is the authoritative server for the domain and has the required info in its cache
- When local DNS does not have the answer, it looks up the ip address of one of the "root" servers, also known as iterative lookup to get the required info

## Stub Zone

- Has only the bare necessities for DNS functions, which are SOA record zone, Name Server records to identify authoritative servers and a record for name servers that are authoritative
- Commonly used to help quickly resolve computer names

### Zone Transfer Privilege

- Local DNS requires to have zone transfer privilege granted from the target DNS which owns the Forward zone
- You cannot set up a Stub Zone for [google.com](http://google.com) unless your local DNS has the required privilege granted from the authoritative DNS of google.com

## Additional DNS Server Roles

- It is common to designate one DNS server to forward name resolution requests to a specific remote DNS server
- DNS forwarding can be set up if the DNS server receives the forwarded request cannot resolve the name
- Windows Server 2016 supports the use of forwarder and root hints

### Caching Servers

- A DNS server can function as a caching server to provide fast queries because the results of each query is stored in RAM
- A DNS server without zones is a server that is caching-only
- A caching-only server queries a primary or secondary DNS server and caches the results to provide fast responses for identical queries in the future
- Used to reduce the number of secondary servers and reduce extra network traffic
- One limitation is that it takes time for each one to build up a comprehensive set of resolved names to IP addressses
- Lastly, sometimes it is necessary to flush the DNS server cache

## Forwarder vs Root Hints

- Both approaches have pros and cons in terms of operational concerns or security concerns

### Forwarder

- Faster recursive query that may give questionable answers
- Local DNS has no way to ensure security configuration of external forwarders
- Potential to enable customizable DNS service within an Enterprise for security enhancement

### Root Hints

- Slower due to interactive queries for best answer
- More reliable

## Creating a DNS Implementation Plan

### Best Practices

- Implement WinServer 2016 DNS servers instead of other types
- Set up resource records and zones for IPv4 and IPv6
- Consider using namespaces to represent natural organizational boundaries
- Make sure the DNS servers on a private network are well secured in terms of WinServer2016 security options
- Plan to locate a DNS server across most site links
- Create two or more DNS servers to take advantage of the load balancing, the multi-master relationships and the fault tolerance
- Designate one DNS server as a forwarder to reduce traffic
- The number of DNS servers that you set up can be related to your analysis of an organization
- If you have multiple servers used for one application, use round robin to distribute the load
- If a branch location with a read-only domain controller (RODC) needs local DNS services, make the RODC a secondary DNS server and not a primary server

## DNS Enhancement in WinServer 2016

- The ability for DNS to work with client computers that have more than one NIC
- New Powershell cmdlets for configuring DNS
- DNS Group Policies

### Group Polices

- Filter malicious IP addresses and redirecting malicious clients to a dead end rather than to the system they want to reach
- Redirect clients to specific data sources or servers according to time of day
- Managing client access to account for high traffic situations
- Direct clients to the best source for a specific application

## Troubleshooting DNS Steps

- Restarts the DNS server and the DNS client services
- Check for the most recent error logs related to DNS

![Chapter%204%20Deploying%20and%20Managing%20DNS%20&%20Group%20Polic%20ce6cdbaf091c4cbda3910d918cb634b9/Untitled.png](Chapter%204%20Deploying%20and%20Managing%20DNS%20&%20Group%20Polic%20ce6cdbaf091c4cbda3910d918cb634b9/Untitled.png)

## DNS Threats

- DDOS with DNS amplification attacks where bogus queries are sent to a DNS to trigger it to send high volume of replies to the targeted victim
- Cache Poisoning where the DNS cache, stub zone or forwarder is compromised and causes it to return incorrect IP addresses or divert to wrong location
- Registrar Hijacking or domain hijacking where the registration of a domain is changed without permission of its original registrant. Done most commonly by exploiting vulnerabilities in the domain name registration system or through social engineering

### Securing the Windows DNS Server

![Chapter%204%20Deploying%20and%20Managing%20DNS%20&%20Group%20Polic%20ce6cdbaf091c4cbda3910d918cb634b9/Untitled%201.png](Chapter%204%20Deploying%20and%20Managing%20DNS%20&%20Group%20Polic%20ce6cdbaf091c4cbda3910d918cb634b9/Untitled%201.png)

# Using Microsoft Baseline Security Analyzer

- A tools used to scan Windows-based computers for common security holes
- Compares a computer's settings against Microsoft's released patches and listed vulnerabilities
- Provides a streamlined method to identify missing security updates and common security misconfigurations

### MBSA Checked Parameters

- Internet Explorer security zone settings per local user
- Outlook security zone settings per local user
- Office products security zone settings per local user

### Running MBSA on multiple machines or remotely

- Server service, Remote Registry service, File & Print Sharing must be enabled

# Microsoft Security Compliance Manager

- Utility to enable automation of deployment and monitoring baseline compliance

## Key Benefits and Features

- Download security baselines from Microsoft
- Compare and customize security baselines
- Export baselines in formats like XLS and/or GPOs

# Part 2

# Overview of Security Features in Windows Server 2016

## Windows Server 2016 was created to emphasize security

- Reduced attack surface of the kernel through Server Core and Nano Server
- Expanded and evolving Group Policies
- Windows Firewall
- Windows Defender
- Security Templates and Security Configuration and Analysis Tools
- User Account Control
- BitLocker Driver Encryption

# Introduction to Group Policy

## Group Policy in Windows Server 2016

- Enables you to standardize the working environment of clients and servers by setting policies in Active Directory
- Computer Configuration settings applies to computers
- User Configuration settings applies to users

### Defining Characteristics of a Group Policy

- Group Policy can be set for a site, domain, OU or local computer
- Group Policy cannot be set for non-OU folder containers
- Group Policy settings are stored in Group Policy Objects
- GPOs can be local and nonlocal
- Group Policy can be set up to affect user accounts and computers
- When Group Policy is updated, old policies are removed or updated for all clients

# Securing Windows Server 2016 Using Security Policies

- Security policies are a subset of individual policies within a larger group policy for a site, domain, OU or local computer

## Security Policies Include

- Account Policies
- Audit Policy
- User Rights
- Security Options
- IP Security Policies (Covered in IPsec lecture)

## Account Policies

- Security measures set up in a Group Policy that applies to all accounts or to all accounts in a container when AD is installed

### Account Policy Options That You Can Configure

- Password security
    - One option is to set a password expiration period, requiring password changes at intervals
    - Some organizations require minimum password length
    - Enforce password history
    - Minimum and maximum password age
    - Passwords must meet complexity requirements
    - Store password using reversible encryption
- Account lockout
    - The OS can employ lockdown to an access to an account after a number of unsuccessful tries
    - The lockout can be set to release after a specific period of time or by intervention of server administrator
    - A common policy is to have lockout go into effect after 5-10 failed attempts
    - Parameters for account lockout:
        - Account lockout duration
        - Account lockout threshold
        - Reset account lockout count after
- Kerberos security
    - Involves the use of tickets that are exchanged between the client who requests logon and network services access and the server or AD that grants access
    - When AD is used, each DC is a key distribution center
    - One a user is authenticated, the Kerberos ticket-granting service grants a permanent ticket to that computer
    - A service ticket is good for the duration of the logon session
    - Options for configuring Kerberos:
        - Enforce user logon restrictions
        - Max lifetime for service and user ticket and user ticket renewal, the shorter the safer
        - Maximum tolerance for computer clock synchronization
    - Enhancements on Windows Server 2016 and Windows 10:
        - The use of AES encryption
        - When AD is installed, account policies enable Kerberos, when AD not installed, default authentication is through Windows NT LAN Manager Version 2 (NTLMv2)

### Establish Audit Policies

- Examples of events an organization can audit are as follows:
    - Account logon and logoff events
    - Account management
    - Directory service access
    - Logon and log off events at the local computer
    - Object access
    - Policy change
    - Privilege use
    - Process tracking
    - System events

### Configuring User Rights

- User rights enable an account or group to perform predefined tasks
- The most basic right is the ability to access a server, more advanced rights give privileges to create account and manage server functions
- Two general categories of rights:
    - Privileges — Generally relate to the ability to manage server or AD functions
    - Logon rights — Are related to how accounts, computers and services are accessed
- Some examples of privileges include:
    - Add workstations to domain
    - Back up files and directories
    - Change the system time
    - Create permanent shared objects
    - Generate security audits
    - Load and unload device drivers
    - Perform volume maintenance tasks
    - Shut down the system
- Examples of logon rights are as follows:
    - Access this computer from the network
    - Allow logon locally
    - Allow logon through Remote Desktop Services
    - Deny access to this computer from the network
    - Deny logon as a service
    - Deny logon locally
    - Deny logon through Remote Desktop Services

    ### Configuring Security Options

    - Many specialized security options divided into these categories:
        - Accounts
        - Audit
        - DCOM
        - Devices
        - Domain Controller
        - Interactive Logon
        - Microsoft Network Client
        - Network Access
        - Network Security
        - Recovery Console
        - Shutdown
        - System Cryptography
        - System Objects
        - System Settings
        - User Account Control

        # Policy Application Order and Troubleshooting

        - Policies can be applied at Domain Level, OU level etc
        - Any settings that do not conflict with other settings will be applied
        - What about conflicting policy settings? Example:
            - Policy at Domain Level states that only admins can shutdown computers
            - Policy at Sales OU level states that Admins and Mgr1 can shutdown computers
            - What is applied is that admins and Mgr1 can shutdown computers in Sales OU but only Admins can shutdown computers not in Sales OU
        - Important to understand the order in which the settings in the group policy should be configured
        - Usual order in which GP are applied is LSDOU: Local, site, domain, OU
        - Settings that conflict will be applied based on the usual order of application, last setting applied is the effective setting
        - Some rules of policies:
            - User policies are more important than computer policies
            - If a policy has blocked inheritance, it does not apply
            - Unless it is enforced, it applies more than all others
            - You should never give a deny permission
            - Group policy loopback can make computer GPOs rule over User GPOs
            - Computer policies are updated every 90-120 minutes after the computer is turned on, User policies are updated every 90-120 minutes after user logs in
        - In Windows Server 2003 and previous versions, settings related to Account Policies can only be set at domain level
        - From Windows Server 2008, we can have different password policies and account lockout policies for different OUs

        ## Policy Application Order (Slide 76 to 80)

        ### Examples

        - ABC Company has a policy at domain level to set every user's desktop to their logo
        - Domain policies will be inherited by all
        - If there are 2 Policies at domain level to set different desktop wallpaper, policy with lowest link order number is applied last
        - SalesOU admin creates a Policy for SalesOU to put latest sales figures as desktop wallpapers, as per LSDOU, OU policy is applied last
        - SalesOU admin can also choose to Block Inheritance, policies will not be inherited
        - Domain Admins can enforce his policy, lower level admins cannot block

        ### To avoid complexity in Group Policies

        - Limit number of Group Policies Objects
        - Minimize use of Block Inheritance and Enforced to avoid complexity

        # Resultant Set of Policy and gpresult

        ## Resultant Set of Policy (RSoP)

        - Used to make implementation and troubleshooting of group policies much simpler for an administrator
        - Can query the existing policies that are in place and then provide reports and the results of policy changes
        - RSoP supports two modes: planning and logging
        - Available within GMPC & Command Line Interface

        ## GPRESULT

        - A command to be run on the workstation to check current accepted and active GPOs