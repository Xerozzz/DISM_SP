# Chapter 6: Wireless Security

Created: Jan 28, 2020 10:19 AM
Updated: Feb 29, 2020 10:45 AM

**Objectives:**

- Describe the different types of wireless network attacks
- List the vulnerabilities in IEEE 802.11 security
- Explain the solutions for securing a wireless network

**Wireless Attacks:**

- Bluetooth Attacks
- Near Field Communication (NFC) attacks
- Radio Frequency Identification Systems
- Wireless Local Area Network attacks

**Bluetooth Attacks:**

Bluetooth:

- Wireless technology that uses short-range radio frequency transmission
- Provides rapid device pairings
- Personal Area Network (PAN) technology

Piconet:

- Established when two Bluetooth devices come within range of each other
- One device (master) controls all wireless traffic
- Other device (slave) takes commands
    - Active slaves send transmissions
    - Parked slaves connected but not actively participating

Bluejacking:

- Attack that sends unsolicited messages to Bluetooth-enabled devices
    - Text messages, images or sounds
- Bluejacking is more annoying than harmful as it cannot steal data

Bluesnarfing:

- An attack that accesses unauthorized information from a wireless device through a Bluetooth connection
- Often between cell phone and laptops
- Attacker copies email, contacts or other data by connecting to Bluetooth device without owner's knowledge

**Near Field Communication (NFC) Attacks:**

Near Field Communication (NFC):

- A set of standards used to establish communication between devices in close proximity
- Once devices are brought within 4cm of each other or tapped together, two-way communication is established
- Passive NFC device - contains informations that other devices can read but does not read or receive any information
- Active NFC device - can read information and transmit data
- Examples of use
    - Automobile
    - Office
    - Retail Stores
    - Transportation
    - Mobile payment

NFC Attacks:

[Chapter%206%20Wireless%20Security%20498ca5dd00c84301b359917bf367e4a4/untitled](Chapter%206%20Wireless%20Security%20498ca5dd00c84301b359917bf367e4a4/untitled)

**Radio Frequency Identification (RFID) Attacks:**

Radio Frequency Identification (RFID):

- Commonly used to transmit information between employee identification badges, inventory tags, book labels and other paper-based tags that can be detected by proximity reader
- Can be very small as they are passive and do not have their only power supply
- Susceptible to many different attacks

RFID Attacks:

[Chapter%206%20Wireless%20Security%20498ca5dd00c84301b359917bf367e4a4/untitled%201](Chapter%206%20Wireless%20Security%20498ca5dd00c84301b359917bf367e4a4/untitled%201)

**Wireless Local Area Network Attacks:**

Wireless Local Area Network:

- Designed to replace or supplement a wired LAN

[Chapter%206%20Wireless%20Security%20498ca5dd00c84301b359917bf367e4a4/untitled%202](Chapter%206%20Wireless%20Security%20498ca5dd00c84301b359917bf367e4a4/untitled%202)

Hardware:

- Wireless Client NIC adapter
    - Performs same functions as wired adapter
    - Antenna sends and receives signals through airwaves
- Access Point
    - Antenna and radio transmitter/receiver to send and receive wireless signals
    - Bridging software to interface wireless devices to other devices
    - Wired network interface allows it to connect by cable to standard wired network
- Access Point Functions
    - Acts as "base station" for wireless network
    - Acts as a bridge between wireless and wired networks
    - Can connect to wired network by a cable
- Infrastructure Mode - WLAN using an AP
- Ad-Hoc Mode - WLAN not using AP
    - Cannot connect to another network
    - Devices can only communicate among themselves

Enterprise Attacks:

- Rogue Access Point
    - An unauthorized access point that allows an attacker to bypass network security configurations
    - Usually set up by insider (employee)
    - May be set up behind a firewall, opening the network to attacks
- Evil Twin
    - AP set up by attacker
    - Attempts to mimic an authorized AP
    - Attackers capture transmissions from users to evil twin AP
- Intercepting Wireless Data
    - Attacker can pick up on RF signal from an open or misconfigured AP
    - Using a WLAN to read this data could yield significant information to an attacker regarding the wired enterprise network
- Wireless Replay Attack
    - Also known as hijacking
    - Attacker captures transmitted wireless data, records it and sends it on to original recipient without attacker's presence being detected
    - Can be accomplished using an evil twin AP
    - Known as Man-in-the-Middle attack
- Wireless DOS attack
    - RF jamming - attackers use intentional RF interference to flood RF spectrum to prevent device from communicating with ap
    - Spoofing - Attacker crafts a fictitious frame that pretends to come from a trusted client when it actually comes from the attacker
    - Manipulating duration field values - Attackers send a frame with the duration field set to a high value, preventing other devices from transmitting for that period of time
- Wireless Home Attacks
    - Steal data
    - Read wireless transmissions
    - Inject Malware
    - Crack weak passwords

**Wired** Equivalent **Privacy (WEP):**

Details:

- An IEEE 802.11 security protocol designed to ensure that only authorized parties can view transmissions by encrypting plaintext into ciphertext
- Secret key is shared between wireless client device and AP

Vulnerabilties:

- Can only use 64-bit or 128-bit key to encrypt as well as a 24-bit Initialization Vector (IV)
- Short length makes it easy to break
- Violates cardinal rule of cryptography by having a detectable pattern when IVs start repeating

