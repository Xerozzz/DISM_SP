# Chapter 5: Wireless Security

Created: Feb 16, 2020 6:59 PM
Updated: Feb 27, 2020 9:48 AM

**Objectives:**

- Describe the benefits of documenting a network and list what elements should be documented
- List the steps of the problem-solving process
- Explain different approaches to network troubleshooting
- Make use of problem-solving resources
- Describe network troubleshooting tools
- Summarize common trouble situations
- Describe disaster recovery procedures

**Documenting Your Network:**

Why should you document your network?:

- Makes equipment moves, adds and changes easier
- Provides needed information or troubleshooting
- Offers justification for additional staff or equipment
- Helps ensure compliance with standards
- Supplies proof that your installations meet hardware or software requirements
- Reduces training requirements
- Facilitates security management
- Improves compliance with software licensing agreements

Change Management:

- When a workstation is moved, you must know which patch-panel and switch ports are currently being used so they can be disconnected
- Without proper documentation, cables must be traced
- Additions made to your network can happen more quickly and with less chance for errors if documentation is up to date
- Change Management - Document reasons for change, the potential impact of a change, notifications, and approval procedures

Troubleshooting:

- Accurate documentation of workstation MAC addresses helps quickly find issues such as IP address conflicts and the source of invalid or excessive frames
- Physical and logical addressing, connectivity to devices, and even data about the cabling should be documented

IT Staffing:

- Documenting the type and frequency of support calls can provide justification for additions to staff or tools to make support more efficient
- Statistics on network response time and bandwidth load as justification for upgrading servers or adding new equipment
- Train new employees on how to properly document additions and changes

Standards Compliance:

- Be sure to document which standards are in use (Eg. 568A or 568B)
- Another reason to document standards compliance when there is dispute between you and equipment vendor about persistent network error

Technical Support:

- When solving a network device problem, some manufacturers of network devices will want to know that your cabling passed appropriate tests as well as other test results
- When calling technical support for a software problem on one of your servers, the manufacturer will most likely want to know the hardware details as well as operating system version and patch installations

Security:

- Documenting security patches and virus protection updates helps you adhere to your security policies and confirms your resistance to current threats

What Should Be Documented:

- Description of the Network
    - Should include network topology, technologies in use, operating systems installed and number of devices and users served
- Cable Plant
    - Describes the physical layout of your network cabling, terminations used, conventions used for labeling cable and equipment, and results of test completed on cable plant
- Equipment room/Telecommunications Closet
    - Document the items in each room and their location
- Internetworking Devices
    - Know what devices are connected to other devices, network management features, port usage, physical and logical addresses, model numbers and hard/software revision numbers
- Servers
    - Document hardware configuration, operating system and application version numbers, NIC information, and system serial and model numbers
- Workstations
    - Hardware and software configuration, physical and logical addresses

**Problem-Solving Process:**

Steps:

- 1. Determine the problem definition and scope
- 2. Gather information
- 3. Consider possible causes
- 4. Devise a solution
- 5. Implement the solution
- 6. Test the solution
- 7. Document the solution
- 8. Devise preventative measures

Step 1: Determine the Problem Definition and Scope:

- Defines what does work and what doesn't work
- Know who and what are affected by the problem
- Assign priority after defining problem
- Questions to ask
    - Is anyone else near you having same problem?
    - What about other areas of the building?
    - Is the problem occurring with all applications or just one
    - If you move to another computer, does the computer occur there as well?
- Examples
    - Mike can't access email server, other servers are available to Mike, no one else reports problem
    - Third-floor uses can't connect to network but others can

Step 2: Gather Information:

- Questions
    - Did it ever work?
    - When did it stop working? How often? Other apps too?
    - Was anything changed?
    - Any obvious clues? Unplugged cables etc
- Define how it is supposed to work
    - Have good documentation and clear baseline of network
    - Include network utilization stats on network, server CPUs, memory, hard drives and other resources as well as normal traffic patterns
    - Eg. If utilization increases for many months, prepare for upgrade

Step 3: Consider Possible Causes:

- Create a checklist of possible things that could have gone wrong
- Eg. An area of building lost connection, but none other affected
    - Connection in main wiring closet to rest of network failed
    - Switch to all workstations failed
    - All workstations has a virus that prevents network connection
    - Major upgrade made to the all workstations with wrongly network addresses configured

