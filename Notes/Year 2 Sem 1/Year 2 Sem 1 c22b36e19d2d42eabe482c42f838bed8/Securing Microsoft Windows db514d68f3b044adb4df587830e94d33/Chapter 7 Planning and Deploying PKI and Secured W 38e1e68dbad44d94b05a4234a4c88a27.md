# Chapter 7: Planning and Deploying PKI and Secured Web Content Access Services

# Part 1

# Defining Certificate Requirements

- Microsoft WinServer enables secure data access based on the use of digital certificates
- Certificates allow users or systems to prove to others that they are who they say they are
- Before you can use digital certificates, you need to design a Public Key Infrastructure (PKI)

## Use Cases of Certificates

- Digital Signatures
- Secured Email or HTTP communication (TLS,SSL)
- Internet authentication
- Software code signing
- IPSec
- Smart card logon
- Encrypted file system
- 802.1x authentication

## Protecting Message Exchanges from Eavesdropping

- A key pair is associated with an individual party
- Each individual party will keep its private key as a secret but share out its public key to everyone
- Messages being encrypted with the public key can only be decrypted by the corresponding private key
- A digital signed message with the individual private key can only be verified by its corresponding public key
- The problem is how to obtain a genuine public key of a party before establishing a secure communication channel with the party?

## Questions for Certificates

- How do we tell if it is genuine?
- Why do we need it?

## Public Key Infrastructure (PKI)

- Refers to a technology that includes a series of features relating to authentication and encryption
- Based on a system of certificates, each certificate contains a public key and the name of the subject
- Allows an organization to publish, use, renew and/or revoke certificates and enroll clients

# Certificate Authority

- A certificate authority is an entity that issues digital certificates to other parties
- The Root CA can issue certificates to Subordinate or Intermediate or Issuing CAs
- Issuing CAs can issue certificates to users or clients

## Types of Hierarchies used for CAs

### Rooted trust model

![Chapter%207%20Planning%20and%20Deploying%20PKI%20and%20Secured%20W%2038e1e68dbad44d94b05a4234a4c88a27/Untitled.png](Chapter%207%20Planning%20and%20Deploying%20PKI%20and%20Secured%20W%2038e1e68dbad44d94b05a4234a4c88a27/Untitled.png)

- A model in which the root CA has a self-signed certificate and the CA issues a certificate to all direct subordinate CAs
- CAs in this model can be online or offline and allows flexibility in deploying or managing PKI
- Each CA serves a single role within the hierarchy and is not dependent on other CAs, allows rooted trust hierarchies to be more scalable and easier to administer than other hierarchies
- Possible to add a new CA to a hierarchy
- Rooted trust falls into 2 sub-categories, two-tier and three-tier CA hierarchy
- Any CA in a rooted trust hierarchy is either a root or a subordinate but never both
- Each CA is responsible for processing requests, issuing or revoking certificates and publishing CRLs
- Each CA can be managed independently

### Cross-certification trust model

![Chapter%207%20Planning%20and%20Deploying%20PKI%20and%20Secured%20W%2038e1e68dbad44d94b05a4234a4c88a27/Untitled%201.png](Chapter%207%20Planning%20and%20Deploying%20PKI%20and%20Secured%20W%2038e1e68dbad44d94b05a4234a4c88a27/Untitled%201.png)

- A model in which all CAs are self-signed and trust relationships between CAs are based on cross-certificates
- Certificates issued by one CA will be trusted by computers which belong to other CA hierarachy
- Cross-certificates do not need to be bi-directional
- Advantage is that it is low cost and has higher flexibility
- Disadvantage is that there is greater administrative overhead and increased risk of an unauthorized access to internal resources

### Third-Party CAs

- Useful when an orgnization conducts most of its business with external customers and clients
- Some examples of 3rd party CAs include DigiCert, GlobalSign and GoDaddy
- Advantage is that customers have greater degree of confidence when the third party CA is trusted and it allows an organization to take advantage of third party CA's understand of technical, legal and business issues with certificate uses
- Disadvantage is that it has high per-certificate cost, allows less flexibility in managing certs and auto-enrollment is not possible
- Windows Systems are already configured with a list of trusted commercial third party CAs

