# Chapter 5: Planning and Deploying Patch Management

# Part 1

# Planning Deployment of Service Packs and Hotfixes

- Need to keep technology environment secure and reliable
- Requires identifying security vulnerabilities and responding quickly

## Patch Management

- Method for keeping computers up to date with new software releases

## Security Patch Management

- Patch management with a concentration of reducing security vulnerabilities, is essential for secure IT management and operations

## How to manage updates

- Microsoft Update and Automatic Updates
- Windows Server Update Services (WSUS)
- Microsoft Endpoint Manager

### Microsoft Update and Automatic Updates

- For consumers and small businesses with less than 50 computers
- Updates can be installed with minimal to no user interaction
- Uses Internet connection to search for downloads from Microsoft Update website
- No need to understand the technical details of the security update
- Simplest and free approach for client systems that do not run mission critical services/
- May affect applications during update so not ideal for enterprises

### Windows Server Update Services (WSUS)

- For medium or large businesses
- Admins can manage update settings and control the distribution of updates
- Admins can test updates on selected computers before deploying to the rest of the network
- Updates can be downloaded from Microsoft Update Website and stored on local server to free up Internet bandwidth during mass updating
- Does not support deployment of non-Microsoft updates
- Free approach that is good for updating mission critical systems

### Microsoft Endpoint Manager

- Supports management and distribution of Microsoft and non-Microsoft software updates and applications
- Supports various types of endpoints like windows or non-windows platforms
- WSUS is part of it
- Advanced administrator control features
- Not free, charges apply
- Alternatives include Freshservice and Rippling

## Additional Resources

### Security Update Guide

- Formally known as Security Bulletin
- Contains detailed guidance and information about the security update and the vulnerability
- Supporting search / filter feature to locate specific entries

### Microsoft Technical Security Notifications

- Free of charge notification services for sign-up users
- Security update email alerts provide new or major revisions of Microsoft product security content
- Security advisories alerts to help admins to plan for upcoming security updates

## Getting Updates from Microsoft Website Only

- Microsoft may send email notifications about security updates
- Users should download updates from Microsoft Update website
- Microsoft does not distribute security updates by using email attachments
- Such emails containing attached "patch installers" are fake and malicious

# Windows Server Update Services (WSUS)

## Advantages

- The system admin can control the updates to be applied
- Clients can be configured to get updates from a local WSUS server instead of downloading them from Microsoft's site, reducing network traffic
- WSUS is a means to provide updates to computers that don't have Internet access

## Features

- Admin must approve updates before WSUS clients can install them
- WSUS clients can be controlled by Group Policy to connect to WSUS Server to check for updates
- After updating, WSUS clients will notify WSUS Server
- WSUS Server can maintain update status of all clients

## Operations To Configure WSUS Server

- Known as synchronization, initial synchronization may take a while depending on the selection choices
- WSUS Server needs Internet access to Microsoft Update Server to get information about security updates

## Performing Software Update Services and Common Administration Tasks

### Synchronization Log

- Time of the last and next scheduled synchronization
- Success and failure notification
- Update packages that have been downloaded and/or updated since last sync, or that filed sync
- Whether sync was a Manual or Automatic

### Approval Log

- Keeps track of content that has been approved or not approved

## Content Synchronization

- During sync, new security updates can be handled in two ways:
    - Automatically approve new versions of previously approved updates
    - Do not automatically approve
- In testing environment, second option is better, otherwise, testers may overlook and skip testing of new updates

## WSUS Policy Options for Clients

![Chapter%205%20Planning%20and%20Deploying%20Patch%20Management%20cdddfcd5ca3b44c282beb7e744f920a4/Untitled.png](Chapter%205%20Planning%20and%20Deploying%20Patch%20Management%20cdddfcd5ca3b44c282beb7e744f920a4/Untitled.png)

# Part 2

## WSUS Computer Groups

- WSUS clients can be placed into Computer Groups
- For eg, some clients can be put into a "Test" Computer Group to apply new updates for testing before applying the update to every other computer
- For eg, Servers with the same roles can be in one group, so all can receive relevant update at the same time

