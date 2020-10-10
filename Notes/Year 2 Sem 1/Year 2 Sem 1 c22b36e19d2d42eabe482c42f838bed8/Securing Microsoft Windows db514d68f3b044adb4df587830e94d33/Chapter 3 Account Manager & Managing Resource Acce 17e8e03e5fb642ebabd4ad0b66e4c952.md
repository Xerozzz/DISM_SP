# Chapter 3: Account Manager & Managing Resource Access

# Learning Objectives

- Create and manage user accounts
- Configure and use security groups
- Set up security for folders and files
- Configure shared folders and shared folder security
- Important features in Windows Server 2016 Active Directory
- Introduction to user profiles

---

# Part 1

# User Account Management

## Default Accounts

- Administrator
- Guest

## Two General Environment to set up an account

### Local User Accounts

- Accounts set up through a stand-alone server that does not have AD installed

### Domain User Accounts

- Accounts set up in a domain when AD is installed
- Can be used to access any server or resource in the domain

## Managing Accounts

### Disabling Accounts

- Based on security concerns and company policies
- When a user takes a leave of absence
- When someone leaves and will have a replacement
- Should disable accounts for some time before deleting for purposes of digital forensics

### Moving Accounts

- When employees move from one department to another
- Move accounts from one container or OU to another

### Resetting Passwords

- Admin cannot see a user's password but can reset it
- Have specific guidelines that govern the circumstances which an account password can be reset

### Deleting an Account

- Good practice to delete accounts no longer in use
- Failure to do so can expose company to security risks
- Globally Unique Identifier (GUID) not reused even if account is deleted

## Active Directory Recycle Bin

- By default is off
- Once enabled, irreversible

# Security Group Management

## Definition

- For resource permissions management, one of the best ways to manage accounts is by grouping accounts that have similar characteristic
- All of the groups can be used for security or distribution groups

## Scope

- The reach of a group for gaining access to resources in AD

## Type of Groups

- Local
- Domain Local
- Global
- Universal

### Security Groups

- Used to enable access to resources on a stand-alone server or in AD
- The resources access permission is simply implement via group membership

### Distribution Groups

- Used for email or telephone lists, to provide quick, mass distribution of information

## Properties of Groups

### You can configure the properties of a specific group through:

- Local Users and Groups for local groups
- Active Directory Users and Computers for domain groups

### Properties Configured Using Tabs

- General
- Members
- Member of
- Managed By

## OU vs Security Membership

- Group policies are applied to OUs
- Delegation of authority are applied to OUs
- Security groups are used to assign file and folder permissions, shared folder permissions, and any type of resources permission

## Implementing Local Groups

### Definition

- Used to manage resources on a stand-alone computer not part of a domain and on member servers in a domain
- Instead of installing AD, you can divide accounts into local groups
- Each group would be given different security access based on the resources at the server

## Implementing Domain Local Security Group

### Definition

- Used when AD is deployed
- Typically used to manage and provide access to resources
- Grants access to servers, folders, shared folders and printers
- Put domain local groups in access control lists only

### Membership Capabilities

![Chapter%203%20Account%20Manager%20&%20Managing%20Resource%20Acce%2017e8e03e5fb642ebabd4ad0b66e4c952/Untitled.png](Chapter%203%20Account%20Manager%20&%20Managing%20Resource%20Acce%2017e8e03e5fb642ebabd4ad0b66e4c952/Untitled.png)

## Implementing Global Groups

### Definition

- Intended to contain user accounts from a single domain
- Can also be set up as a member of a domain local group in the same or another domain
- Can contain user accounts and other global groups from the domain in which it was created
- Can be converted to a universal group as long as it is not nested in another global group or universal group
- Used to give accounts access to resources in the same or in another domain and then making the global group in one domain a member of a domain local group in the same or another domain

### Nested Global Groups

![Chapter%203%20Account%20Manager%20&%20Managing%20Resource%20Acce%2017e8e03e5fb642ebabd4ad0b66e4c952/Untitled%201.png](Chapter%203%20Account%20Manager%20&%20Managing%20Resource%20Acce%2017e8e03e5fb642ebabd4ad0b66e4c952/Untitled%201.png)

## Implementing Universal Group

### Definition

- Provide a means to span domains and trees
- Membership can include user accounts from any domain, global groups from any domain and other universal groups from any domain
- Offered to provide an easy means to access any resource in a tree or among trees in a forest

## Guidelines to Simplify Group Usage

- Use global groups to hold accounts as members
- Use domain local groups to provide access to resources in a specific domain
- Use universal groups to provide extensive access to resources

## Implementing Security Groups and Resources Permissions

### Best Practices

- AGDLP
- AGUDLP

### Meanings

- A - Account
- U- Universal
- G- Global
- DL - Domain Local
- P - Permissions

### Group/Resource Permission Approaches

- AP
- AGP
- AUP
- AGUP
- The shorter the distance of A to P, the easier to create and but more error-prone and harder to maintain