## Roles that can be chosen for CAs

- **Standalone CAs:** Rudimentary or Intermediate CA
- **Enterprise CAs:** Basic-security, Medium-security or High-security CA

# How Setting up CA Works

## Installing Certificate Authority Roles

- Root CA is installed first, followed by installing intermediate CAs, then finally issuing CAs
- Root CA is the top of the certification hierarchy and must be trusted unconditionally by clients in the organization
- An enterprise root CA stores its information in AD and the server that hosts the service must be joined to a domain, storing the root CA offline is much more secure
- Intermediate CA is the subordinate to the root CA
- Issuing CA issues certificates to users and computers

## Selecting A Certificate Enrollment And Renewal Method

- Depends on types of certificates you want to use and the number and type of clients you enroll
- Two types, manual and automatic

### Manual

- Use if administrative approval is required
- Most useful for issuing and renewing computer and IPSec certificates

### Automatic

- Use if approval is not needed
- Can improve administrative control over certificates

### Methods for Automatic Enrollment

- Certificate autoentrollment and renewal based on a combination of Group Policy settings and certificate templates
- Certificate Request Wizard and Certificate Renewal Wizard
- Web enrollment support pages
- Smart card enrolment station

## Obtaining Certificate from Issuing CA

![Chapter%207%20Planning%20and%20Deploying%20PKI%20and%20Secured%20W%2038e1e68dbad44d94b05a4234a4c88a27/Untitled%202.png](Chapter%207%20Planning%20and%20Deploying%20PKI%20and%20Secured%20W%2038e1e68dbad44d94b05a4234a4c88a27/Untitled%202.png)

## Configuring Certificate Templates

- Certificate services provides certificate templates to simplify the process of requesting and issuing certificates
- Each template contains the rules and settings to serve a single or multiple purpose
- Certificate templates are available only on Enterprise Root and Subordinate CAs
- Stored in AD and available to every enterprise CA in the forest
- Restrict permissions on your CAs to prevent unauthorized Access
- Configure the Discretionary Access Control List (DACL) for each template

![Chapter%207%20Planning%20and%20Deploying%20PKI%20and%20Secured%20W%2038e1e68dbad44d94b05a4234a4c88a27/Untitled%203.png](Chapter%207%20Planning%20and%20Deploying%20PKI%20and%20Secured%20W%2038e1e68dbad44d94b05a4234a4c88a27/Untitled%203.png)

### Certificate Templates MMC Snap-In Uses

- Create additional templates by duplicating and modifying existing templates
- Modify template properties
- Configure policies applied to certificate enrollment, issuance and application
- Allow the autoentrollment of certificates
- Configure ACLs on certificate templates

### Ways to Control Issuance of Certificate Requests

- Configuring permissions on the template from Security tab
- Preventing the CA from issuing that certificate type by deleting the template
- Configuring permissions on your CA

## Configuring Archival and Recovery of Keys

- Possible to configure the CA to archive private keys of certificates at the time of issuance which enables recovery of the key should it be lost
- Only highly trusted individuals should be granted the privilege of archiving and recovering keys
- Certificate Services does not archive private keys by default
- Key recovery methods include the key recovery agent, certutil tool and krt.exe

## Deploying and Revoking Certs for Users, Computers and CAs

- Possible to automate the deployment of certificates by configuring Group Policy
- Manual approval should be required for all certificates that are needed to perform network administration, software development or issued to joint venue partners

### Conditions to Auto-Enroll Certificates

- Client computer must be integrated into AD
- Users require the Read, Enroll and Autoenroll permissions

### Reasons for Revoking a Certificate

- Certificate is compromised
- Termination of the account to whom the certificate was issued

![Chapter%207%20Planning%20and%20Deploying%20PKI%20and%20Secured%20W%2038e1e68dbad44d94b05a4234a4c88a27/Untitled%204.png](Chapter%207%20Planning%20and%20Deploying%20PKI%20and%20Secured%20W%2038e1e68dbad44d94b05a4234a4c88a27/Untitled%204.png)