## Patch Management Processes Best Practices

- Make an inventory
- Categorize your systems
- Identify high-priority patches
- Test patches first
- Establish a patching timeline
- Scan for vulnerabilities
- Use automated patching software
- Run patching reports

## Severity Ratings

### Critical

A vulnerability whose exploitation could enable the propagation of an Internet worm with little or no user action

### Important

A vulnerability whose exploitation could result in compromise of the confidentiality, integrity or availability of users' data, or of the integrity or availability of processing resources

### Moderate

A vulnerability whose exploitation is mitigated to a significant degree by factors such as default configuration, auditing, or difficulty of exploitation

### Low

A vulnerability whose exploitation is extremely difficult, or whose impact is minimal

## Managing Updates Through Stages (5+1 Stages)

- Stage 1: Receive Microsoft Security
- Stage 2: Evaluate Risk
- Stage 3: Evaluate Mitigation
- Stage 4: Deploy Updates
- Stage 5: Monitor Systems and Post-Deployment Review

### Stage 1: Receive Microsoft Security

- Microsoft sends out a notification if there is an issue affecting customer's security, received on Email, RSS, Twitter or Website
- If security changes are required, a security update is released
- Urgent updates will be released immediately

### Stage 2: Evaluate Risk

- Does the vulnerability apply to the organization?
- Does the vulnerability represent a risk high to the organization?
- Deployment of security update comes with costs:
    - Cost of testing updates
    - Cost of deploying updates
    - Support costs in case of any negative results after updates

![Chapter%205%20Planning%20and%20Deploying%20Patch%20Management%20cdddfcd5ca3b44c282beb7e744f920a4/Untitled%201.png](Chapter%205%20Planning%20and%20Deploying%20Patch%20Management%20cdddfcd5ca3b44c282beb7e744f920a4/Untitled%201.png)

### Stage 3: Evaluate Mitigation

- While admins are evaluating security updates, some short term security control may be applied
- For example, adjust firewall policies, or restrict a port only to a specific subnet instead of the whole network
- Microsoft may provide some suggested mitigations or workarounds in their security advisories if the security update can not be applied immediately
- Such mitigations and workarounds are meant for short-term use, they do not replace security updates

### Stage 4: Deploy Updates

1. Plan the deployment, determine which updates need to roll out quickly and which ones need more testing. Also decide which computers need it more urgently
2. Determine whether the security update is available for download, if none, Microsoft will advise the actions to take to protect computer systems
3. Obtain required update files from Microsoft Security Guide, WSUS, Windows Update, Microsoft Update, Microsoft Endpoint manager, Microsoft Download Center and more
4. Create the update package if security updates need to be customized
5. Test the package to ensure all business-critical systems will continue to run successfully after security update has been deployed, ensure rollback or uninstallation is possible, ensure the system can be restarted properly and ensure the update is effective. Testing can be done in Test environment or Pilot environment
6. Rolling out deployment and carry them out to computers that need it. Be compliant to the Standard Patch Deployment Timeline

### Stage 5: Monitor Systems

- Determine which systems successfully deployed the update and which systems did not
- Can be done using WSUS or Endpoint Manager features
- If not deployed, need to resolve the problem and get update applied
- Possible reasons why update was not successfully deployed:
    - Computer is offline
    - Computer is being rebuilt or reimaged
    - Computer has insufficient disk space
    - Computer is not communicating with update server
    - Required update client software is not running on the computer
    - Computer is missing some dependent software

### Post-Deployment Review

- Conducted after the deployment to review organization's performance during the incident
- Discuss changes to your service windows
- Assess the total incident damage and cost if any
- Update the existing baseline for your environment

## Common Approaches to Fix Windows Update Errors

- Checking the disk storage as system may not have enough storage left to support the download and installation requirement
- Windows Update Catalog to download the specific update package from windows update catalog web site to install update locally
- Windows Update Troubleshooter, a free tool from Microsoft which can fix most of the common windows update errors