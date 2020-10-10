# Chapter 1a: Network Protocols

# Learning Outcome

- Introduction to Kali Linux
- Wireshark
- Hypertext Transfer Protocol (HTTP and HTTPS)
- Ports
- File Transfer Protocol (FTP)
- Telnet
- SSH (Secure Shell), SCP, SFTP

---

# Wireshark

## Description

- Open source packet analyzer
- Network traffic can be captured and stored for offline analysis
- Displays information in packets in human-readable format

## Usage

- Better understand how protocols work
- Reassemble captured network traffic

---

# HTTP

## HTTP

- Normally runs on Port 80
- Data not encrypted

## HTTPS

- Used to encrypt HTTP data
- Normally runs on Port 443

## HTTP Methods

### GET

When the client requests for a webpage, the request is sent as a HTTP GET method. Most commonly used HTTP method

### POST

When the client submit some data in a webform, the data is sent as a HTTP POST method

### HEAD

Similar to GET but returned packet only has HTTP headers, with no response body and used for testing

### PUT

To replace a resource specified in URL, **VERY DANGEROUS**

### DELETE

To delete a resource specified in URL

### TRACE

Perform a loopback test to the specific resource specified in URL

### OPTIONS

Describe communication options available

---

# Netstat

A command available on both Windows and Linux to display opened ports and current connections

---

# Comparing Different Protocols for Remote Access

## FTP

- Protocol for copying files between systems
- Normally runs on Port 20 for data connection
- Normally runs on Port 21 for control connections
- No encryption
- Can use alternatives like SFTP

## Telnet

- Allows a user to login remotely to another system
- Normally runs on Port 23
- Old protocol, not encrypted
- SSH is better and more secure now

## Secure Shell (SSH)

- Popular application for remote login
- Normally runs on Port 22
- Data is encrypted
- SCP and SFTP work over SSH Protocol to allow secured file transfers