### Case Study

- Scenario: To give 5 users access to a particular printer
- Create a domain local group and assign it with permission to access the printer
- Put 5 users in a global group and add the global group to the printer domain local group
- If the printer changes, assign the domain local group with permission to access new printer
- All members of the global group will receive access automatically without having to change each of their permissions

---

# Part 2

# Managing Folder and File Security

## Creating accounts and groups

- The next step is to create ACLs to secure these objects and then set them up for sharing

## Discretionary ACL (DACL)

- An ACL that is configured by a server administrator or owner of an object

## System ACL (SACL)

- Contains information used to audit the access to an object

## DACL and SACL controls for Folders and Files

- Attributes
- Permissions
- Auditing
- Ownership

# Configuring Folder and File Attributes

## Attributes stored as header information with folder and file

- Volume label, designation as a subfolder, date and time of creation

## Two basic attributes in NTFS compatible with FAT

- Read-only and hidden
- On the general tab in an NTFS folder's or file's properties dialog box

## Advanced Attributes of NTFS

### Archive

- Indicates that the folder of file has been changed recently or is new and needs to be backed up
- File server backup systems can be set to detect files with archive attribute to ensure only those files are backed up, saves time

### Index

- The NTFS index attribute is used to index the folder and file contents so that file properties can be quickly searched in Windows Server 2016 through the Indexing Service
- WinServer 2016 offers newer and faster search service called Windows Search SErvice
- To use Windows Search Service, must install the File and Storage Services role via Server Manager

### Compress

- A folder and its contents can be stored on the disk in compressed format
- Compression saves space and you can work on compressed files in the same way as on uncompressed files
- Compressed files increase CPU overhead to open files and copy them
- If you compress you cannot encrypt

4 Best Practices:

- Busy servers that experience high-volume write or execute operations are poor candidates for the use of compression
- Servers that are rarely busy or that primary have read traffic are acceptable candidates
- Files that are rarely accessed or that are archived on the server can be candidates
- User home folders on a server typically have high levels of read and write activity and generally should not be compressed

### Encrypt

- Protects folders and files so that only the user who encrypts the folder or file is able to read it
- Encrypted file or folder uses Microsoft Encrypting File System (EFS)
- A unique private encryption key associated with the user account that encrypted the folder or file
- EFS uses both symmetric and asymmetric encryption technique
- When you move an encrypted file to another folder on the same computer, that file remains encrypted, even if you rename it
- If your encrypt you cannot compress

## 4 Best Practices for using EFS:

- Move files for encryption into specifically designated folders flagged for encryption
- Safer to encrypt the whole folder instead of individual files
- Workstation users and server administrators should consider encrypting the My Document or Document folders on their systems
- Users and server admins should frequently export certificates and private keys to portable media and store the media in a secure place

# Configuring Folder and File Permissions

## Permissions

- Used to control access to an object, such as a folder or file
- Example: Used to configure a folder so that a domain local group has access to only read the contents of that folder
- At the same time you are configuring the folder's DACL of security descriptors

## Type of Permissions

- Full Control
- Modify
- Read & Execute
- List folder contents
- Read
- Write

## Customized Permissions

- You can set up special permissions for a particular group or users
- Uses 14 individual permissions

## Best Practices for setting permissions

- Protect the \Windows folder that contains OS files
- Protect server utility folders and only allow Administrators
- Create publicly used folders to have modify access
- Provide users full control of their own home folders
- Remove unnecessary access groups from confidential folders
- Use Deny sparingly

# Configuring Folder and File Auditing

## Auditing

- Enables you to track activity on a folder or file
- Creates an audit log

# Configuring Folder and File Ownership

## Definition

- Folders are first owned by the account that creates them
- Folder owners have the ability to change permissions for the folders they create
- Ownership can be transferred only by having the Take ownership advanced permission or Full Control permission
- Take ownership permissions gives full control permission at any time the user wants

# Configuring Shared Folders and Shared Folder Permissions

## Definition

- A folder can be set up as a shared folder for users to access over the network
- Configuring a shared folder includes features so that the person configuring a share is more aware of security options
- Sharing a folder or file consists of first enabling sharing

## Enabling Sharing

- Make sure folder/file and printer sharing is turned on
- Network discovery can be turned on
    - The ability to view other network computers and devices

# Configuring Folder/File Sharing Through the Folder/File Properties

## Share Permissions for Folder or File

- Can be set by configuring sharing using the File Sharing window and a folder's or file's sharing tab in its properties dialog box
- Share permissions also include Full control and Change
- Configured using the Advanced Sharing button on the Sharing tab of Properties

## Share Permissions

- Read
- Write
- Change or Contribute
- Custom
- Full Control
- Owner

## Folder Caching

- To make contents of a shared folder available offline
- Offline files that have been modified can be synchronized with the network versions of the files

### 3 Ways to Cache

