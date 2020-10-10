# Chapter 2: System Security I

Created: Jan 15, 2020 10:16 PM
Updated: Jan 15, 2020 11:32 PM

**Objectives:**

- Define malware
- List the different types of malware
- Identify payloads of malware
- Describe the types of psychological social engineering attacks
- Explain physical social engineering attacks

**Malware:**

- Malicious software that enters a computer system without's the owner's knowledge or consent
- Uses a threat vector to unload a malicious payload that performs a harmful function once invoked
- General term referring to harmful or annoying software

Circulation:

- Spreading rapidly to other systems in order to impact a large number of users
- Worms, Viruses

Infection:

- How it embeds itself into a system

Concealment:

- Avoid detection by concealing its presence from scanners

Payload Capabilities:

- What actions the malware performs

**Virus:**

Type of Viruses:

- Computer Virus:
    - Malicious computer code that reproduces itself on the same computer
- Program Virus:
    - Infects an executable program file
- Macro:
    - A series of instructions that can be grouped together as a single command

Infection Method:

- Appender Infection:
    - Virus appends itself to end of a file
    - Easily detected by virus scanners
- Swiss Cheese Infection:
    - Virus scrambles itself to make it harder to detect then injects itself into executable code
- Split Infection:
    - Virus splits itself into several parts and places them at random positions in host program
    - Parts may contain random "garbage" doe to mask their true purpose
- Mutation:
    - Oligomorphic virus changes its internal code to one of a set of number of predefined mutations whenever executed
    - Polymorphic virus completely changes from its original form when executed
    - Metamorphic virus rewrites its own code and appears differently each time it is run

Actions:

- Unloads a payload to perform malicious action
- Reproduces itself by inserting its code into another file on the same computer
- Causes computer to crash
- Erases or re-formats hard drive
- Turns off computer security settings
- Relies on user to spread by sending infected files

**Worms:**

- Malicious program that uses a computer network to replicate, sends copies of itself to other network devices

Actions:

- Consume resources or leave behind a payload to harm infected systems
- Delete computer files
- Allows remote control of a computer by an attacker

**Trojans:**

- Executable program that does something other than advertised
- Contains hidden code that launches an attack
- Remote Access Trojan (RAT) - gives the threat actor unauthorized remote access to victim's computer via specially configured communication protocols

**Ransomware:**

- Prevents a user's device from properly operating until a fee is paid
- A variation of ransomware display a fake warning that a software license has expired or there is a problem and users must purchase additional software online to fix the problem

**Crypto-Malware:**

- A more malicious form of ransomware where threat actors encrypt all files on the device so that none of them can be opned
- Once infected, the software connects to the attackser's command and control server to receive updated or instructed data
- A locking key is generated for the encrypted files and that key is encrypted with another key from attacker's C&C
- Second key is sent to victim once ransom is paid

**Rootkits:**

- Software tools used by attacker to hide actions or presence of malicious software
- Hides or remove traces of log-in records and log entries
- May alter or replace existing operating system files with modified versions that are specifically designed to ignore malicious activity

**Payload Capabilities:**

Collect Data:

- Spyware:
    - Software that gathers user information without consent
    - Uses computer's resources for the purposes of collecting and distributing personal or sensitive information
- Keylogger:
    - Captures and stores each keystroke the user types on the keyboard
    - Attacker searches captured text for any useful information such as passwords or credit card numbers
    - Can be a small hardware device inserted via USB port or program installed on the computer
    - Often installed as a Trojan or virus
- Adware:
    - Program that delivers advertising content in a manner unexpected and unwanted by user
    - May open browsers randomly
    - May display objectionable content
    - Interrupts user productivity and slow computer processes
    - Annoying and a nuisance

Delete Data:

- Logic Bomb:
    - Computer code that lies dormant until it is triggered by a specific logical event
    - Difficult to detect before triggered
    - Often embedded in large computer programs not routinely scanned

Modify System Security:

- Backdoor:
    - Gives access to a computer, program, or service that circumvents normal security to give program access
    - Allows attacker to return at a later time and bypass security settings

Launch Attacks:

- Botnet:
    - Group of bot computers gathered into a logical computer network called a botnet under the control of the attackers
    - Bots/zombie is an infected computer under the remote control an attacker
    - Infected zombie computers wait for instructions through a command and control structure from bot herders usually via HTTP
- Botnet Attacks:
- Spamming:
    - Botnets can be used to send massive amounts of spam
- Spreading Malware:
    - Botnets are used to spread malware and create new bots and botnets.
- Manipulating Online Polls:
    - Because each bot has a unique Internet Protocol address, each vote by a bot is deemed as legit and can tip the scales in favor of someone
- Denying Services:
    - Botnets can flood a web server with thousands of requests and overwhelm it to the point that it cannot respond to legitimate request

**Social Engineering:**

- Means of gathering information for an attack by relying on the weaknesses of individuals

Psychological Approaches:

- Persuade the victim to provide information or take action
- Variety of techniques used:
    - Provide a reason
    - Project confidence
    - Use evasion and diversion
    - Make them laugh
- Impersonation:
    - Attacker pretends to be someone else
    - Eg. Help desk support technician, IT support, Manager, Repairperson
    - Attackers often impersonate a person with authority because victim generally resist saying "no" to people in power
- Phishing:
    - Sending a fake email claiming to be legitimate source
    - Tries to trick user into giving private or personal information
    - Emails and fake websites hard to distinguish from legitimate ones
    - Spear Phishing - Targets specific users
    - Whaling - targets the "big fish"
    - Vishing - Instead of using email, uses a telephone call instead
- Spam:
    - Unsolicited e-mail
    - Primary vehicle for distribution of malware
    - Cost very little to send millions of spam
    - Filters look for specific words to block spam email
    - Image spam - uses graphical images of text in order to circumvent text-based filters
- Hoaxes:
    - False warning usually claiming to come form IT team
    - Attackers try to get victims to change configuration settings on their computers that would allow the attacker to compromise the system
    - Attacker may give a telephone number for the victim to call, which puts them in direct contact with attacker
- Watering Hole Attack:
    - Malicious attack that is directed toward a small group of specific individuals who visit the same website
    - Eg. Major executives working for a manufacturing company may visit a common website such as parts supplier

Physical Approaches:

- Dumpster Diving:
    - Digging through trash to find information that can be useful in an attack
- Google Dorking:
    - Electronic version of dumpster diving to look for documents and data posted online
- Tailgating:
    - Following an authorized individual through an access door
    - An employee could conspire with an unauthorized person to allow him to walk him in (piggyback)
    - Watching an authorized user enter a security code on a keypad is known as shoulder surfing