Step 4: Devise a Solution:

- Questions
    - Is identified cause of problem truly the case, or just a symptom?
    - How to test proposed solution adequately?
    - What results and ramifications in proposed solution?/
- Might need to
    - Save, document and back up all network,workstation and wiring closet configs
    - Conduct a final baseline to compare new and old results

Step 5: Implement the Solution:

- Create immediate testing opportunities, testing small steps in which a limited things could go wrong is easier than testing a complex solution with lots of problem areas
- Inform users of possible disruption to some network solutions
- Put plan into action and take note about every change made

Step 6: Test the Solution:

- Attempt to emulate a real-world situation as closely as possible
- If testing workstation problem
    - Attempt to logon to network as a user with similar privileges as the main users
    - Next, attempt to access applications that would run from that application
- If testing network upgrade
    - Start some workstation on the upgraded part of the network and run some network-intensive applications
    - Gather information on how network behaves and compare with results before upgrade

Step 7: Document the Solution:

- Documentation should include
    - Problem Definition
    - Solution
    - Implementation
    - Testing
- If the problem and solution have implications for whole network, include this information

Step 8: Devise Preventive Measures:

- After solving problem, do everything you can to prevent recurrance
- Eg.
    - If problem was a virus that spread throughout the network, install anti-virus and tighten security policies
- Devising preventive measures is proactive than reactive network management

**Approaches to Network Troubleshooting:**

Trial and Error:

- Requires an assessment of the problem, an educated guess to solution and a test of results
- Used under following conditions
    - System is newly configured, no data can be lost
    - System not attached to live network
    - Changes can be undone easily
    - Other approaches more time-consuming in this case
    - There are few possible causes of problem
    - No documentation and other resources are available to arrive at a more scientific solution
- Do not use under these conditions
    - Server or internetworking device is live on network
    - Problem is being discussed over phone and you are instructing an untrained user
    - You aren't sure of consequences of solutions you propose
    - No way to undo changes made
    - Other approaches take same or less time
- Follow these guidelines
    - Make only one change at a time before testing the results
    - Avoid making changes that might affect the operation of a live network
    - Document the original settings of hardware and software before making changes
    - Avoid making a change that can destroy user data
    - If possible,avoid making changes that cannot be undone

Solve by Example:

- Comparing something that doesn't work with something that does
- One of the easiest/fastest ways to solve problems
- General rules to follow
    - Use only when working sample has similar environment as the problem machine
    - Don't make config changes that will cause conflicts, do not use same addresses on both machines
    - Dont make any changes that can destroy data

The Replacement Method:

- Requires narrowing down possible sources of the problem and having known working replacement parts on hand to replace
- Follow these rules
    - Narrow list of potentially defective parts down to a few possibilities
    - Make sure correct replacement parts are on hand
    - Replace one part at a time only
    - If first replacement does not fix problem, reinstall original part before next replacement

Step by Step with OSI Model:

- Test problem starting from Application layer and keep testing each layer down until successful or reach Physical layer
- Can be the other way round too
- Must understand how networks work and which tools to use for this approach

**Making Use of Problem-Solving Resources:**

Experience:

- Make the most of your experience, take notes and learn
- If it happened once, it can happen again
- Colleagues experience
- Experience manufacturer's technical support

Internet:

- Most manufacturers create databases of problems and solutions so their customers can research problems themselves
- Be as specific as possible and enclose error messages in quotation marks
- When installing new device or OS, check whether bug fixes, driver updates or new firmware revisions are available
- Consult online support services and newsgroups
- Online Periodicals and Networking Journals

Network Documentation:

- Documentation should read like a user's manual for network admins
- Include network diagrams to show logical and physical picture of network and its aspects
- Include model and serial numbers, location, IP addresses, MAC addresses and number of ports for each internetworking device

**Network Troubleshooting Tools:**

Tools:

- Ping and Trace Route
- Network Monitors
- Protocol Analyzers
- Time-Domain Reflectometer (TDR)
- Basic Cable Tester
- Advanced Cable Tester
- Multimeter
- Tone Generator and Probe
- Optical Power Meter

Ping and Trace Route:

- ping command tells you whether your computer can communicate with another using IP
    - With successful reply, you know target machine is running and path to the computer can be established
    - Also tells you the amount of time to receive a reply