- Only the files and programs that users specify will be available offline
- No files or programs from the shared folder are available offline
- All files and programs that users open from the shared folder are automatically available offline

### Access-based Enumeration

- Permits the user to view only files and folders for which they have permissions
- Used to hide a shared folder, can also use $ sign to hide folders

# Configuring Sharing Through Server Manager

## Server Manager

- Another way to configure folder and file permissions and share permissions
- Offers an interface for managing permissions and shares from one tool
- There are more easily accessed options for share management

## Server Message Block (SMB) Protocol

- Enables an OS to offer shared files, folders, printers, serial ports and other port communications on a network

## Network File System (NFS) Protocol

- Used for file and folder sharing on UNIX and Linux systems
- When installed on a Windows system share, enables it to be accessed by UNIX and Linux computers

## File Server Resource Manager Role Service

- Allows you to set folder quotas

# Publishing a Shared Folder in Active Directory

## Publishing an Object

- Means to make it available for users to access when they view AD contents
- Makes it easier to find when a user searches for that object
- When you publish an object, can be shared for domain-wide access or shared and managed through an OU

---

# Part 3

# Troubleshooting a Security Conflict

## Effective Access

- Windows Server 2016 offers the Effective Access tab in the properties of a folder or file
- helps to troubleshoot permissions conflicts
- Using the above, you can view the effective permissions assigned to a user or group
- The calculation will take into account group membership as well as permission inheritance
- Take into account what happens when a folder or files in a folder are copied or moved

## Ways File or Folder Permissions Can Be Affected When Created, Copied or Moved

- A newly created file inherits the permissions already set up in a folder
- A file that is copied from one folder to another on the same volume inherits the permissions of the folder to which it is copied
- A file or folder that is moved rom one folder to another on the same volume takes with it the permissions it had in the original folder
- A file or folder that is moved or copied to a folder on a different volume inherits the permissions of the folder to which it is moved or copied
- A file or folder that is moved or copied from an NTFS volume to a folder in a FAT or FAT32 volume is not protected by NTFS permissions
- A file or folder that is moved or copied from a FAT volume to a folder in an NTFS volume inherits the permissions already assigned in the NTFS folder

# Combining NTFS and Shared Folder Permissions

- If John has NTFS Modify permission to the Reports folder
- He is given Reader Share permission to the Reports folder
- If he logs in locally to the system and accesses Reports folder, he can modify it as only the NTFS permission applies

# 5 Important Features in WinServer 2016 AD

## Restart Capability

- If he accesses Reports folder over the network, he has only Read permission, which is the more restrictive permission of NTFS and Share
- WinServer 2016 provides the option to stop AD Domain Services without taking down the computer
- After your work is done on AD, you simply restart AD Domain Services

## Read-Only Domain Controller

- Used to provide better security at branch locations where physical security measures may not be as strong as at a central office
- You cannot use it to update information on AD and does not replicate to regular DCs
- Can still function as a Key Distribution Center for the Kerberos authentication method
- Can also be configured as a DNS server

## Cloning Domain Controllers

- Used for easier deployment of multiple domain controllers in an environment with multiple virtual machines
- Cloning cuts down on the steps required to create additional virtual domain controllers
- Server admin can configure AD an then create a copy of the virtual DC
- Additional steps can be handled by running PowerShell cmdlets and using a PowerShell script to define configuration parameters

## Fine-Grained Password Policy Enhancement

- Different security groups can have different password policies
- Windows Server 2012 R2 introduced the ability to use AD Administrative Center for managing password setting objects in the AD Schema
- Makes server access more secure
- Helps reduce errors made by server administrators when working with fine-grained passwords

## Protected Users Global Group

- Enforces strict locked-in security and protection measures that cannot be reconfigured
- Only way to change the security for a member of this group is to remove him from the group
- User accounts, computers, printers and servers can be members of this group

### Security Restrictions That Apply To Members Of This Group

- Group members cannot use weaker forms of authentication
- The Kerberos Ticket Granting Ticket's lifetime is limited to 4 hours, which means group member must be authenticated every 4 hours
- Connections to system that do not utilize this global group may not succeed
- Only higher-level encryption methods compatible with Kerberos security can be used

# Implementing User Profiles

## Definition

- A local user profile is automatically created at the local computer when you log on with an account for the first time
- The profile can be modified to consist of desktop settings that are customized for one or more clients who log on locally

## Advantages

- Multiple users can use the same computer and maintain their own customized setting
- Profiles can be stored on a network server so they are available to users regardless of the computer they use to log on
- Profiles can be made mandatory so users have the same settings each time they log on

## Setting Up A User Profile

- Set up a generic account on the server with the desired desktop configuration
- Then copy the Ntuser.dat file to the \Users\Default folder in WinServer 2016

## Setting Up A Roaming Profile

- Set up a generic account and customize the desktop
- Set up the user to access a profile by opening the Profile tab in each user's account properties and entering the path to that profile