### Certificate Revocation List

- All certificates have specified lifetimes
- IN some situations, there is a need to invalidate or revoke a certificate before the end of its lifetime
- Revoked certifications are published in the certificate revocation list (CRL)
- CRLs are valid only for a limited time and PKI clients need to retrieve a new CRL periodically
- Must define the CRL location along with the access path before deploying certificates

# OCSP and OCSP Responder

## OCSP

- Online Certificate Status Protocol
- An internet protocol used for obtaining the recovation status of an X.509 digital certificate
- It complements but does not replace the operations of CRLs

## OCSP Responder

- A server typically run by the certificate issuer which returns a signed response on the status of a particular issued certificate
- Possible responses are Good, Revoked, Unknown or no response if the issuer does not implement the responder service

## Comparison to CRLs

- Less network and storage burden for clients to maintain CRLs
- Easier to implement compared to CRLs for up to date checking
- OCSP uses non-encrypted message and may be subjected to interception
- OCSP is an optional component for the cert server

# Part 2

# Secured Web Access

## Issues with not securing web access

- How to authenticate identity of the remote server? Hackers may setup phishing sites
- How to ensure the transferred content is not tampered or intercepted by unauthorized parties
- For enterprise servers, they need a solution to authenticate the identity of the remote clients trying to access their services

## Deploying and Managing SSL Certificates

- A certificate-based SSL features in IIS consists of a server certificate, an optional client certificate and various digital keys
- Can be obtain from trusted third-party CA or created using Certificate Services

## IIS Authentication Methods

![Chapter%207%20Planning%20and%20Deploying%20PKI%20and%20Secured%20W%2038e1e68dbad44d94b05a4234a4c88a27/Untitled%205.png](Chapter%207%20Planning%20and%20Deploying%20PKI%20and%20Secured%20W%2038e1e68dbad44d94b05a4234a4c88a27/Untitled%205.png)

## HTTPS

- A technology that encrypts individual messages in Web communications rather than establishing a secure channel
- Popular ecommerce technology and is used for secure online shopping
- Communicates on port 443
- SSL-Secured URLs begin with https:// prefix

## Configuration of Web Servers for SSL Certificate Use

- Use SSL encryption only for sensitive information as encrypted transmissions can significantly reduce transmission rates and server performance
- Server certificates provides a way for users to confirm the identity of the website
- A server certificates contains the organization name affiliated with the server content, name of the organization that issued the certificate and a public key used to establish an encrypted connection

## Self-Issued Certificates

### Considerations of Issuing your own certificate

- Microsoft Certificate Services can accommodate different certificate formats and provide for auditing and logging of certificate-related activity
- Evaluate the cost of each
- Keep the learning curve in mind
- Evaluate the willingness of outside vendors clients to trust your organization as a certificate supplier

## Publicly Issued Certificates

- Used when a user suspects your self-issued certificates
- Certificates can be obtained from a mutually trusted third party CA like VeriSign or GlobalSign
- Wait time can take up to several days or months
- Must be renewed on a regular basis

### General Rules About Any Types of Web Certificates

- Each website can only have one server certificate assigned to it
- One certificate can be assigned to multiple websites
- You can assign multiple IP addresses per website
- You can assign multiple SSL ports per website

## Configuration of Client for SSL Certificates

### Typical Client Certificate Contents

- Identity of the user
- Identity of the certification authority
- A public key used for establishing encrypted communications
- Validation information such as an expiration date and serial number

### Protecting webcontent from unauthorized access

- Use Basic, Digest or Integrated Windows authentication in addition to requiring a client certificate
- Create a Windows account mapping for client certificates

## Certificate Renewal

### Security and Renewal Requirement Factors

- Value of the network resources protected by the CA trust chain
- Degree to which you trust your certificate users
- Amount of administrative effort that you are willing to devote to certificate renewal and CA renewal
- Business value of the certificate