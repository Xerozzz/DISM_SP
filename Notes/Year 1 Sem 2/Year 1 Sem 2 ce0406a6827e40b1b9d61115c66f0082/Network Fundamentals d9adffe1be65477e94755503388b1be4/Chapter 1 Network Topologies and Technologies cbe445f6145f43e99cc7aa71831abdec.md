# Chapter 1: Network Topologies and Technologies

Created: Jan 17, 2020 1:40 PM
Updated: Apr 6, 2020 7:55 PM

**Objectives:**

- Describe the primary physical networking topologies in common use
- Describe the primary logical networking topologies in common use
- Describe major LAN networking technologies
- Compare Wi-Fi standard

**Physical Topologies**:

- The lay of the land
- Describes how a network is physically laid out, and the arrangement of cabling and how cables connect one device to another
- Physical Bus:
    - A continuous length of cable connecting one computer to another in a daisy-chain fashion
    - Weaknesses
        - Limit of 30 computers per cable segment
        - Max length of cabling is 185 metres
        - Both ends must be terminated if not signal will bounce back
        - Any break in bus brings down the whole network
        - Adding or removing a machine temporarily brings down the entire network
        - Limited to 10 Mbps half-duplex communication due to coaxial cabling
    - Signal continues until it weakens or is absorbed by terminator, signal weakens after each workstation
- Physical Star:
    - Uses a central device such as hub or switch to allow monitoring and managing of a network
    - Collects statistics about network traffic patterns and detect errors
    - Can be upgraded by replacing central device
    - Central device determines logical topology (hub = logical bus, switch = logical switching, MAU = logical ring)
    - Disadvantages:
        - Central device represents a single point of failure
        - If hub or switch fails or the power cord is disconnected from outlet, whole network goes down
        - Should have a spare central device on hand
- Physical Ring:
    - Devices are daisy-chained to one another
    - Instead of terminating each end, the cabling is brought around from the last device to the first one to forma ring
    - Most widely used to connect LANs with Fiber Distributed Data Interface (FDDI)
        - FDDI mostly used as network backbone to connect between LANs or between hubs and switches
        - FDDI uses dual ring, data travels in both directions and one ring failure doesn't break network
        - Operates using fiber-optic at 100 Mbps
    - Data travels in one direction
    - If any station fails, the whole ring breaks
- Point-to-Point:
    - Direct link between two devices
    - Mostly used in WANs (connecting HQ in New York to branch in Tokyo)
    - Wireless bridge
- Point-to-MultiPoint:
    - Central device communicates with two or more other devices
    - All comms go thru central device
    - Often used in WANs where a main office has connections to several branch offices
- Mesh:
    - Connects each device to every other deivce in a network.
    - High redundancy and fault tolerance, even if one connection fails, there is always another path
    - Very expensive
    - Usually found in large WANs and internetworks

**Logical Topologies**:

- Describe how data travels from computer to computer
- In physical bus and ring, the logical topology same as physical
- For physical star, electronics in central device determine logical topology

**Baseband and Broadband Signaling**:

- Baseband:
    - Sends digital signals in which each bit of data is represented by a pulse of electricity or light
    - Sent at a fixed frequency and no other frames can be sent along with it
- Broadband:
    - Uses analog techniques to encode binary 1s and 0s across a range of values
    - Signals flow at a particular frequency and each frequency represent a channel of data

**Ethernet**:

- Networks:
    - Easy to install and support with a low cost factor
    - Baseband
    - Supports speeds from 10Mbps to 10Gbps
- Frames:
    - Ethernet II frame type used TCP/IP
    - Consists of:
        - Destination MAC
        - Source MAC
        - Type
        - Data
        - FCS
- Media Access:
    - Ethernet uses CSMA/CD
        - Carrier Sense Multiple Access with Collision Detection
        - Carrier Sense - Listen before send, must hear silence
        - Multiple Access - If two or more stations hear silence, multiple stations may transmit at the same time
        - Collision Detection - If two or more stations transmit, a collision occurs and is detected by the NIC, all stations must retransmit
- Error Handling:
    - Ethernet is best-effort delivery system
    - Hope it gets there but no acknowledgement or confirmation
    - Network protocols and applications ensure delivery
    - Only collisions are detected and retransmitted
- Damaged Frames:
    - Cyclic Redundancy Check used to determine if data is unchanged
    - If frame is detected as damaged, it is discarded with no notification