# Chapter 4: Access Control

Created: Jan 21, 2020 2:06 PM
Updated: Mar 1, 2020 11:42 AM

**Objectives:**

- Describe the different type of authentication credentials
- Define access management and list the access control models
- List the best practices for access control

**Authentication Credentials:**

Where you are:

- Eg. Military Base, Home

What you have:

- Eg. Key fob to lock your car

What you are:

- Eg. Facial Characteristics

What you know:

- Eg. Combination to cipher lock

What you do:

- Eg. Do something to prove authenticity

**What you know, Passwords:**

Details:

- User logging into a system
- Asked to identify himself - Username
- Asked to authenticate - Passwords
- Passwords are the most common type of authentication today

Weaknesses:

- Long complex passwords are most effective, but hard to memorise
- Users must remember different passwords for many different accounts
- Each password should be unique
- Security policies mandating passwords must expire
- Users often take short cuts to use easy or weak passwords
- Weak passwords have sequences or patterns in them

Attacks on Passwords:

- Social Engineering:
    - Phishing
    - Shoulder Surfing
    - Dumpster Diving
- Capturing:
    - Keylogger
    - Man-in-the-middle
    - Replay attacks
- Resetting:
    - Attack accesses computer physically and changes passwords
- Offline Attack:
    - Steals file of password digest and compares against attacker's own digests
- Brute Force:
    - Every possible combination of passwords encrypted and matched against stolen file
    - Slowest, most thorough method
    - New Technology LAN Manager (NTLM)
        - NTLM passwords do not need to be broken, attacker sends stolen hash of password to system to authenticate himself
        - Known as pass the hash attack
- Mask Attack:
    - More targetted brute force that uses placeholders for characters in certain positions of the passwords
    - Parameters include password length, language, pattern, skips, character set
- Rule Attack:
    - Conducts a statistical analysis on the stolen passwords that is used to create a mask to break the largest number of passwords
- Dictionary Attack:
    - Attacker creates digests of common dictionary words and compares against stolen digest file
    - Pre-image attack - dictionary attack that uses a set of dictionary words and compares with stolen digest
    - Birthday Attack - Search for any two digests that are the same
- Rainbow Tables:
    - Creates a large pregenerated data set of candidate digests
    - Advantages:
        - Can be used repeatedly
        - Faster than dictionary
        - Less memory on attack machine required
- Password Collections
    - Attackers can steal thousands of passwords from a database
    - Gives them a large corpus of real world passwords
    - Gives them valuable insight on the strategic thinking of users when creating passwords

Security:

- User - Properly manage passwords
- Enterprise - Protecting password digests
- Recommendations for strong password:
    - Long passwords
    - Do not use dictionary words
    - Do not repeat characters, sequences or patterns
    - Do not use birthdays, pet names, addresses or personal information in general
    - Use non-keyboard characters
- Password managers:
    - Technology used for securing passwords
    - Password generator
    - Online vaults
    - Password management apps
- Protecting password digests (Salts):
    - Add random string to the user's clear text password before hashing
    - Makes dictionary and brute force attacks much slower and limits rainbow tables
- Protecting password digests (key stretching):
    - Specialised hash algorithm that is intentionally designed to be slower
    - Eg. brypt and PBKDF2
- Recommendation for salting and key stretching
    - Use a strong random number generator to create a salt of at least 128 bits
    - Input salt and user's plaintext password into PBKDF2 algorithm that uses HMAC-SHA-256 as core hash
    - Perform at least 30k iterations on PBKDF2
    - Capture first 256 bits of output from PBKDF2 as password digest
    - Store iteration count, salt and password digest in secure database

**What you have, Tokens, Cards:**

Authentication:

- Multi-factor:
    - User uses more than one type of authentication credential
    - Eg. Password + OTP
- Single-Factor:
    - Uses just one type of authentication
    - Eg. Only password

Tokens:

- Used to create OTPs that expire after a period of time
- Small device with a window display
- Advantages over passwords:
    - Changes frequently
    - Expires
    - If token is stolen, it is more obvious than if a password was stolen
- Time-based-on-time-password (TOTP)
    - Synced with authentication server
    - Code is generated from an algorithm
    - Code changes every 30-60 seconds
- HMAC-based-one-time-password (HOTP)
    - Event driven and changes when specific event occurs

