# Chapter 3: System Security II

Created: Jan 20, 2020 10:26 AM
Updated: Jan 20, 2020 12:31 PM

**Objectives:**

- List the steps for security a client device
- Define application security
- Explain how physical security can be used for protection

**Client Security:**

- Hardware system security
- Securing the operating system software
- Protecting peripheral devices connected to client

**Hardware System Security:**

Secure Booting Tools:

- BIOS (Basic Input/Output System):
    - Firmware used on early computers to hold the boot process
    - Ability to update the BIOS with a firmware update opened the door for a threat actor to create malware to infect BIOS
- UEFI (Unified Extensible Firmware Interface)
- Secure Boot security standard
- When UEFI and Secure Boot:
    - The computer check the digital signature of each piece of boot software
    - If signatures are deemed valid the computer boots
    - Computer does not boot

Hardware Root of Trust:

- Chain of trust:
    - Each element of the boot process relies on the confirmation of the previous element to know that the entire process is secure
- Hardware root of trust:
    - Strongest starting point is hardware, which cannot be modified
- Security checks are "rooted" in hardware checks

Electromagnetic Spying:

- It is possible to pick up electromagnetic fields and read data that is producing them
- US government has developed a classified standard TEMPEST to prevent attackers from pricking up electromagnetic fields emitted from government building

Supply Chain Infections:

- Different steps in the supply chain has opened door for malware to be injected into products at different stages, such as manufacturing or storage
- If malware is planted in ROM of device, hard to remove
- Users may be purchasing infected device with no knowledge
- Cannot be easily purchased

**Securing OS Software:**

Type of OS:

- Network OS:
    - Software that runs on a network device, such as router or firewall
    - Eg. Cisco Internetwork OS
- Server OS:
    - OS Software that runs on a server to provide resources to network users
    - Eg. Microsoft Windows Server, Apple macOS Server, Red Hat Enterprise Linux
- Workstation OS:
    - Software that manages hardware and software on a client computer
    - Eg. Microsoft Windows, Apple Mac OS, Ubuntu Linux
- Appliance OS:
    - OS in firmware that is designed to manage a specific device like a digital video recorder or game console
    - Eg. Linpus Linux
- Kiosk OS:
    - System and user interface OS to provide an interactive kiosk
    - Eg. Kioware, Microsoft Windows, Apple IOS
- Mobile OS:
    - OS system for mobile phones, tablets and handheld devices
    - Eg. Android, Apple iOS, Microsoft Windows Mobile

OS Security Configuration:

- Typical OS configurations:
    - Disabling unnecessary ports and services
    - Disabling default accounts/passwords
    - Employing least functionality/privilege
    - Application whitelisting/blacklisting
- Use templates and tools to automate creating the same security configuration on each computer

Patch Management:

- Security Patch
    - Software security update to repair discovered vulnerabilities
- Feature Update
    - Includes enhancements to software to provide new or expanded functionality
- Service Pack
    - Accumulates security updates and additional features
- Patch Management Tools
    - Tools for patch distribution
    - Patch reception
- Automated Patch Update Service (Patch Distribution)
    - Manages patches locally instead of relies on vendor's online update service
    - Downloading patches from a local server can save bandwidth and time
    - Admins can approve or decline updates, force updates to install by specific dates and obtain reports on what update each computer needs
    - Admins can approve updates for "detection" only, allows them to see which computer needs update without actually installing it
- Patch Reception
    - Most patches are automatically downloaded and installed to ensure software is always up-to-date
    - Microsoft security update procedures
        - Forced Updates
        - No Selective Updates
        - More Efficient Distribution
        - Up-to-Date resets

Anti-Malware:

- Antivirus
    - Software that examines a computer for infections
    - Scans new documents that might contain viruses
    - Searches for known virus patterns
    - Weakness - Vendor must continually search for new viruses, update and distribute
    - Heuristic Monitoring (dynamic analysis) - Uses a variety of techniques to spot characteristics of a virus instead of attempting to make matches
    - Code Emulation - A HM technique to execute questionable code in a virtual environment
- Antispam
    - Mail Gateway - Monitor emails for spam and other unwanted content
    - Spam filtering methods:
        - Blacklist/Whitelist
        - Blocking certain file attachment types
        - Bayesian Filtering - Divides emails into two piles, spam and non spam
- Antispyware
    - Helps prevent computers from being infected by different types of spyware
    - Pop up blockers
- OS Hardening
    - Tightening security during the design and coding of OS
    - Trusted OS - OS designed through OS hardening
    - Least Privilege
        - Remove all admin or superuser accounts that can bypass security and provide least privilege to each user
    - Reduce capabilities
        - Significantly restrict what resources can be accessed and by whom
    - Read-Only file system
        - Important OS files cannot be changed
    - Kernel Pruning
        - Remove unnecessary features that may compromise the OS

**Physical Security:**

- External perimeter defenses
- Internal physical access security
- Security for protecting the hardware device itself

**External Perimeter Defenses:**

Fencing:

- Tall permanent structure, tall fences
- Equipped with other deterrents such as proper lighting and signage

Cage:

- Fenced secure waiting area
- Eg. To contain visitors to a facility until they are approved for entry

Barricade:

- Large concretes ones should be used

Bollard:

- Short but sturdy vertical post that is used to prevent cars from ramming into secured area

Security Guards:

- Considered active security element
- Uses CCTV (closed circuit television) to monitor security

Motion Detection:

- Determining an object's change in position in relation to its surroundings
- Eg.
    - Visual - CCTV
    - Radio Frequency - Radar, Microwave
    - Vibration - Seismic Sensors
    - Sound - Microphones
    - Magnetism - Magnetic Senors

**Internal Physical Access Security:**

Door Locks:

- Standard Keyed locks provides minimal security
- Deadbolt locks provide additional security and require a key to both open and lock the door
- Cipher locks are combination locks that use buttons that must be pushed in a proper sequence
    - Can be programmed to allow individual's code to be valid on specific date and times
- Key Management Procedures:
    - Keep track of keys issued and require users to sign their names when receiving keys
    - Receive proper approvals of supervisors or other superiors before issuing
    - When making duplicates of master keys, mark them "Do not Duplicate" and wipe out manufacturer serial numbers
    - Change locks upon loss or theft of keys
    - Secure unused keys in a locked safe

Access Logs:

- Access List
    - Record of individuals who have permission to enter secure area and the time they enter and left
- Electronic access logs

Mantraps:

- Separates secure area from non secured
- Monitors and controls two interlocking doors, only one door may open at a time
- Used at high-security areas where only authorised persons can enter
    - Eg. Cash handling areas, research labs

Protected Distribution Systems (PDS):

- Cable conduits used to protect classified information that is being transmitted between two secure areas
- Two Types:
    - Hardened Carrier PDS - Conduit constructed of special electrical metallic tubing
    - Alarmed Carrier PDS - Specialised optical fibers in the conduit that sense acoustic vibrations that occur when an intruder attempts to gain access

**Computer Hardware Security:**

Safe or Secure cabinet:

- Prewired for power and network connetion
- Allows devices to charge while stored as well as update

Application Security:

- Application Development security
- Secure Coding Techniques
- Code Testing
- Virtualisation