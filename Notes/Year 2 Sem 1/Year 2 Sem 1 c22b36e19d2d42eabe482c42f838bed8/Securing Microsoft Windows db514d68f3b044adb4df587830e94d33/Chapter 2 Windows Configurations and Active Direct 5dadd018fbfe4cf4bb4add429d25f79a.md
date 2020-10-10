# Chapter 2: Windows Configurations and Active Directory Basics

# Learning Objectives

- Use Server Manager to manage a server
- Initial system verification tools
    - Use the Best Practices Analyzer on server roles
    - Use Sigverif to verify important system files
- Understand and configure the Registry
- Understand Active Directory basic concepts
- Install and configure Active Directory
- Implement Active Directory containers

---

# Part 1

# Server Manager

- Consolidates administrative functions to make a server easier to manage

## Installing and Removing Server Roles

- For each server role there are different role services you can choose to include or omit
- Two common roles for Windows Server 2016

### File and Storage Services Role

- Focuses on sharing files from the server or using the server to coordinate and simplify file sharing through Distributed File System (DFS)

### Print and Document Services Role

- Used to manage network printing services and it can offer one or more network printers connected to the network through the server itself

---

# System Verification Tools

## Using the Best Practices Analyzer (BPA) for Server Roles

- Important to determine that you have followed the best practices for the establishment of a role
- BPA can be run to determine if one or more roles are installed and configured to follow the guidelines recommended by Microsoft
- When problems are found, analysis of each role yields a report that shows three levels of severity

### Three Levels of Severity

- Information
- Warning
- Error

### Guidelines BPA uses for Analysis

- Configuration
- Security
- Predeployment
- Postdeployment
- Performance
- BPA Prerequisites

### General Steps for running BPA

- Open Server Manager
- Click Local Server in the left pane
- In the right pane, scroll to Best Practices Analyzer
- Click the down arrow for TASKS
- Click start BPA Scan and wait for scan to complete
- Read results for the scan

## Using System File Checker

### Usage

- Scan system files for integrity
- Scan all system files to verify integrity
- Scan and replace files as needed
- Scan only certain files

## Using Sigverif to Verify System and Critical Files

- Sigverif verifies system and critical files to determine if they have a signature
- After scan is complete, results are written into sigverif.txt
- Only scans files and does not overwrite

---

# Understanding the Windows Server 2016 Registry

## Windows Server 2016 Registry

- Very complex database containing all information the OS needs about the entire server
- The Registry is the coordinating center for a specific server
- Registry editor is launched from Start Button, Run or Command Prompt option as regedit

### Data Contained in the Registry

- Information about all hardware components
- Information about Windows Server 2016 services that are installed
- Data about user profiles and Windows Server 2016 group policies
- Configuration information about all software in use
- Data on the last current and last known setup used to boot the computer
- Software licensing information
- Server Manager and Control Panel parameter configurations

### Precautions when working with the Registry

- Establish a specific group of admins who have privileges to open and modify the Registry
- Only make changes to the Registry as a last resort
- Regularly back up the Registry as part of backing up Windows Server 2016 Windows folder
- Never copy the Registry from one Windows-Based system over the Registry of a different system

### Backing Up The Registry

- Important to have a backup of its contents before working on Registry
- Set a restore point for an easy way to create a backup
- If registry is damaged after working on it, go back to the restore point

## Registry Contents

### Registry

- Made up of keys, subkeys and entries

### Registry Keys

- A category or division of information within the Registry

### Registry Subkeys

- A single key may contain one or more lower-level keys

### Registry entry

- A data parameter associated with a software or hardware characteristic under a key

### Root Key

- Primary or highest level category of data contained in the Registry
- Total of 5 root keys

## Root Keys

### HKEY_LOCAL_MACHINE root key

- Contains information on every hardware component in the server
- Includes information about what drivers are loaded and their version levels, what IRQ lines are used, setup configurations, the BIOS version and more
- A few subkeys stored as a set are called hives, because they hold related information

### HKEY_CURRENT_USER root key

- Contains information about the desktop setup for the account presently signed in to the server console
- is an alias for HKEY_USERS\logged-on user's hive

### HKEY_USERS

- Contains profile information for each user who has logged onto the computer
- Each profile is listed under this root key
- Within each user profile is information identical to that viewed within the HKEY_CURRENT_USER root key

### HKEY_CLASSES_ROOT

- Holds data to associate file extensions with programs
- An alias for HKEY_LOCAL_MACHINE\Software\Classes
- Associations exist for executable, text, graphics, clipboard, audio and many other file types

### HKEY_CURRENT_CONFIG

- has information about current hardware profile
- Holds information about the monitor type, keyboard, mouse and other hardware characteristics for the current profile

---

# Part 2

# Active Directory

- Directory service that houses information about all network resources such as servers, printers, user accounts, group of user accounts, security policies and other information
- Responsible for providing a central listing of resources and ways to quickly find and access specific resources and for providing a way to manage network resources
- Windows Server 2016 uses Active Directory to manage accounts, groups and many more network management services

