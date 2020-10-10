# Chapter 2: Network Media

Created: Jan 23, 2020 11:02 PM
Updated: Jan 24, 2020 12:37 PM

**Objectives:**

- Define the primary cables used in wired networking
- Describe the characteristics of the major types of fiber-optic media
- Explain the technologies used for wireless networking

**Wired Networking**:

- Categories:
    - Copper wire and fiber optic
- Main Differences:
    - Composition of signals (electricity/light)
    - Speed at which signals are sent
    - Distance the signals can effectively travel

**Criteria for Choosing Network Media**:

- Bandwidth Rating:
    - Number of bits per second that can be transmitted across a medium
    - Determined by enconding
    - Choose a cable compatible with current standard and support growth
- Maximum Segment Length:
    - Max length of cable between two network devices
    - Each cable can only carry signal so far before attenuation
    - Any intermediate passive devices such as wall jacks are part of total segment length
- Interference and Eavesdropping Susceptibility:
    - Copper media is susceptible to electromagnetic interference and radio frequency interference
        - Motors, transformers and other sources of intense electrical activity can emit both EMI and RFI
    - Cross talk - interference one wire generates on another wire when both wires are in a bundle
    - Copper is suspect to all these but fiber optic is not
- Cable Grade:
    - Building and fire codes require specific cabling requirements
    - Plenum rated
    - Fire resistant
- Connection Hardware:
    - Every type of cable has connectors that influence the kinds of hardware the cable can connect to
    - The media selected must be supported by the network device
- Ease of installation:
    - Minimum bend radius
    - Cost and time to set up and terminate medium
    - Physical environment (EFI/RFI)
- Total cost:
    - Cost of everything including cabling, connectors, termination panels, wall jacks, testing equipment

**Twisted-Pair Cable**:

- Details:
    - Consists of one or more pairs of insulated strands of copper wires twisted around each other and housed in outer jacket
    - The more twists per unit length, the better the resistance to EMI and crosstalk
    - More expensive TP has more twists
- Unshielded Twisted Pair (UTP):
    - Mostly used
    - Consists of 4 pairs of insulated wires
    - Cat 1-6a accepted in US
    - Cat 7 and 7a still not accepted
- Shielded Twisted Pair (UTP):
    - Includes shielding to reduce crosstalk and interference
    - Best to use in electrically noisy or high bandwidth applications
- Cable Plant Components:
    - RJ-45 Connectors
        - Most commonly used in patch cables
    - RJ-45 Jacks
        - What you plug an RJ-45 connector into when computer not near switch or hub
        - Usually placed behind wall plates
    - Patch Cable
        - Short cable for connecting a computer to an RJ-45 wall jack or connecting a patch-panel port to a switch or hub
    - Patch Panels
        - Used to terminate long runs of cable from where computers are to the wiring closet
    - Distribution Racks
        - Holds network equipment such as routers and switches plus patch panels and rack-mounted servers

**Structured Cabling**:

- Specifies how cabling should be organised regardless of the media type or network architecture
- Work Area:
    - Where workstations and other user devices are located
    - Faceplates and wall jacks installed here
    - Patch Cable connects computer and printers to wall jacks
- Horizontal Wiring:
    - Runs from work area's wall jack to the telecommunication closet
    - Max wiring distance of 90m
- Telecommunication Closet:
    - Provides connectivity to computer equipment in nearby work area
    - Typically includes patch panels to terminate horizontal wiring runs, hubs and switches
    - TC that houses the cabling and devices for work area computers is called intermediate distribution frame (IDF)
- Equipment Room:
    - Houses servers,routers,switches and other major network equipment and serves as connection point for backbone cabling
    - An Equipment room thats the connection point between IDFs is called a main distribution frame (MDF)
    - MDF can be main cross-connect for entire network or might serve as a connection point for backbone cabling between buildings
- Backbone Cabling:
    - Interconnects IDFs and MDFs
    - Runs between floors or wings of building
    - Usually fiber-optic cable but can be UTP is distance between TCs is less than 90 meters
