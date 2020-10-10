# Chapter 8: Organisational Security

Created: Feb 10, 2020 12:17 PM
Updated: Mar 1, 2020 6:53 PM

**Objectives:**

- Define business continuity
- Describe how to achieve fault tolerance through redundancy
- Explain different environmental controls

**What is Business Continuity?**

Details:

- An organisation's ability to maintain operations after a disruptive event
- Preparedness Measures
    - Business continuity planning
    - Business impact analysis
    - Disaster recovery planning

Business Continuity Planning (BCP):

- The process of identifying exposure to threats, create prevantative and recovery procedures as well as testing for sufficiency
- Consists of 3 essential elements
    - Business Recovery Planning
    - Crisis Management and Communications
    - Disaster Recovery

Business Impact Analysis (BIA):

- Identifies business functions and quantifies the impact a loss of these functions may have on business operations
- Range from
    - Impact on property and tangible assets
    - Impact on finance and monetary funding
    - Impact on safety and physical protection
    - Impact on reputation and status
    - Impact on life and well-being
- BIA helps to determine mission-essential function that serves as core purpose of an enterprise
- BIA helps to identify critical systems and single point of failures
- BIAs usually contain privacy impact assessment to identify and mitigate privacy risks
- BIAs has privacy threshold assessment to determine if a system contains personally identifiable information

Disaster Recovery Plan (DRP):

- Focuses on protecting and restoring information technology functions
- Written document detailing process for restoring IT resources following a disruptive event
- Comprehensive in scope and meant to be updated regularly
- Usually has a common set of features, cover specific topics and require testing for verification
- Typical Outline
    - Unit 1: Purpose and Scope
    - Unit 2: Recovery Team
    - Unit 3: Preparing for a Disaster
    - Unit 4: Emergency Procedures
    - Unit 5: Restoration Procedures
- Topics
    - Sequence in restoring systems, which should have priority?
    - What should be done if a disaster makes current location unusable? Alternative processing site must be identified and failback must be initiated
        - Failback - The process of resynchronizing data back to the primary location
- Testing
    - Disaster exercises are designed to test the effectiveness of the DRP
    - To test efficiency of interdepartmental planning and coordination in managing a disaster, test current DRP procedures and determine responses strengths and weaknesses
- Tabletop Exercises
    - Simulate an emergency situation but in an informal and stress-free environment
    - After report should be generated to analyze the exercise results to identify strengths to be maintained and weaknesses to improve upon

**Fault Tolerance Through Redundancy:**

Details:

- Fault tolerance refers to system's ability to deal with malfunctions
- Use duplicated equipment to improve availability of a system
- Goal is to reduce mean time to recovery (MTTR) which is the average amount of time that it will take a device to recover from a non-terminal failure
- Redundancy planning applies to servers, storage, networks, power, sites and data

Server:

- Servers play a key role in network infrastructure
- Failure has a significant business impact
- Clustering combines two or more servers to act as a single server connected through public and private cluster connections
- Asymmetric
    - In asymmetric server cluster, a standby server performs no function except to be ready if needed, used for databases, file and print services
- Symmetric
    - All servers do useful work in symmetric server cluster
    - If one server fails, remaining server takes on failed server's work
    - More cost effective than asymmetric and used for Web,media and VPN servers

Storage:

- Use SSDs as they are more resistant to failure and more reliable than HDDs
- HDDs usually fail first
- Usually has hard drives on hand
- Mean time between failures (MTBF)
    - Measures average time until a component fails and must be replaced
    - Can be used to determine number of spare hard drives an organisation should keep
- Redundant Array of Independent Devices (RAID)
    - Uses multiple hard disk drives to increase reliability and performance
    - Can be Implemented through software or hardware
    - Multiple Levels Exit (0,1,5,0+1)
    - RAID Level 0 (striped disk array without fault tolerance)
        - Striping partitions hard drive into smaller sections
        - Data written to stripes is alternated across drives
        - If one drive fails, all data on that drive is lost
        - 

            [Chapter%208%20Organisational%20Security%20abb94d081f2a4d47967ebde7fa613166/untitled](Chapter%208%20Organisational%20Security%20abb94d081f2a4d47967ebde7fa613166/untitled)

    - RAID Level 1 (mirroring)
        - Disk mirroring used to connect multiple disk to same controller card
        - Action on primary drive is duplicated on other drive
        - If primary drive fails, data is not lost
        - Disk Duplexing - A variation of RAID level 1 that separate cards used for each disk, protects against controller card failures
        - 

            [Chapter%208%20Organisational%20Security%20abb94d081f2a4d47967ebde7fa613166/untitled%201](Chapter%208%20Organisational%20Security%20abb94d081f2a4d47967ebde7fa613166/untitled%201)

    - RAID Level 5 (independent disks with distributed parity)
        - Distribute parity error checking across all drives
        - Data stored on one drive and its parity information stored on another drive
        - 

            [Chapter%208%20Organisational%20Security%20abb94d081f2a4d47967ebde7fa613166/untitled%202](Chapter%208%20Organisational%20Security%20abb94d081f2a4d47967ebde7fa613166/untitled%202)

    - RAID Level 0+1 (high data transfer)
        - Nested-level RAID
        - Mirrored array whose segments are RAID 0 arrays
        - Can achieve high data transfer rates
        - 

            [Chapter%208%20Organisational%20Security%20abb94d081f2a4d47967ebde7fa613166/untitled%203](Chapter%208%20Organisational%20Security%20abb94d081f2a4d47967ebde7fa613166/untitled%203)

