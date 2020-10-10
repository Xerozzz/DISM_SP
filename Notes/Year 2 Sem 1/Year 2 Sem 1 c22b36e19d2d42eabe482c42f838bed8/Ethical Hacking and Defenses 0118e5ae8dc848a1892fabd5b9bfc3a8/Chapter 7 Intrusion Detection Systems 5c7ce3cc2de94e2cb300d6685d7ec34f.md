# Chapter 7: Intrusion Detection Systems

# Intrusion Detection and Prevention Systems

![Chapter%207%20Intrusion%20Detection%20Systems%205c7ce3cc2de94e2cb300d6685d7ec34f/Untitled.png](Chapter%207%20Intrusion%20Detection%20Systems%205c7ce3cc2de94e2cb300d6685d7ec34f/Untitled.png)

## Intrusion Detection Systems

- Placed in networks or systems to detect possible malicious activities
- Sensors are used to monitor network traffic, system resources and activities
- Data collected matched to signatures and an alarm is sent if malicious activity is detected

## Intrusion Prevention Systems

- Same as above
- Can also drop the malicious activity detected or stop it

# Intrusion Detection System Components

## Network and Host Sensors

### Sensors

- Electronic eyes of an IDS to log monitored data
- Hardware or software that monitors traffic and events in your network or host and triggers alarms

### Network-Based Sensors

- Hardware of software that capture data in network packets

### Host-Based Sensors

- Usually software running on hosts like servers to monitor the CPU, memory, disk usage, network connections and others

### Collecting Network Data

- **Network Tap:** Hardware connected inline between two nodes in a network
- **Port Mirroring:** Copies of incoming/outgoing packets on a port of network switch forwarded to another port for analysis

### Network Sensors

- Should be placed at entry points of networks like Internet Gateways, Connections between LANs, Remote access server that receive dial-up connections from remote users and VPN devices
- Management program is used to control sensors
- Sensors can be positioned at either side of a firewall, but better to be behind the firewall

![Chapter%207%20Intrusion%20Detection%20Systems%205c7ce3cc2de94e2cb300d6685d7ec34f/Untitled%201.png](Chapter%207%20Intrusion%20Detection%20Systems%205c7ce3cc2de94e2cb300d6685d7ec34f/Untitled%201.png)

### Sensor Deployment Concerns

- Throughput
    - A sensor may receive more data than it can handle which results in the sensor dropping packets or crashing
    - On a busy network, sensors may not catch all packets
- Security
    - Can be target of attacks as they may contain information of network configuration
    - Compromised sensors can cause unreliable or false data to be recorded

## Alert Systems

### Triggers

- Circumstances that cause and alert message to be sent
- Types of triggers
    - Detection of an anomaly
    - Detection of misuse or attack signature
    - Target monitoring

### Profile-Based Anomaly Detection

- Makes use of profiles for each authorized user, group or system
- Describe how services and resources are normally accessed
- Eg. "The network's UDP traffic never exceeds 20%" or "Agent A only accesses 10-20 records a day from his laptop during office hours only"
- IDSs have to create profiles of normal behavior during "training period"
- May require the use of Machine Learning or Behavior Analytics
- May be able to detect potential insider threats like a user suddenly downloading many files
- Human behavior is not consistent though, sometimes a user may need sudden access at an unusual time instead of his normal behavior
- This causes accuracy problems like false negatives and false positives

### Rule-Based Misuse or Attack Signature Detection

- An attack signature is a sequence of bytes or network packets indicating a possible attack
- Misuse Detection triggers alarms based on signatures of known attacks
- IDS comes equipped with a set of signatures to monitor for
- Can start protecting the network immediately
- Needs to be updated regularly to add new signatures

### Advantages and Disadvantages of each IDS triggering mechanism

![Chapter%207%20Intrusion%20Detection%20Systems%205c7ce3cc2de94e2cb300d6685d7ec34f/Untitled%202.png](Chapter%207%20Intrusion%20Detection%20Systems%205c7ce3cc2de94e2cb300d6685d7ec34f/Untitled%202.png)

