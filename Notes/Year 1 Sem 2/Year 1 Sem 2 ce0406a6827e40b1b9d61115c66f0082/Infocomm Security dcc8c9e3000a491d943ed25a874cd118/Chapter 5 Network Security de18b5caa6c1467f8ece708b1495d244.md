# Chapter 5: Network Security

Created: Jan 26, 2020 10:17 PM
Updated: Feb 18, 2020 11:53 AM

**Objectives:**

- Describe the different types of networking-based attacks
- Explain how servers are attacked

**Networking-Based Attacks:**

- Interception attacks
- Poisoning attacks

**Interception Attacks:**

Man-in-the-middle:

- Interception of legitimate communication and forging a fake response to sender
- Two computers sending and receiving data with a computer between
- Usually happens between user and server

Man-in-the-browser:

- Intercepts communication between parties to steal or manipulate the data
- Happens between browser and user
- Usually begins with a Trojan infecting the computer and installing an extension into the browser configuration
- Extension waits for a specific webpage where user enters sensitive information
- Extension then captures all data when the submit button is pressed
- May modify data submitted as well
- Advantages
    - Difficult to recognise that malicious code has been installed as it is distributed through Trojans
    - Infected browser may remain dormant for months until user visits target website
    - MITB software resides exclusively within a browser, making it hard to detect by anti-virus software

Replay Attacks:

- Attacker makes copy of transmission before sending it to original recipient
- Methods to prevent
    - Both sides can negotiate and create a random key that is valid for a limited period or for specific processes
    - Use timestamps in all messages and reject messages that fall out of a window of time

**Poisoning Attacks:**

ARP Poisoning:

- Address Resolution Protocol (ARP)
    - If IP address is known but MAC isn't, sending computer sends an ARP packet to determine MAC address
    - MAC addresses stored in ARP cache
    - All computers that hear ARP reply also cache the data
- Relies upon MAC spoofing, which is imitating another computer by changing MAC Address
- Types of Attacks
    - Steal data
        - An attacker can substitute her own MAC address and steal data intended for another device
    - Prevent Internet Access
        - An attacker substitutes an invalid MAC address for network gateway to disable access to external networks
    - Man-in-the-Middle
        - MITM device set to receive all communications by substituting that MAC address
    - DOS Attack
        - IP address of target can be substituted with an invalid MAC address, causing all traffic destined for it to fail

DNS Poisoning:

- Substitutes DNS addresses to redirect a computer to another website
- Usually happens in local host table or external DNS server

[Chapter%205%20Network%20Security%20de18b5caa6c1467f8ece708b1495d244/untitled](Chapter%205%20Network%20Security%20de18b5caa6c1467f8ece708b1495d244/untitled)

Privilege Escalation:

- Access rights
    - Privilege to access hardware and software resources that are granted to users
- Exploiting a software vulnerability to gain access to resources that they would normally be restricted from accessing
- Vertical Privilege Escalation
    - When a lower privilege user accesses functions restricted to higher privilege users
- Horizontal Privilege Escalation
    - When a user with restricted privilege accesses different restricted functions of a user of the same privilege level

**Server Attacks:**

- Compromised server can provide threat actors with its privileged contents or provide an opening for attacking any device connected to the server
- Type of Attacks:
    - DOS
    - Web server application attacks
    - Hijacking
    - Overflow attacks
    - Advertising attacks
    - Exploiting browser vulnerabilities

Denial of Service (DOS):

- Deliberate attempt to prevent authorized users from accessing a system by overwhelming it with requests
- Smurf Attack
    - Attacker broadcasts a network request to all computers on network but spoofs the source IP address
    - Appears as if victim is asking for response from all computers
    - Victim is then overwhelmed by all computer's response
- DNS Amplification Attack
    - Floods a victim by redirecting valid responses to it
    - Uses public and open DNS servers to flood a system with DNS response traffic
- SYN Flood
    - Takes advantages of procedures for initiating a session
    - Attacker sends SYN segments in IP packets to the server
    - Attacker modifies source address of each packet to computer addresses that are invalid

Web Server Application Attacks:

