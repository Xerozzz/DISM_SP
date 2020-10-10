# Chapter 3: Footprinting

# Learning Outcomes

- Footprinting or Information Gathering
- Use Web tools for footprinting
- Use DNS and DNS zone transfers
- Viewing information in HTTP
- Identify the types of social engineering

---

# What is Footprinting?

- Discover information about the organization and its network
- Usually such information is available on the Internet
- Information gathered may be used to determine how to conduct security test
    - Size of the network
    - Operating systems used

## Information Gathering

- Numerous resources to find information legally
- Identify methods others can use to find information about your organization
- Companies should try to limit the amount of information that is available publicly

## What are some information that would be useful?

### Domains

- The target may own more than one domain

### Visible Systems

- How many systems can be accessed publicly?

### Software Services Available

- What are the main public services provided and their versions?
- Test are generally for standard service ports like 21,22,25,80 and 443

### IP Addresses Discovered

- Knowing their range of IP addresses may tell us how big their networks are

### Gateway Routers

- This may tell you who their ISP is

### Primary Operating Systems Being Used

- Windows, Linux or other OS?

### Firewalls

- Which kind of Firewalls are they using

### Intrusion Detection Systems/Intrusion Prevention Systems

- Is there one?
- Will it track us?

### Web Technologies

- Is their using Python, Javascript, ActiveX etc?
- Are they hosting their web servers in-house or using cloud technologies

## Web Tools

### Google Groups

- Search for email addresses in postings in technical or nontechnical newsgroups

### Whois

- Gather IP and domain information
- Domain names are registered with NICs

### SamSpade

- Gather IP and domain information like who owns a domain, contact information etc
- Versions available for UNIX and Windows OSs

### Google Advanced Search

- Search for web sites and company data

### Namedroppers

- Run a domain name search
- More than 30 million domain names updated daily

### White Pages

- Conduct reverse phone number lookups and retrieve address information

### Metis

- Gather competitive intelligence from websites

### Dig

- Perform DNS zone transfers
- Replaces nslookup command

### Host

- Obtain host IP and domain information
- Can also be used to initiate DNS zone transfers

### Netcat

- Read and write data to ports over a network

### Wget

- Retrieve HTTP, HTTPS and FTP files over the Internet

### Paros

- Capture web server information and possible vulnerabilities in a web site's pages that could allow exploits such as SQL injection and buffer overflows

### Email Addresses

- Find email address format to guess other employee's email accounts
- Bounce an email using a non-existent account by reading mail header get information about servers
- Tools to find corporate employee information (groups.google.com)

### Analyzing a Company's Web Site

- Web pages are an easy source of information like preferred web technologies, type of OS, webserver etc
- Simplest tool is browser
- Tools for intercepting proxies can be used like Paros, Webscarab, BurpSuite
- Developer Tools feature on Web Browsers

### Copying Whole Websites

- Tools are available to copy the whole website
- The pages of the website can then be inspected and analyzed offline
- HTTrack Website Copier

## Using DNS (Domain Name Service)

### DNS

- DNS resolves host names to IP addresses
- People prefer using URLs to IP addresses
- Can be vulnerable

### DNS Query Tools

- nslookup
- Dig
- Host
- Whois

### Using DNS Zone Transfers

- Zone transfer enables you to see all hosts on a network
- Gives you organization's network diagram
- Determine company's primary DNS server and look for the Start of Authority (SOA) record
- Show zones or IP addresses

### Other DNS Whois Tools

- www.whois.net
- Greenwich
- Wikto
- SmartWhois
- ActiveWhois
- SpiderFoot
- www.dnsstuff.com
- www.mxtoolbox.com

## Traceroute

- To trace the route of packets from source to destination
- May be used to find out the gateways/routers used by the target
- Uses ICMP (Windows) or UDP (Linux)
- TTL values is used to trace the route
- However, routers may block the packets from a traceroute

## Using HTTP Basics

- HTTP operates on port 80
- Use HTTP language to pull information from a webserver
- Basic understanding of HTTP is beneficial for security tresters
- Return codes to reveal information about system
- GET / HTTP/1.1 is the most basic method

![Chapter%203%20Footprinting%2041470709fe054383a3ea166d1e90c4c4/Untitled.png](Chapter%203%20Footprinting%2041470709fe054383a3ea166d1e90c4c4/Untitled.png)

![Chapter%203%20Footprinting%2041470709fe054383a3ea166d1e90c4c4/Untitled%201.png](Chapter%203%20Footprinting%2041470709fe054383a3ea166d1e90c4c4/Untitled%201.png)

### HTTP Headers

- Every HTTP packet contains a set of header fields
- HTTP headers may contain information on
    - Web browser of the client making the request
    - Operating system of the client
    - Web server returning the response
    - Cookies

## Social Engineering

- Using knowledge of human nature to get information from other people
- Can be biggest security threat to networks
- Most difficult to protect against

### Techniques of Social Engineers

- Urgency
- Help with problems
- Everyone else is doing
- Kindness and charm
- Authority

### Shoulder Surf

- Look at what the user is entering on the keyboard, especially usernames and passwords
- Shoulder surfers may stand behind people at the ATMs to see the PINs being entered
- Use of camera phones to take photos and videos increase this threat

### Dumpster Diving

- Going through the trash
- Lots of valuable information can be found
    - Discarded Windows XP manuals
    - Company organizational charts
    - Printouts of emails
    - Discarded hard disks, USB drives — deleted data may still be retrieved from them
- Use disk-cleaning software to wipe out all data before discarding disks

### Piggybacking

- Trailing authorized staff closely to enter restricted areas
- May carry a fake staff card or badge and rely on the kindness of people to hold the door open for them
- May carry big boxes and rely on people to open secured doors for them

### Phishing

- Phishing emails are urgent emails that seem to be from legitimate companies asking you to click on a link provide or update your details
- The link usually leads to the attacker's website
- Spear phishing sent to specific people in an organization
- Can occur in mobile messages

## Viewing Email Headers

- Learn how to find email headers
- After you open email headers, copy and paste them into a text document
- Headers contain valuable information about the sender

### Information in Email Headers to look out for

- Return path
- Recipient's email address
- Type of sending email service
- IP address of sending server
- Name of the email server
- Unique message number
- Date and time email was sent
- Attachment files information