[Chapter%208%20Organisational%20Security%20abb94d081f2a4d47967ebde7fa613166/untitled%204](Chapter%208%20Organisational%20Security%20abb94d081f2a4d47967ebde7fa613166/untitled%204)

Networks:

- Redundant networks are necessary due to critical nature of connectivity today
- Wait in the background during normal operations
- Uses a replication scheme to keep live network information current
- Launches automatically in event of disaster
- Hardware components are duplicated and sometimes second ISP contracted
- Software defined networks (SDNs)
    - SDN controller can increase network reliability and may lessen the need for redundant equipment

Power:

- Maintaining power is essential for redundancy
- Uninterruptible Power Supply (UPS)
    - Maintains power to equipment in event of interruption of primary source
- Off-line UPS
    - Least expensive and simplest solution
    - Charged by main power supply
    - Begins supplying power quickly when primary power is interrupted
    - Switches back to standby mode when primary power restored
- On-line UPS
    - Always running off its battery while main power runs battery charger
    - Not affected by dips or sags in voltage
    - Can serve as surge protector
- Backup Generator
    - Powered by diesel,natural gas or propane

Recovery Sites:

- Backup sites may be necessary if building is damaged
- Hot Site
    - Generally run by a commercial disaster recovery service
    - Duplicate of production site
    - Has all needed equipment and data can be quickly moved over
- Cold Site
    - Provides office space
    - Customer must provide and install all equipment to continue operations
    - No backups immediately available
    - Less expensive than hot site
    - Takes longer time to resume full operations
- Warm Site
    - All equipment installed
    - No internet, telecommunications facilities or data backups
    - Less expensive than hot site
    - Time to turn on connections and install backups can be half a day or more
- Cloud Computing
    - Growing trend to back up applications and data to the cloud
    - If disaster occurs, restore it to hardware in hot, cold or warm site

Data:

- Data Backup - Copying information to a different medium and storing it in an off-site location
- Involves
    - Data backup calculations
    - Using different types of data backups
    - Off-site backups
- Recovery Point Objective (RPO)
    - Max time organisation can tolerate between backups
- Recover Time Objective (RTO)
    - Length of time to recover backed up data
- Types of Data Backups
    - 

        [Chapter%208%20Organisational%20Security%20abb94d081f2a4d47967ebde7fa613166/untitled%205](Chapter%208%20Organisational%20Security%20abb94d081f2a4d47967ebde7fa613166/untitled%205)

- Continuous Data Protection (CDP)
    - Performs continuous backups that can be restored immediately
    - Maintains a historical record of all changes made to data
    - Creates snapshot of data
- 3-2-1 Backup Plan
    - Should always be three different copies of backups on at least two different types of storage media and one backup stored in another location
- Internet Services
    - Automatic continuous backup
    - Universal access
    - Delayed deletion
    - Online or media-based restore

**Environmental Controls:**

Methods:

- Fire Suppression
- Electromagnetic disruption protection
- Proper configuration of HVAC system

Fire Suppression:

- Attempts to reduce impact of a fire
- Requirements for fire to occur
    - Type of fuel or combustible material
    - Sufficient oxygen to sustain combustion
    - Enough heat to raise material to ignition temperature
    - Chemical reaction to set fire itself
- Best to equip server closet or room with stationary fire suppression
- Types
    - Water Sprinkler System
    - Dry Chemical System (dry powder)
    - Clean Agent System (CAN BE POISONOUS, best for server or electronics)

Electromagnetic Disruption Protection:

- Electromagnetic Interference (EMI)
    - Caused by short duration burst of energy from a source called an electromagnetic pulse (EMP)
- Electromagnetic Compatibility (EMC)
    - Reducing or eliminating the unintentional generation, spread and reception of electromagnetic energy
    - Goal of EMC is the correct operation of different types of equipment that function in the same electromagnetic environment
- Faraday Cage
    - Metal enclosure that prevents entry or escape of electromagnetic fields
    - Often used for testing in electronic labs

HVAC:

- Data centers have special cooling requirements to reduce heat generated from systems
- HVAC - Heating, ventilating and air conditioning systems
- Maintain temperature and relative humidity at required levels
- Hot/Cold aisle layout
    - Used to reduce heat by managing air flow
    - Servers lined up in alternating rows with cold air intakes facing one direction and hot air exhausts in another

**Incidence Response:**

Details:

- When an unauthorized incident occurs, an immediate response is required
- Involves using forensic and proper incident response procedures

Forensics:

- Analyzing evidence and can be applied to tehnology
- Uses technology to search for computer evidence of a crime
- Importance due to
    - Amount of digital evidence
    - Increased scrutiny by legal profession
    - Higher level of computer skill by criminals

Incident Response Plan:

- A set of written instructions for reacting to a security incident
- Six steps to take when incident occurs
    - Preparation
    - Identification
    - Containment
    - Eradication
    - Recovery
    - Lessons learned
- At a minimum, should contain
    - Documented incident definitions
    - Cyber-incident response teams
    - Reporting requirements/escalation
    - Exercises

Forensics Procedures:

- Five basic steps
    - Secure crime scene
    - Preserve evidence
    - Establish chain of custody
    - Examine evidence
    - Enable recovery