# Wi-Fi Protected Setup (WPS):

Details:

- WPS is an optional means of configuring security on WLANS
- PIN method
    - Utilizes a PIN printed on a sticker of the wireless router or displayed through software wizard
    - User enters PIN and security configuration automatically occurs
- Push-Button Method
    - User pushes buttons and security configuration takes place

Design and Implementation Flaws:

- No lockout limit for entering PINs
- The last PIN character is only a checksum
- Wireless router reports validity of the first and second halves of the PIN separately

# MAC Address Filtering:

Details:

- Method of controlling WLAN access by limiting a device's access to AP
- Used by nearly all wireless AP Vendors
- Permits or blocks devices based on MAC Address

Weaknesses:

- Can be countered with MAC spoofing as exchange of MAC addresses is unencrypted
- Hard to manage a large number of addresses

# SSID Broadcasting:

Details:

- Service set identifier, user-supplied name of a wireless network
- Weaknesses
    - SSID can be discovered when transmitted in other frames
    - May prevent users from being able to freely roam from one AP coverage area to another
    - Not always possible to turn off broadcasting

# Wi-Fi Protected Access (WPA):

Details:

- Two types
    - WPA Personal
    - WPA Enterprise
- Addresses both encryption and authentication
- Uses Temporal Key Integrity Protocol Encryption (TKIP)
    - Uses a longer 128 bit key than WEP that is dynamically generated for each packet
    - Includes Message Integrity Check (MIC) to prevent MITM attacks
- Uses Preshared Key Authentication (PSK)
    - Key is shared prior to communication taking palce
    - Uses a passphrase to generate encryption key
    - Devices with secret key is automatically authenticated by AP

Vulnerabilities:

- Key management
    - Key sharing is done manually with no security protection
    - Key must be changed on regular basis
    - Key must be disclosed to guest users
- Passphrases
    - PSK passphrases fewer than 20 characters subject to cracking

# AES-CCMP Encryption:

Details:

- AES block cipher of 128-bits, performs three steps on every block of plaintext
- Within second step, multiple iterations of substitution and rearrangement of bytes is performed
- Counter Mode with Cipher Block Chaining Message Authentication Code Protocol (CCMP)
    - Encryption protocol used in WPA2
    - Specifies the use of AES with CCM
- Cipher Block Chaining Message Authentication Code (CBC-MAC) provides data integrity and authentication
- CCMP and TKIP uses 128-bit key for encryption
- Both uses 64-bit MIC value

# IEEE 802.1x Authentication:

Details:

- Originally developed for wired networks
- Provide greater degree of security by implementing port-based authentication
- Blocks all traffic on port-by-port basis until client is authenticated

Extensible Authentication Protocol (EAP):

- Framework for transporting authentication protocols
- Defines message format
- Uses four types of packets
    - Request
    - Response
    - Success
    - Failure
- Creates encrypted channel between client and authentication server

# Rogue AP System Detection:

Details:

- Uses 4 types of probes to monitor
    - Wireless device probe
    - Desktop probe
    - AP probe
    - Dedicated probe
- Once suspicious signal detected by probe
    - Information is sent to centralised database where WLAN management system software compares it to list of approved APs
    - Any device not on the list is considered a rogue AP

# AP Type:

Details:

- AP Types can be divided into
    - Fat vs Thin
    - Controller vs Standalone
    - Captive Portal APs

Fat vs Thin:

- Autonomous APs have the intelligence required to manage wireless authentication, encryption and other functions for the wireless devices they serve (FAT APs)
- Lightweight APs do not contain all the management and configuration functions found in fat APs (Thin APs)

Standalone vs Controller APs:

- Controllers APs can be managed through a dedicated wireless LAN controller (WLC)
- WLC is the single device that can be configured and settings are automatically distributed to all controller APs
- Advantages of controllers APs
    - Handoff procedure is eliminated because all authentications are performed in the WLC
    - Offers tools that provide for monitoring the environment and providing information regrading the best locations for APs, wireless AP configuration settings, and power settings

Captive Portal APs:

- Uses a standard web browser to provide information
- Gives the wireless user the opportunity to agree to a policy or present valid login credentials

# AP Configurations and Device Options:

Details:

- Other AP configuration are designed to limit the spread of RF signal so that as little as possible extends past the physical boundaries of the enterprise to be accessible to outsiders and attackers

Site Surveys:

- An in-dept examination and analysis of a WLAN site

Signal Strength Settings:

- Some APs allow adjustment of power level at which the WLAN transmits
- Reducing power allows less signal to reach outsiders

Spectrum Selection:

- Some APs allow the ability to adjust frequency spectrum settings such as
    - Frequency Band
    - Channel Selection
    - Channel Width

Antennas:

- APs should be located near the center or coverage area and placed high up to avoid theft
- Positioned so that the minimal amount of signal reaches past the boundaries of the building

Wireless Peripheral Protection:

- Vulnerabilities in wireless mice and keyboards are common which allow attackers to inject mouse movements or keystrokes from far away
- Protections
    - Updating or replacing vulnerable devices
    - Switching to fully tested bluetooth mice and keyboards
    - Use wired mouse and keyboards