Cards:

- Smart card contains integrated circuit chip that holds information
- Types:
    - Contact cards
    - Contact-less cards
    - Common access card

Cell Phones:

- Code can be sent to user's cell phone through an app on the device
- Allow a user to send a request via the phone to receive an authorization OTP code

**What you are, Biometrics:**

Standard Biometrics:

- Uses a person's unique physical characteristics for authentication
- Face, hand or eye characteristics used to authenticate
- Specialised Scanners:
    - Retinal scanners uses human retina to identify
    - Finger print scanners
    - Voice recognition micropones
    - Iris scanner uses a standard webcam
- Disadvantages:
    - Cost of hardware scanning devices
    - Readers can have error, accepts unauthorized and rejects authorized users
    - Can be tricked

Cognitive Biometrics:

- Relates to perception, thought process and understanding of the user
- Easier for user to remember since its based on their life experience
- Hard to imitate for attacker
- Some types
    - Picture password - User identifies 10 landmarks on a picture to touch
    - Requires user to identify specific faces
    - User selects one of several memorable events

**What you do, Behavioral Biometrics:**

Keystroke dynamics:

- Attempts to recognize the user's typing rhythm
    - All users type at different paces
    - Provides up to 98% accuracy
- Uses two unique typing variables
    - Dwell time - Time it takes to press and release a key
    - Flight time - time between keystrokes

**Access Control Models:**

Access Control:

- Granting or denying approval to use specific resources
- Physical - Consists of fencing, hardware door locks, mantraps
- Technical - Consists of technology restrictions that limit users on computers from accessing data

Discretionary Access Control (DAC):

- Least restrictive model
- Every object has an owner
- Owners have total control over their objects and give permissions to other subjects over their objects
- Used on operating systems like UNIX and Windows
- Weaknesses:
    - Poses a risk in that it relies on decisions made by the end user for security
    - Subject's permissions will be "inherited" by any programs the subject executes

Mandatory Access Control (MAC):

- Most restrictive access control model
- User has no freedom to set controls or distribute access to other subjects
- Usually found in military settings
- Two elements:
    - Label - Every entity is an object and is assigned a classification label that represents the relative importance of the object
    - Levels - Hierachy based on the labels used. Top secret has higher level than secret, which has a higher level than confidential etc.
- MAC grants permissions by matching object labels with subject labels

Role Based Access Control (RBAC):

- Access permissions are based on user's job function
- RBAC Assigns permissions to particular roles in an organisation, those roles are then assigned to users

Rule Based Access Control (RB-RBAC):

- Dynamically assigns roles to subjects based on a set of rules defined by a custodian
- Each resource object contains access properties based on the rules defined by a custodian
- When user attempts access, system checks object's rules to determine access permission
- Often used for managing user access to one or more systems

Attribute Based Access Control (ABAC):

- Uses more flexible polices than rules based AC
- Can combine attributes of object, subject and environment
- Formatted with If-Then-Else structure

![Chapter%204%20Access%20Control%20368253175dfb4222a63d376a3e0bc54b/Annotation_2020-01-21_214553.jpg](Chapter%204%20Access%20Control%20368253175dfb4222a63d376a3e0bc54b/Annotation_2020-01-21_214553.jpg)

**Best Practices for Access Control:**

Separation of duties:

- Requires two or more people responsible for functions related to Eg. handling money
- System is then not vulnerable to actions of a single person
- Fraud can result from a single user being trusted with complete control of a process
- Rule of Thumb - If a process can become a breach of security, process should be divided between two or more individuals

Job Rotation:

- Individuals periodically moved between job responsibilities, employees rotated within their department or across departments
- Limits amount of time individuals are in a position to manipulate security configurations
- Helps expose potential avenues for fraud
- Reduce employee burnout

Mandatory Vacations:

- Limits fraud because perpetrator must be present daily to conduct and hide fraudulent actions
- Audit of employee's activities usually scheduled during vacation for sensitive position

Clean Desk Policy:

- Ensure all confidential or sensitive materials are removed from workspace and secured when not in use
- Eg.
    - Computer workstations must be locked when workspace unoccupied or turned off
    - File cabinets to be kept closed and locked when not attended, and key must be properly secured
    - Laptops either locked with locking cable or locked in drawer