- Use ping to verify Network Layer connectivity
    - Run ipconfig/all to display IP config
    - Ping loopback address to check if IP protocol working properly
    - Ping local IP address to verify computer can receive ICMP packets
    - Ping default gateway to check gateway
    - Ping IP address of host to verify if you can communicate using ICMP of target computer
    - Ping hostname to verify hostname can be resolved
    - Ping DNS servers to check if your computer can communicate with DNS services
    - Use NSlookup to verify DNS server can resolve name of host you are trying to communicate with
- Use tracert
    - tracert does a reverse DNS lookup on IP address of each router and displays its name
    - Response times can help determine if there is bottleneck between source and destination
    - Can also be used to confirm network design

Network Monitors:

- Software packages that track all or part of network traffic
- Can track packet type, errors and traffic to and from each computer
- Can generate reports and graphs
- Sometimes can email admins when problem is detected

Protocol Analyzers:

- Allows you to capture packets and analyze network traffic from each protocol
- Can be used to troubleshoot problems related to DNS, Authentication, DHCP, IP addressing, remote access etc...
- Can be used to create baseline for network performance
- Most advanced analyzers combine hardware and software in a self-contained unit

Time-Domain Reflectometer (TDR):

- Used to determine whether there is a break or short in cable and measure its length
- TDR sends electrical pulse down the cable and reflects back when encounters a short or break
- Measures time taken for signal to return to determine length of cable and location of fault
- TDR should be used to document actual length of cables

Basic Cable Testers:

- Usually less than $100
- Only test correct termination of TP cable or continuity of coaxial cable
- Great for checking patch cables and testing correct termination at patch panel and jack
- Cannot check for attenuation, noise or other performance problems

Advanced Cable Testers:

- More expensive than TDRs and basic testers
- Performs several tests for crosstalk, EMI, attenuation and impedance mismatches
- Can measure frame counts, collisions, CRC errors and broadcast storms
- Costs a few thousand dollars

Additional Tools:

- Multimeter
    - Measure voltage, current and resistance on a wire
- Tone Generator and Probe
    - Generator issues an electrical signal and a probe to detect signal and emits a tone
    - Useful for locating a wire that might be in bundle of other wires
- Optical Power Meter (OPM)
    - Used to measure amount of light on a fiber-optic circuit
    - Used to determine signal loss on fiber-optic cable between transmitter and receiver

**Common Troubleshooting Situations:**

Cabling and Related Components:

- First step is to determine whether problem is cable or computer, check by connecting another computer to cable
- Verify right type of cable for connection is used and terminated correctly
- Check back of NIC to see if it has indicator lights, if no lights, swap out NICs

Power Fluctuations:

- Verify servers are up and running
- Use UPSs with battery power so they can be shut down without data loss f power supply is cut

Upgrades:

- When network upgardes are performed
- Keep current and do one upgrade at a time
- Test any upgrade before deploying to actual network
- Tell users about upgrades before implementation

Poor Network Performance:

- What has changed since last time network functioned properly?
- Has new equipment or applications been added to network?
- Is someone or something causes interference to network?
- Are there too many users?
- Could be time to upgrade and expand the network

**Disaster Recovery:**

Backup Procedures:

- Determine what data should be backed up and how often
- Develop schedule for backing up data
- Identify people responsible for performing backups
- Test backup system regularly
- Maintain a backup log listing what data was back up, when the backup took place, who performed the backup, and what media was used
- Develop a plan for storing data after it has been backed up
- Backup Types
    - Full backup
        - Copies all selected files to selected media and marks files as backed up
    - Incremental Backup
        - Copies all files changed since last full or incremental backup and marks files as backup
    - Differential Backup
        - Copies all files since the last file backup, doesn't mark files backed up
    - Copy Backup
        - Copies selected files to the selected media without marking files as backed up
    - Daily Backup
        - Copies all files changed the day the backup is made, doesnt mark files backed up
    - Bare Metal Restore Backup
        - Designed to allow restoring the system disk directly from backup media without having to install the OS and backup software first

Business Continuity:

- Business continuity consists of the policies, procedures and resources required to ensure a business can function after a major catastrophe
- Sites
    - Cold - Physical location that house the hardware needed to get IT functioning again
    - Warm - Location containing all infrastructure needed for operations to continue
    - Hot - Can be running at moments notiice