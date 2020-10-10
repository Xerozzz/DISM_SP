# Chapter 4: Network Devices in Depth

Created: Jan 16, 2020 3:21 PM
Updated: Feb 19, 2020 4:44 PM

**Objectives:**

- Describe the advanced features and operation of network switches
- Describe routing table properties and discuss routing protocols
- Explain basic and advanced wireless access point features
- Select the most suitable NIC bus and features for a computer

**Network Switches in Depth:**

- Switches work at the Data Link Layer (Layer 2)
- Receives frames on one port and forward them to the port where the destination device can be found
- Broadcast frames is sent out to all ports
- Each switch port is a collision domain
- Switch ports can operate in full-duplex mode

Mode of Operations:

- Most switches run in auto-negotiate mode, the switch sets the mode to the highest performance setting the connected device supports
- Auto-MDIX mode - switch port detects the type of device and cable it's connected to (straight-through or crossover can be used)

Switching Table:

- Holds MAC address and port pairs that tell the switch where to forward a frame based on destination MAC Address
- When first turned on, table is empty
- As network devices send frames, the switch reads each frame's source address and adds to the table along with with port it was received from
- If a frame's destination address isn't found in the switching table the switch forwards the frame out to all ports
- Switches can only hold a limited number of MAC addresses
- Switching tables prevent stale entries by including time stamps when an entry is created
- The period of time a table keeps a MAC address entry is called aging time
- Time stamp is updated every time the switch receives a frame from the device
- If time stamp isn't updated within aging time, the entry expires and is removed

Frame Forwarding Methods:

- Cut Through - switch reads only the destination and source address before sending, fastest but no error checking
- Store-and-forward - Switch reads the entire frame into buffers and examines FCS field before forwarding, ensuring there are no errors before forwarding the frame, slowest method
- Fragment-Free - Switch reads enough of the frame to guarantee it's at least the minimum size for the network type

**Advanced Switch Features**:

- High-end switches (smart switches, managed switches) can make networks more efficient and reliable
- Multicast Processing:
    - Switches process multicast frames in one of two ways
    - Low-end switches broadcast and sends them out to all ports
    - High end switches that support IGMP (Internet Group Management Protocol), forwards the frames only to ports that have registered the multicast address
    - Multicast addresses always begin with "01:00:5E"
- Spanning Tree Protocol:
    - Enables switches to detect when there is a potential for a switching loop
        - Occurs when a frame is forwarded from one switch to another in an infinite loop
    - When a possible loop is detected:
        - One of the switch ports goes into blocking mode, preventing it from forwarding frames that would create a loop
        - If loop configuration is broken, switch in blocking mode resumes forwarding frames
    - Side Effect - Devices take longer to create a link with a switch that runs the STP
    - Rapid STP (RSTP) an enhancement to STP that provides faster convergence when the topology changes
- Virtual Local Area Network (VLANS):
    - Enables you to configure one or more switch ports into separate broadcast domains
    - Almost like separating a switch into two or more switches not connected to one another
    - Router is needed to communicate between VLANs
    - Improves management, security of network and gives more control of broadcast frames
    - Allows admins to group users and resources logically instead of physically
    - Factors to consider:
        - Overuse VLANs may cost more than it benefits you
        - More VLANs mean more logical networks so network will be more complicated
        - Routers are slower devices, so performance can decrease with more VLANs added
        - Every VLAN created needs a corresponding router interface
        - More router interfaces mean more IP networks, meaning more subnetting required
- VLAN Trunks:
    - Trunk port is a switch port configured to carry traffic from all VLANs to another switch or router
    - Involves the switch adding a tag to each frame that must traverse the trunk port to identify which VLAN the traffic came from
- Switch Port Security:
    - Most buildings have network jacks connected to switches available to public users, who can easily plug in malicious devices
    - Help prevent attackers from plugging in a laptop that contain viruses or malware or hacker tools
    - Enables admin to limit how many and which MAC addresses are allowed to connect to a port
    - If unauthorized computer attempts to connect, the port can be disabled and a message can be sent to the admin to alert them of intrusion
- Multi-layer Switches:
    - Some advanced switches have all the functions of a managed switch but add Layer 3 capabilities too
    - Typically used in interior of networks to route between VLANs instead of being placed on network perimeter
    - Offers performance advantage over routers as packet routing between VLANs is done with switch instead of exiting to a router

# Routers in Depth:

- Routers operate at Network Layer (Layer 3) and work with packets
- Connects separate logical networks to form an internetwork
- Broadcast frames not forwarded to other router ports
- Routers can be used to create complex internetworks with multiple paths creating fault tolerance and load sharing
- Interfaces:
    - Must have two or more interfaces/ports in order to forward packets to other networks
    - When router receives a frame, it compares destination MAC address with the interface's MAC Address
    - If they match, router strips frame header and trailer and reads packet's destination IP address. If it matches it processes the packet, if not, it consults its routing table on how to get the packet to its destination
    - Packet Forwarding - Process of moving a packet from incoming interface to outgoing interface
- Tables:
    - Composed of network address and interface pairs that tell the router which interface to forward a packet to
    - Usual entries:
        - Destination Network
        - Next hop
        - Metric
        - Timestamp
        - How the route is derived