## Domain Controllers (DC)

- Servers that have the AD DS server role installed
- Contain writable copies of information in Active Directory

## Member Servers

- Servers on a network managed by Active Directory that do not have Active Directory installed

## Domain

- Container that holds information about all network resources that are grouped within it
- Every resource is called an object

## Multi-master Replication

- Each DC is equal to every other DC in that it contains the full range of information that composes Active Directory
- If information on one DC changes it is replicated to all other DCs

## Efficient Replication of AD in WinServer 2016

- Replicate individual properties instead of entire accounts
- Replicate Active Directory on the basis of the speed of the network link

## Schema

### Active Directory Schema

- Defines the objects and the information pertaining to those objects that can be stored in Active Directory

### Examples of Object Classes

- User accounts
- Computers
- Groups

### Caveat

- Replication between Domain Controllers require the involved parties to be having an identical Active Directory schema

## Global Catalog

- Stores information about every object within a forest
- The first DC configured in a forest becomes the global catalog server

### Global Catalog Server

- Store a full replica of every object within its own domain and partial replica of each object within every domain in the forest
- Enables forest-wide searches of data
- Any DCs can be a global catalog server
- Should have more than one for redundancy

### Global Catalog Server Purposes

- Serving as the central storehouse of key object information in a forest that has multiple domains
- Providing lookup and access to all resources in all domains
- Providing replication of key Active Directory elements
- Keeping a copy of the most used attributes for each object for quick access

## Namespace

- Active Directory uses DNS, there must be a DNS server on the network that AD can access
- A logical area on a network that contains directory services and named objects
- Has the ability to perform name resolution
- Two kinds of namespaces — Contiguous and disjointed

### Contiguous Namespace

- Child object contains name of parent object

### Disjointed Namespace

- Child object does not resemble name of parent object

---

# Part 3

## Active Directory Structure

### Forests

- Consists of one or more AD trees that are in a common relationship
- Two-way transitive trusts are automatically configured between domain within a single forest
- Forests provide a means to relate trees that use a contiguous namespace in domains within each tree
- All trees and domains share the same schema and global catalog

### Trees

- Contains one or more domains that are in a common relationship
- Domains are represented in a contiguous namespace and can be in a hierarchy
- All domains in a single tree use the same schema for all types of common objects
- Two-way trust relationships exist between parent domain and child domains
- Because of trust relationship between parent and child domains, any one domain can have access to the resources of all others

### Domains

- A logical partition within an AD forest
- Grouping of objects that typically exists as a primary container within AD
- To provide an AD partition in which to house objects that have a common relationship, particularly in terms of management and security
- To establish a set of information to be replicated from one DC to another
- To expedite management of a set of objects

### Organizational Units

- Offers a way to achieve more flexibility in managing the resources associated with a business unit, department or division
- Grouping of related objects within a domain so that they can be administrated using the same group policies
- OUs can be nested within OUs
- When creating OUs, keep three concerns in mind:
    - Microsoft recommends that you limit OUs to 10 levels or fewer
    - AD works more efficiently when OUs are set up horizontally instead of vertically
    - The creation of OUs involves more processing resources because each request through an OU require CPU time

### Site

- TCP/IP based concept within AD that is linked to IP subnet
- A site reflects one or more interconnected subnets and the physical aspect of the network
- Used for DC replication and used to enable a client to access the DC that is physically closest
- Is composed of only two types of objects, servers and configuration objects
- Sites are based on connectivity and replication functions
- Advantage of a site it that it sets up redundant paths between DCs
- Reasons to define a site:
    - Enable a client to access network servers using most efficient physical route
    - DC replication is most efficient when AD has information about which DCs are in which locations

### Bridgehead

- Bridgehead is a DC designed to have the role of exchanging replication information
- Only one bridgehead server is set up per site

## Active Directory Guidelines

- Keep AD as simple as possible, plan the structure before implementing it
- Implement the least number of domains possible and only one domain on most small networks
- Use OUs to reflect the organization's structure
- Create only the number of OUs that are absolutely necessary and not more than 10 levels of OUs
- Use domains as partitions in forests to demarcate commonly associated accounts and resources governed by group and security policies
- Implement multiple trees and forests only as necessary
- Use sites in situations where there are multiple IP subnets and multiple geographic locations

## Security Configuration Wizard

### Definition

- Steps you through analyzing and configuring security settings on a server
- SCW examines the roles a server plays and then tries to adjust security settings to match these roles
- SCW allows the administrator the choice of applying the adjustment immediately or not

### Usage

- Disable unnecessary services and software
- Close network communication ports and other communication resources that aren't in use
- Examine shared files and folders to help manage network access through access protocols
- Configure audit policy

### Components

- GUI Interactive Wizard
- Database
- Command Line Tool called scwcmd
- Security Configuration Database (Group of XML files that establish a security policy)