- Entrance Facility:
    - Location of the cabling and equipment that connects a corporate network to a third party telecommunications provider
    - Can serve as equipment room and main cross-connect for all backbone cabling
    - Where connection to a WAN is made
    - Demarcation Point - Where corporate LAN equipment ends and third party provider's equipment and cabling begins

**Straight-Through vs Crossover Cable**:

- Straight-Through:
    - Standard patch cables
    - Uses same wiring standards on both sides
- Cross-over Cables:
    - Uses 568A standard on one side and 568B on the other side of the cable
    - Crosses the transmit and receive wires so that transmit on one end connects to receive on the other
    - Needed when you connect similar type of devices together
- Medium Dependent Interface:
    - Network devices that connect using RJ-45 plugs over twisted pair cabling are classified as MDI or MDI-X devices
    - MDI devices transmit on pins 1 and 2 and receive on pin 3 and 6
        - PC NICs, Routers
    - MDI-X devices transmit on 3 and 6 and receive on 1 and 2
        - Hubs and switches
    - When two like devices (etc 2 switches) want to connect, you need to use a crossover cable
- Why two transmit and receive wires?:
    - One wire pair used for transmit (T+/T-) and one pair used for receive (R+/R-)
    - The wires carry a positive and negative signal
    - This differential signal mitigates the effect of crosstalk and noise on cable

**Fiber Optic Cable**:

- Details:
    - Bits are transmitted as pulses of light instead of electricity
    - Immune to EMI and RFI
    - Immune to eavesdropping
    - Composition
        - Slender cylinder of glass fiber called the core surrounded by a concentric layer of glass called cladding
        - Fiber is then jacketed in a thin transparent plastic material called buffer
    - Each strand carries data in only one direction
        - Two or more strands needed for network conenctions
- Installation:
    - More difficult and time consuming than copper media installation
    - Many methods for installation and terminating fiber optic cables due to many connectors and cable types available
- Cable Type:
    - Single-Mode Fiber
        - Includes a single, small diameter fiber at the core
        - Generally works with laser based emitters
        - Spans the longest distances and higher bandwidth than MMF
    - Multi-Mode Fiber
        - Larger diameter fiber at the core
        - Costs less than SMF
        - Works with LED emitters
        - Shorter distances and less bandwidth than SMF

**Wireless Networking**:

- Details:
    - Often used with wired networks to interconnect geographically dispersed LANs or groups of mobile users with wired servers and resources on a LAN
- Benefits:
    - Creates temporary connections to wired networks
    - Establishes backup or contingency connectivity for existing wired networks
    - Extends network span beyond limitations of wired cabling
    - Allows businesses to provide customers with wireless networking easily, offering a service that brings in customers and keeps them there
    - Enables users to roam around a corporate or college campus with their machines
- Types:
    - Local Area Networks (LAN)
        - Usually provides connectivity for mobile users or across areas that otherwise cannot be networked
    - Extended LANs
        - Usually used to increase a LAN's spam beyond normal distance limitations
    - Internet Service
        - Used to bring Internet Access to homes and businesses
    - Mobile Computing
        - Users communicate by using a wireless networking medium that enables them to move while remaining connected to network
- Components:
    - Access Points
    - NIC
    - Antenna
    - Transceiver
- Transmissions:
    - Signals take from of Electromagnetic waves
    - Frequencey of Hz
    - Lower-frequency transmissions carry less data over longer distances
    - Higher-frequency transmissions carry more data over shorter distances
- Technologies:
    - Infrared
    - Laser
    - Narrow-Band Radio
        - Uses low-powered two-way radio communication
        - Receiver and transmitter must be tuned to same frequency to handle incoming and outgoing data
        - Requires no line of sight between sender and receiver as long as both parties stay in broadcast range
        - Signals can be blocked or interfered with by radio interference
    - Spread-Spectrum
        - Uses multiple frequencies simultaneously to improve reliability and reduce interference
        - Two kinds:
            - Frequency Hopping - Switches data between multiple frequencies at regular intervals
            - Direct-Sequence Modulation - Breaks data into fixed size segments called chips and transmits that data on several different frequencies at the same time