### Target Monitoring

- Reports when certain target objects have been modified
- Usually implemented by calculating a checksum for target files or directories to be monitored
- Any modification to the file or directory will cause a change in the generated checksum and an alert will be generated

### IDS Agents

- Processes that analyze events to detect possible intrusions and generates alerts if needed
- Different agents can be used to check different aspects of the network or host
- Agents need to work together to share information with other agents

### Data Correlation

- IDS collects lots of data from various sources like Firewall Logs, Packet Captures, System Log etc
- One attack attempt can cause events to be recorded in different sources
- Data Correlation
    - Associating an event from one source to related events from other sources
    - Recognizing an intrusion attempt from data from different sources
    - Trigger one alert for the same intrusion alert instead of multiple alerts

## Command Console

- Provides a GUI to an IDS to enable admins to receive and analyze alert messages and log files
- IDS can collect information from security devices throughout a network
- Command console should run on a computer dedicated solely to the IDS to maximize speed of respond

## Response System

- IDS can be setup to take some countermeasures like resetting all network connections when intrusion is detected
- Response systems do not substitute network administrators as admins can use judgement to distinguish false positives and can determine if a response should be escalated to a higher level

## Database of Attack Signatures or Behaviors

- IDSs make use of a source of information for comparing the traffic they monitor
- Signature-based detection references a database of known attack signatures, if traffic matches a signature, it sends an alert
- Anomaly-based detection stores normal profile information in a database and if actual traffic or events deviate too much, it sends an alert

# Examining Intrusion Detection Step By Step

![Chapter%207%20Intrusion%20Detection%20Systems%205c7ce3cc2de94e2cb300d6685d7ec34f/Untitled%203.png](Chapter%207%20Intrusion%20Detection%20Systems%205c7ce3cc2de94e2cb300d6685d7ec34f/Untitled%203.png)

## Steps

1. Installing IDS database
2. Gathering data
3. Sending alert messages
4. IDS responds
5. Administrator assesses damage
6. Following escalation procedures
7. Logging and reviewing the event

## Step 1: Installing the IDS Database

- IDS uses the database to compare traffic detected by sensors
- Anomaly-based IDSs need a training period to observe traffic and compile a network baseline
- Signature-based IDS can use a database immediately along with your custom rules

## Step 2: gathering Data

- Sensors gather data by capturing packets or reading log files
- Sensors need to be positioned where they can capture all data, sensors on individual hosts capture information that enters and leaves the host, sensors on network segments read packets as they pass throughout the segment
- If network traffic is too heavy, there is a chance that network sensors may not capture all packets, need to ensure that sensors can cope with load

## Step 3: Sending Alert Messages

- Sensors capture data
- IDS software compares captured data with information in its database
- IDS sends alert messages if data matches an attack signature or deviates from usual behavior

## Step 4: The IDS Responds

- Command console receives alert messages and notifies the admin
- IDS can be configured to take actions when a suspicious packet is received

### Actions

- Sending an alarm message
- Drop packet
- Stop and restart network traffic

## Step 5: The Administrator Assesses Damage

- Admin monitors alerts and determines whether countermeasures are needed
- Administrator need to fine-tune the database to reduce false negatives

## Step 6: Following Escalation Procedures

- Escalation procedures are a set of actions to be followed in the IDS detects a true positive
- Should be spelled out in company's security policy

### Incident Levels

1. Might be managed quickly
2. Represents a more serious threat
3. Represents the highest degree of threat

## Step 7: Logging and Reviewing the Event

- IDS events are stored in log files or databases
- Admin should review logs to determine suspicious behavior or traffic and spot a gradual attack
- IDS should provide accountability capability to track an attempted attack or intrusion back to the responsible party, some systems have built-in tracing features for that

# Types of IDS

- Network-based
- Host-based
- Hybrid

## Network-Based IDS (NIDS)

![Chapter%207%20Intrusion%20Detection%20Systems%205c7ce3cc2de94e2cb300d6685d7ec34f/Untitled%204.png](Chapter%207%20Intrusion%20Detection%20Systems%205c7ce3cc2de94e2cb300d6685d7ec34f/Untitled%204.png)

