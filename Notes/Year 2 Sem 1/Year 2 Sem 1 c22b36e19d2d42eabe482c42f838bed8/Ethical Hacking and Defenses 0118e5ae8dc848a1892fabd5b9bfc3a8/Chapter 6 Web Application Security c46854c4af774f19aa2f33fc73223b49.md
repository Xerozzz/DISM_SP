# Chapter 6: Web Application Security

# Vulnerabilities

- OWASP Top 10 Vulnerabilities

## Common Vulnerabilities

- Cross site scripting
- Forceful browsing
- Parameter tampering, cookie poisoning and hidden field manipulation
- SQL injection

## Sample Vulnerable Web Apps

- Sample web applications designed with vulnerabilities for learning
- DVWA
- Webgoat
- Badstore

# Character Encoding

## Encoding

### ASCII Table

- Search on the Internet for ASCII table

### UTF-8

- One of the common encoding schemes used on the web
- Each character represented by 8 bits
- Values in the rage 0 to 127 represent each of the ASCII characters

## Attackers

- Attackers try to use methods to disguise their attack strings
- For eg. "www%2eyahoo%2ecom", where the ASCII code 2E is used to disguise the "."
- Possible URL attack for SQL injection attack:

![Chapter%206%20Web%20Application%20Security%20c46854c4af774f19aa2f33fc73223b49/Untitled.png](Chapter%206%20Web%20Application%20Security%20c46854c4af774f19aa2f33fc73223b49/Untitled.png)

- The above link executed SQL query "SELECT preferences FROM logintable WHERE userid="bob"; update logintable set password = "123"; --

# Cross Site Scripting (XSS)

- Can occur when the website takes information entered by the user and displays it in a web page without validating the input first
- A hacker will enter specially crafted information that will cause the web page to generate unexpected output

![Chapter%206%20Web%20Application%20Security%20c46854c4af774f19aa2f33fc73223b49/Untitled%201.png](Chapter%206%20Web%20Application%20Security%20c46854c4af774f19aa2f33fc73223b49/Untitled%201.png)

## Example

- Hackers may enter scripts like "<script>alert("hello")</script>"
- New browsers try to guard against such scripts

![Chapter%206%20Web%20Application%20Security%20c46854c4af774f19aa2f33fc73223b49/Untitled%202.png](Chapter%206%20Web%20Application%20Security%20c46854c4af774f19aa2f33fc73223b49/Untitled%202.png)

## How It Works

- Relies on the ability to inject content into the web page
- Besides creating a pop-up windows, XSS can be used to
    - Deface a website
    - Redirect the user to another page
    - Manipulate the Document Object Model (DOM)
    - Any functions like "windows.alert", read or write files etc
    - "Poison" cookies
    - Others

## Stored XSS

- Happens when the attacker enters specially crafted input and it is stored on the web application
- The attacker's crafted input is loaded when other users visit the website
- Eg. Attacker enter malicious input into a Review or Comments textarea, other web visitors who visit the Reviews/Comments page will load the malicious code

## How To Fix XSS Vulnerability

- Look for codes that takes input directly from user and post it back into the webpage
- Perform data sanitization and encode "<" and ">" with "&gt;" and "&lt"
- Advanced XSS can escape simple encoding checks so you have to use more stringent control and explicitly check for allowable characters instead

### Other Ways To Mitigate

- Most lanaguages have functions that can be used to encode output for safe display in HTML
    - & becomes &amp
    - < becomes &lt
    - > becomes &gt
    - " becomes &quot

# Cross-Site Request Forgery (CSRF)

- User has logged into a website successfully and is browsing the site
- Usually the user would have multiple tabs open in his web browser and he is also surfing other sites at the same time
- If he encounters a malicious website with CSRF, his web browser may send unwanted requests to the authenticated website

## Attacks

- Because user is already authenticated or identified to the website, the attacker can cause transactions to be carried out in the user's account
- The website thinks the request is a valid one from a valid user

## How To Mitigate

- Besides authenticating user, website can authenticate request as well
- Send challenge token/data associated with current user session with the request or Re-authenticate the user with one time passwords
- Users should log off properly
- When preforming important transactions like Internet Banking, don't open multiple windows or tabs to surf other sites

# Forced Browsing

- Web servers generally access files that are reachable from its document root
- CGI may allow access to files not in document root
- Attacker can craft an input via the browser to retrieve files not intended for him

## Example

- John is viewing his web documents and notes the URL

![Chapter%206%20Web%20Application%20Security%20c46854c4af774f19aa2f33fc73223b49/Untitled%203.png](Chapter%206%20Web%20Application%20Security%20c46854c4af774f19aa2f33fc73223b49/Untitled%203.png)

- He changes "john" to "mary" and views Mary's documents

![Chapter%206%20Web%20Application%20Security%20c46854c4af774f19aa2f33fc73223b49/Untitled%204.png](Chapter%206%20Web%20Application%20Security%20c46854c4af774f19aa2f33fc73223b49/Untitled%204.png)

- He tries to access admin's pages

![Chapter%206%20Web%20Application%20Security%20c46854c4af774f19aa2f33fc73223b49/Untitled%205.png](Chapter%206%20Web%20Application%20Security%20c46854c4af774f19aa2f33fc73223b49/Untitled%205.png)

- John may even be able to access files in other directories of the web server

![Chapter%206%20Web%20Application%20Security%20c46854c4af774f19aa2f33fc73223b49/Untitled%206.png](Chapter%206%20Web%20Application%20Security%20c46854c4af774f19aa2f33fc73223b49/Untitled%206.png)

![Chapter%206%20Web%20Application%20Security%20c46854c4af774f19aa2f33fc73223b49/Untitled%207.png](Chapter%206%20Web%20Application%20Security%20c46854c4af774f19aa2f33fc73223b49/Untitled%207.png)