- Protocol:
    - Set of rules that routers use to exchange information so that all routers have accurate information about an internetwork to populate their routing tables
    - Distance-vector Protocol (RIP and RIPv2)
        - Share info about an internetwork's status by copying a router's routing table to other routers
        - Slower but lower CPU use
        - Updated periodically
    - Link-State Protocols (OSPF)
        - Share info with other routers by sending status of all their interface links to other routers
        - Updated only when change occurs
        - Faster but Higher CPU use
    - Speed of convergence refers to how fast routing tables of all routers on the internetwork are updated when a change occurs
    - Interior Gateway Protocols (IGP) used in an autonomous system
        - Which is an internetwork managed by a single organisation
        - Routing protocols discussed so far are IGPs
    - Exterior Gateway Protocols (EGP) are used between autonomous systems
        - EGP example is Border Gateway Protocol (BGP)
    - Static routes can be entered in a routing table manually
    - Consider the following before deciding:
        - Does the network change often? If so, a routing protocol is probably a good choice
        - Are there several alternate paths to many of the networks in the internetwork? If so, a routing protocol can reroute around down links or congested routes automatically
        - Is the internetwork large? A routing protocol builds and maintains routing tables automatically
- Access Control Lists:
    - A set of rules configured on a router's interface for specifying which addresses and which protocols can pass through an interface and to which destinations, known as packet filtering
    - ACLs are usually configured to block traffic based on:
        - Inbound or outbound traffic
        - Source address & Destination address
    - Protocol
    - Addresses can be specific IP addresses or network numbers and filtering can be done on either source or destination address or both

# Wireless Access Points in Depth:

- Basic Wireless Settings:
    - Wireless network mode - allows you to choose which 802.11 standard the AP should use
    - SSID - when an AP is shipped the SSID is set to a default value, it is recommended to be change upon setup
    - Wireless channel - recommended that you set your channels five channels apart, such as 1,6,11
    - SSID broadcast status - by default, APs are configured to transmit the SSID so that any wireless device in range can see the network
- Security Options:
    - Most APs offer the following security options:
        - Encryption
        - Authentication
        - MAC filtering
        - AP isolation
    - Encryption
        - Most common protocols are Wired Equivalent Privacy (WEP), Wi-Fi Protected Access (WPA) and WPA2
        - Use highest level of security your systems support
    - Authentication
        - User must enter a username and password to access the wireless network
        - APs that support authentication usually support the Remote Dial-In User Service (RADIUS) protocol
    - MAC Filtering
        - Enables you to restrict which devices can connect to your AP
        - Add the MAC addresses of the wireless devices allowed to access your network to a list on the AP
    - AP Isolation
        - Creates a separate virtual network for each client connection
        - Clients can access the Internet but can't communicate with each other
- Advanced Wireless Settings:
    - Adjustable Transmit Power
        - Lets you control the power and range of the wireless network signal
    - Multiple SSIDs
        - Two or more wireless networks can be created with different security settings
    - VLAN support
        - To assign wireless networks to wired VLANs
    - Traffic Priority
        - If your AP is configured for multiple network you can assign a priority to packets coming from each network
    - Wi-Fi Multimedia
        - Provides Quality of Service (QoS) settings for multimedia traffic, giving priority to streaming audio or video
    - AP Modes
        - AP can be set to operate as a traditional access point, a repeater, or a wireless bridge

# NIC in Depth:

- NIC makes the connection between computer and network medium
- Performance and reliability of NIC crucial to computer's network performance
- Advanced Features of NICs:
    - If NIC is slow, can limit network performance
    - When selecting a network adapter, first identify the physical characteristics the card must match
        - Type of bus
        - Type of network topology
        - Type of connector to connect to media
    - Hardware-enhancement options
        - Shared adapter memory - The adapter's buffers map directly to computer's RAM
        - Shared system memory - A NIC's onboard processor selects a region of RAM on the computer and writes to it as though it were buffer space on the adapter
        - Bus Mastering - Permits a network adapter to take control of the computer's bus to initiate and manage data transfers to and from the computer's memory
        - RAM Buffering - Means a NIC includes additional memory to provide temporary storage for incoming and outgoing network data that arrives at the NIC faster than it can be sent out
        - OnBoard Co-processors - Enables the card to process incoming and outgoing network data without requiring network service form CPU
        - QoS allows prioritizing time-sensitive data
        - Automatic Link Aggregation - Enables you to install multiple NICs in one computer and aggregate the bandwidth
        - Improved fault tolerance by installing second NIC
        - Advanced Configuration Power Management Interface (ACPI) offers wake-on LAN - Allows an administrator to power on a PC remotely by accessing the NIC through the network
        - Preboot Execution Environment (PXE) adapters allow a computer to download an OS isntead of booting it from a local hard drive
        - Virtualized environments benefit from NICs with multiple ports

# Firewall:

- A network firewall is a security device that puts up a barrier between a local network and the Internet
- The firewall acts as a filter, allowing or restricting data traffic between the network it protects and other networks
- Firewalls are flexible, allowing you to modify the blocking rules, such as by IP addresses, by protocol, by port or for software apps and service
- Router vs Firewall:

[Chapter%204%20Network%20Devices%20in%20Depth%2047082c09fbe849d4886be52cfbc18c7a/untitled](Chapter%204%20Network%20Devices%20in%20Depth%2047082c09fbe849d4886be52cfbc18c7a/untitled)

- Hardware Firewall vs Software Firewall:
    - Both protects from malicious traffic
    - Hardware firewall can be a stand-alone device or part of a router which provides simple and effective protection for your network. It reviews the headers of data packets and decides if it can be trusted, if safe, it forwards, if not, it will drop
    - Software firewall is a program installed on your computer as part of an antivirus suite or separately. It protects your computer from uncontrolled access, Trojans and worms as well