- Monitors network traffic
- Management and analysis software installed on a dedicated computer
- NIDS usually handles a high volume of traffic and may require dedicated hardware appliance

### Common Locations

- Behind the firewall and before the LAN
- Between firewall and DMZ
- Any network segment

### Freeware NIDS: Snort

- Ideal for monitoring traffic on a small network or individual host
- Does not consume extensive system resources
- Intended for installation on a computer at network perimeter
- Comes with a collection of rule files
- Separate rules exist for port scans, back door attacks and web attacks

![Chapter%207%20Intrusion%20Detection%20Systems%205c7ce3cc2de94e2cb300d6685d7ec34f/Annotation_2020-08-10_133631.png](Chapter%207%20Intrusion%20Detection%20Systems%205c7ce3cc2de94e2cb300d6685d7ec34f/Annotation_2020-08-10_133631.png)

## Host-Based IDS (HIDS)

- Deployed on a host in the LAN, router, server, firewall etc
- Evaluates traffic and events on host
- Gathers data like system processes, CPU use, memory use, file accesses, file contents, log files and network connections

### Centralized Configuration

![Chapter%207%20Intrusion%20Detection%20Systems%205c7ce3cc2de94e2cb300d6685d7ec34f/Untitled%205.png](Chapter%207%20Intrusion%20Detection%20Systems%205c7ce3cc2de94e2cb300d6685d7ec34f/Untitled%205.png)

- Sensors on host send all data to a central location
- Host's level of performance is unaffected by IDS
- Alert messages that are generated may not occur in real time as time is spent sending data to central console and for central console to process it

### Distributed Configuration

![Chapter%207%20Intrusion%20Detection%20Systems%205c7ce3cc2de94e2cb300d6685d7ec34f/Untitled%206.png](Chapter%207%20Intrusion%20Detection%20Systems%205c7ce3cc2de94e2cb300d6685d7ec34f/Untitled%206.png)

- Processing of events is distributed between host and console
- Host analyzes events in real time
- Performance reduction in host

### HIDS: Tripwire

- Creates a baseline snapshot of the current file system
- Any future changes to files will be detected

## Hybrid IDS Implementations

- Combines the features of HIDSs and NIDSs
- Gain flexibility and increases security
- Combine IDS sensor locations and put sensors on network segments and network hosts
- Can report attacks aimed at particular segments or the entire network

## IDS Hardware Appliances

- Can handle more network traffic and have better scalability than software IDSs
- Plug-and-play capabilities, do not need to be configured to work with a particular OS
- Upgrade appliances periodically

# Security Incident Response Team (SIRT)

## Response Options

- Taking countermeasures to block intrusion
- Making corrections to packet-filtering rules and proxy servers
- Modifying security policies to cover new vulnerabilities
- Having a SIRT gives your organization flexibility to carry out these response options

## Goals of a SIRT

- Group of people assigned to respond effectively to security breaches

### Primary Functions

- Preparation
- Notification
- Response

- Countermeasures
- Recovery
- Follow-up

## Responsibility of SIRT

- Look within the organization for SIRT members
- SIRT members should stop any work they have to respond to a security incident and have enough authority to take decisions
- SIRT should contain employees representing a cross-section of the organization
- This ensures all parts of the organization are represented

### SIRT Members Can Come From

- Management
- IT
- Physical Security
- Public Relations

- Legal
- Information Security Services
- Human Resources
- Finance/Accounting

### Staffing and Training

- Consists of employees with other jobs
- Team exists only during meetings or when an incident occurs
- Tends to get out of touch and need retraining
- If budget allows, assemble a team whose sole responsibility is security incident response

### Staging Drills

- Conduct a security drill, you may need to convince upper management of the necessity
- Drills can pay off in the long run and make response more effective and coordinated
- Drills can be scheduled or spontaneous
- Pick a time for the drill and follow a scenario
- Intended to identify any holes in security procedures

## Public Resource Teams