## Scanning Tools

- Using scanning tools like Paros can help find other directories and webpages

## Mitigating Vulnerability of Forced Browsing

- Parse the parameters if they are being used to access files like "/" or "\"
- Avoid common names for admin page like "admin/", "admin.php" etc
- Restricted web pages need to check if user is authenticated
- Expires session variables as quickly as it is practical for your application

# Command Execution

- Poorly designed websites may allow attackers to enter commands that will be executed on the web server

# SQL Injection

- Most web application interacts with database to persistently store data
- Connection to database requires login credentials to be presented during execution
- Interface to database are typically through construction of "queries" using SQL
- Programmers may assume user will always key in username and password

## Definition

- Technique where attackers manipulate the input data so as to execute query other than the intended one

## Methods

- Simple injection with " or 1-1 - -"

![Chapter%206%20Web%20Application%20Security%20c46854c4af774f19aa2f33fc73223b49/Untitled%208.png](Chapter%206%20Web%20Application%20Security%20c46854c4af774f19aa2f33fc73223b49/Untitled%208.png)

- If used for login processing, the first record being returned will be the login user

## Techniques

- Effects of SQL injection can also be to cause error
- Error messages can reveal important data
- These data can in turn be used to perform further exploitation

## Error Message

- Inject quotes such as ' " reveal details of query
- Eg, from below we know "hash" is a column name for password

![Chapter%206%20Web%20Application%20Security%20c46854c4af774f19aa2f33fc73223b49/Untitled%209.png](Chapter%206%20Web%20Application%20Security%20c46854c4af774f19aa2f33fc73223b49/Untitled%209.png)

## Finding out Table Column

- SQL injection requires creativity
- "and pass =" abc can be used to guess column names
- If it isn't, an error message will return and you can keep guessing

## Meta Information

- Most databases has tables that store information about the database
- Called metadata or data dictionary

## More SQL Information

- Using UNION to find out table names and columns
- ' union select table_name from information_schema.tables --
- Number of columns in UNION operation MUST match
- Cycle through the entire table names
- ' union select table_name from information_schema.tables where table_name NOT in ('CHARACTER_SETS') --

## Stored Procedures

- Most data have stored procedures similar to functions
- Typically used for Data Validation, Access Control and Batch Processing

## Blind SQL Injection

- Advanced SQL injection technique
- Does not respond with a retrieval of data from the database
- The attacker can only make inference from the success or failure of the SQL execution
- A failure of the execution will usually show a different page or general error message

## Other SQL Operations

- Update records like password or modify data
- Insert fake records like login credentials
- Delete records

## Mitigate SQL Vulnerability

- Validate or sanitize input from users
- Use prepared statements or stored procedures
- Limit database access permissions
- Do not let web app access database with database admin account

### Database Login

- Hard coding of login credentials in web pages is NOT a good practice
- Can result in leaking of credentials through viewing of source codes

### Fixing Vulnerability

- Store encrypted login credential in text files
- Use hardware security module for decryptions, also known as CryptoBox
- Limit account privilege and disallow access to metadata
- Restrict clients who can access database server

# Data Tampering

- HTTP Messages carry lots of information like Cookie Values, Form Data, Query String and HTTP Headers
- Undesirable effects may occur when any of these information is tampered

## Form Data

- Form data are passed to the web server through either POST or GET methods
- Most developers uses client-side validation like JS
- Validation can be bypassed easily through direct manipulation of form data

### Hidden Fields

- Used in certain applications to maintain state or preserve information about transaction
- Not really hidden

## Cookie Values

- A common way to store user information
- Essentially a text file stored locally
- Can be tricked to write cookies of another domain

# Session Hijacking

- Exploits the XSS vulnerability in the application
- Victim logs into the system
- XSS page sends session ID to the attacker
- Attacker logs in to the system and replaces his session ID with that of victim

## Fixing Web Vulnerability

- Do not trust user input
- Cookies should not be used entirely for authentication
- Use HTTP_REFERER to check for page origin
- Use USER_AGENT to check the user's web browser
- HTTPS or other forms of encryption can be used to protect session cookie transmission

# Error Messages

- Applications need to respond to error
- Some errors are made by users and can be corrected by users, application informs users about errors
- Some errors are system related and not meant for users

## Problem

- Application often reveals too much information, more than is needed
- Default configuration of web server

## Examples

### Shows File Path

![Chapter%206%20Web%20Application%20Security%20c46854c4af774f19aa2f33fc73223b49/Untitled%2010.png](Chapter%206%20Web%20Application%20Security%20c46854c4af774f19aa2f33fc73223b49/Untitled%2010.png)

### Shows whether username is correct

![Chapter%206%20Web%20Application%20Security%20c46854c4af774f19aa2f33fc73223b49/Untitled%2011.png](Chapter%206%20Web%20Application%20Security%20c46854c4af774f19aa2f33fc73223b49/Untitled%2011.png)

### Reviews System Information

![Chapter%206%20Web%20Application%20Security%20c46854c4af774f19aa2f33fc73223b49/Untitled%2012.png](Chapter%206%20Web%20Application%20Security%20c46854c4af774f19aa2f33fc73223b49/Untitled%2012.png)

## Fixing This Vulnerability

- Application codes, functional codes and error handling codes
- Start looking at error strings
- Make sure they don't reveal too much information
- Extensive testing of error handling

### Guidelines for Error Messages

- Does the user have minimal information he needs for corrective action
- Does this message provide more information about the system than is available from other legitimate sources
- Is each piece of information disclosed useful or necessary for the user?
- Does the corrective advice in the error message disclose sensitive information

## Tools to Intercept HTTP data

- Paros Proxy
- BurpSuite
- OWASP WebScarab