- Zero-day attack
    - Attack that exploits previously unknown vulnerabilities, giving victim no time to prepare or defend against it
- Traditional network security devices can block traditional network attacks but not always block web application attacks
- Cross-Site Scripting Attack (XSS)
    - Threat actor takes advantage of web applications that accept user input without validating it and presents it back to user
    - When user visits injected web site, malicious instructions are sent to victim's browser
    - Designed to retain and steal information
    - Requires a website to accept user input without validating it and uses the input in a response
- Cross-Site Request Forgery (XSRF)
    - Uses victim's web browser to impersonate the victim
    - If a user is currently authenticated on a website and is tricked into loading another webpage, the new page inherits the identity and privileges of the victim to perform an undesired function on attacker's behalf
- SQL Injection
    - Inserts statements to manipulate SQL Database server
    - Attacker enters fictitious email address that included a single quotation mark as part of the data
    - Response lets attacker know whether input is validated
    - Attacker enters email field in SQL statement
    - Statement is processed and all user email addresses will be displayed

[Chapter%205%20Network%20Security%20de18b5caa6c1467f8ece708b1495d244/untitled%201](Chapter%205%20Network%20Security%20de18b5caa6c1467f8ece708b1495d244/untitled%201)

Hijacking:

- Session Hijacking
    - Attacker attempts to impersonate user by stealing or guessing session token which is a random string assigned to an interaction between user and web app
    - Done by
        - Using XSS or other attacks
        - Eavesdropping on transmission
        - Guessing the session token
- URL Hijacking
    - Users are directed to a fake look-aside website full of ads
    - Attacker receives money for traffic generated to the site
    - Attacker purchases domain names similar to legitimate ones
    - Bitsquatting
        - Requesting domain names that are one bit different from original
- Domain Hijacking
    - When a domain pointer that links a domain name to a specific web server is changed by a threat actor
    - Attacker gains access to domain control panel and redirects registered domain to different web server
- Clickjacking
    - Hijacks mouse click
    - User is tricked into clicking a link that is other than what it appears to be
    - Done by embedding another invisible HTML document inside main document

Overflow Attacks:

- Buffer Overflow
    - Occurs when a process attempts to store data in RAM beyond the boundaries of a fixed length storage buffer
    - Extra data overflows into adjacent memory locations
    - Attacker can overflow the buffer with a new address pointing to his malicious code
- Integer Overflow
    - Occurs when the result of an arithmetic operation exceeds the maximum size of the integer type used to store it
    - Attacker changes the value of a variable to something outside the range the programmer had intended
    - Attacker can use integer overflow to create a buffer overflow situation
    - Can reverse flow of money by wrapping a positive value of bank transfer to become negative value

Advertising Attacks:

- Malvertising
    - Attacker uses third-party advertising networks to distribute malware to unsuspecting users who visit well-known sites
    - Redirects visitors who receive it to the attacker's webpage
    - Can result in Trojans and ransomware being installed onto victim device
    - Hard to Prevent
        - Website operators are unaware of the types of ads being displayed
        - Users have a false sense of security going to a "mainstream" website
        - Turning off ads that support plug-ins such as Adobe Flash often disrupts user's web experience
- Ad Fraud
    - Attacker manipulate pre-roll ads to earn ad revenue
    - Methbot used to spoof ad auctions

Browser Vulnerabilities:

- Scripting Code
    - Malicious JS program can capture and remotely transmit user information without user knowledge or authorization
- Extensions
    - Expand the normal capabilities of a web browser
    - Mostly written in JS
    - Browser dependent, only works on one browser
- Plug-Ins
    - Adds new functionality to web browser such as playing music
    - Eg. Java, Adobe Flash Player
- Add-Ons
    - Add a greater degree of functionality to web browser
    - Can do
        - Create additional browser toolbars
        - Change browser menus
        - Process content of every webpage loaded

[Chapter%205%20Network%20Security%20de18b5caa6c1467f8ece708b1495d244/untitled%202](Chapter%205%20Network%20Security%20de18b5caa6c1467f8ece708b1495d244/untitled%202)