- Teams around the world publish notices and articles about serious security incidents
- You can notify these teams if you encounter  a significant security event
- These groups also provide training for response team members

## Outsourcing Incident Response

- Hire a company that monitors your network and IDS sensors to tell you when an intrusion has occurred
- **Advantage:** Results in lower overall costs
- **Disadvantage:** Hard to achieve timely, effective incident response
- Get references from current and former customers before hiring an IR Service

# Incident Respond Process

![Chapter%207%20Intrusion%20Detection%20Systems%205c7ce3cc2de94e2cb300d6685d7ec34f/Untitled%207.png](Chapter%207%20Intrusion%20Detection%20Systems%205c7ce3cc2de94e2cb300d6685d7ec34f/Untitled%207.png)

## Step 1: Preparation

### Using Risk Analysis

- Identifiers what needs to be protected so a security policy can be created
- Use security policy as a guideline when responding to incidents
- Everyone involved in incident response should know where these guidelines are

### Active Network Monitoring

- SIRT members may be dedicated to essential activity
- Considered a proactive to prevent incidents from occurring and reducing false positives
- Involves actively testing your network using a network vulnerability analyzer like SAINT, webSAINT and Nessus

## Step 2: Notification

- Process by which SIRT members receive news about security incidents
- Notifications come from Firewalls, IDSs, SIRT members, Network Admins and Employees
- After notification, SIRT members should assess level of damage
- Not all incidents need to be reported to all SIRT members

## Step 3: Response

- SIRT members should keep in mind to not panic and follow established procedures
- Take time to analyze all reported events and do not simply react
- Important to have clear escalation procedures which is key to efficient response and create a flowchart for the escalation procedures
- Determine need for escalation, what needs to be reported, who needs to know and how quickly you need to do the reporting
- Report the basic facts surrounding the incidents
- Figure out how people will be notified
- Serious security incidents may require reporting to the public

### Standard Response Procedures

- May not be a good idea to contact the SIRT team by e-mail as attackers may monitor or be in control of your mail servers
- Set up a hotline
- Set up a list of people to contact
- Try not to overract to intrusions
- Follow procedures in place that tell you exactly what to do for each situation

## Step 4: Countermeasures

- Define a set of containment procedures

### Containment of Damage

- Preventing spreading to other resources
- Remove infected systems from rest of network

### Considerations

- Is it alright to shut down infected systems and delete malware etc?
- Is there a need to preserve the infected systems as evidence?

### Eradication of Data Introduced by Intrusions

- Removing any files or programs that resulted from the intrusion
- Check user accounts and configuration
- Can be tedious and time consuming

## Step 5: Recovery

- Putting compromised items back in service
- Monitor restored devices for at least 24 hours to make sure network is operating properly
- SIRT members can require users to sign a document agreeing the computer has been serviced and returned to working order
- Adjust firewall rules in necessary

## Step 6: Follow-Up

- Process of documenting all events associated with the security incident like what took place after an intrusion was detected and a response occurred
- Prevents similar intrusions from reoccuring
- Helps fellow SIRT members deal with similar situations
- Documentation is essential for prosecuting offenders

### Reevaluating Policies

- You can recommend changes to the security policy based on previous attacks
- Information should be included in a follow-up database
- Notify others on the Internet about your attack for information sharing

# Dealing with False Alarms

- Minimize false positives and false negatives
- Tuning your system to record false alarms to detect patterns
- Adjust existing rules if needed

# Dealing with Legitimate Security Alert

- Determine whether an attack is a false alarm
- Respond calmly and follow established procedures
- Call law enforcement personnel if necessary

## Real Alarm Indicators

- System crashes
- New user accounts suddenly appear on the network
- Sporadic user accounts suddenly have heavy activity
- New files appear, often with strange file names
- A series of unsuccessful logon attempts occurs

# Working Under Pressure

- Incident response activities need to be carried out with discretion
- Sometimes it is best to let the incident continue for a while to monitor
- Gather evidence according to the goal of your actions, be it prosecution or corrective measures
- Do not rush to respond to incidents