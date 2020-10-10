# Module 4: AWS Cloud Security

# Learning Outcomes

- AWS Shared Responsibility Model
- AWS IAM
- Securing a new AWS account
- Securing accounts
- Securing Data on AWS
- Working to ensure compliance

---

# Part 1: AWS Shared Responsibility Model

![Module%204%20AWS%20Cloud%20Security%208a7ea03894c941e98f6d491a2af592ab/Annotation_2020-05-05_170307.jpg](Module%204%20AWS%20Cloud%20Security%208a7ea03894c941e98f6d491a2af592ab/Annotation_2020-05-05_170307.jpg)

## Customers Responsibility: Security in the cloud

- Patching and maintaining EC2 instances
- Passwords and role based access to applications
- Security group configurations
- OS and host-based firewalls, IDS and IPS
- Network configurations
- Account management and user credentials

## AWS Responsibility: Security of the cloud

- Physical Security of data centers with controlled needs-based access
- Hardware and software infrastructure with OS access logging and auditing
- Network infrastructure with intrusion detections
- Virtualization Infrastructure by using instance isolation

---

# Part 2: AWS IAM

## Definition

- Used to manage access to AWS resources
- Who can access the resource
- Which resources can be accessed by whom and what can they do to the resource
- How resources can be accessed
- No cost AWS account feature

## Essential Components

### IAM User

- Person or application that can authenticate with an AWS account
- Uses an IAM username and password to identify and authenticate
- May have multi-factor authentication as well for higher security
- Can be assigned access to CLI and SDK or just Management console only

### IAM Group

- Collection of IAM users that are granted identical authorization
- Cannot be nested and have no default group
- A user can belong to multiple groups
- Can only contain users
- Easy way to assign a policy to multiple users

### IAM role

- Useful mechanism to grant a set of permissions for making AWS service requests
- Lets a user assume a role to access a service not normally available temporarily
- Meant to be assumed by users for specific needs for limited duration
- Like the sudo command in linux

## Authorization

- Assign permissions by creating an IAM policy
- Permissions determine which resources and operations are allowed
- All permissions denied by default
- If something is denied, it is never allowed
- Best Practice: Follow the principle of least privilege

## IAM policy

- Document that defines which resources can be accessed and the level of access to each resource
- If denied and allowed, will always be denied
- Default is to deny
- Two types, identity-based and resource-based

    ![Module%204%20AWS%20Cloud%20Security%208a7ea03894c941e98f6d491a2af592ab/Annotation_2020-05-05_171820.jpg](Module%204%20AWS%20Cloud%20Security%208a7ea03894c941e98f6d491a2af592ab/Annotation_2020-05-05_171820.jpg)

    ![Module%204%20AWS%20Cloud%20Security%208a7ea03894c941e98f6d491a2af592ab/Annotation_2020-05-05_171953.jpg](Module%204%20AWS%20Cloud%20Security%208a7ea03894c941e98f6d491a2af592ab/Annotation_2020-05-05_171953.jpg)

### Identity-Based Policies

- Attach a policy to any IAM entity (IAM user, group or role)
- Specifies what actions the entity can do and what it cannot do
- Single policy can be attached to multiple entities
- Single entity can have many policies attached to it

### Resource-Based Policies

- Attached to a resource like S3 bucket or EC2 instance
- Specifies who has access to the resource and what actions they can perform on it

## Example

![Module%204%20AWS%20Cloud%20Security%208a7ea03894c941e98f6d491a2af592ab/Annotation_2020-05-05_172158.jpg](Module%204%20AWS%20Cloud%20Security%208a7ea03894c941e98f6d491a2af592ab/Annotation_2020-05-05_172158.jpg)

---

# Part 3: Securing a new AWS account

## Best Practice

- Do not use AWS root user unless necessary

## Actions that Only Root User can Do

- Update account root user password
- Change AWS Support plan
- Restore IAM user's permissions
- Change account settings like contact information

## Steps to Secure Your New Account

### Step 1: Stop using the root account as soon as possible

- Create IAM user for yourself and save access keys if needed
- Create an IAM group and give it full admin permissions then add the IAM user into the group
- Disable and remove root user access keys
- Enable password policy for users and sign in with new IAM user credentials
- Store the root credentials safely

### Step 2: Enable MFA

- Require MFA for root user and all IAM users
- Use MFA to control access to AWS service APIs

### Step 3: Use AWS CloudTrail

- Tracks user activity on your account
- Logs all API Requests to resources in all supported services
- Enables by default and is free
- Contains management event data on the latest 90 days of account activity
- Can create a S3 bucket for log storage to go beyond 90 days

### Step 4: Enable Billing Reports

- Provides information about AWS resources use and estimated costs for that use
- Reports are delivered to an S3 bucket you specify

---

# Part 4: Securing Multiple Accounts

## AWS Organizations

- Account management service to consolidate multiple AWS to centrally management them

### Security Features

- Group AWS accounts into OUs and attach different access policies to each OU
- Integration and support for IAM
- Use service control polices to establish control over AWS services and API actions the account can access

### Service Control Policies

- Offer centralized control over accounts
- Limit permissions that are available in an account that is part of an organization
- Ensures that accounts comply with access control guidelines
- Similar to IAM permissions policies

## AWS Key Management Service (KMS)

- Enables you to create and manage encryption keys
- Enables you to control the use of encryption across AWS services and in your applications
- Integrates with AWS CloudTrail to log all key usage
- Uses hardware security modules (HSMs) that are validated by Federal Information Processing Standards (FIPS) 140-2 to protect keys

## Amazon Cognito

- Adds user sign-up, sign-in and access control to your web and mobile applications
- Scales to millions of users
- Supports sign-in with social identity providers like Facebook, Google and Amazon

## AWS Shield

- A managed DDOS protection service
- Safeguards applications running on AWS
- Provides always-on detection and automatic inline mitigations
- Standard is enabled for no cost, Advanced is an optional paid service
- Used to minimize application downtime and latency

---

# Part 5: Securing Data on AWS

## Encryption At Rest

- Uses secret keys managed by AWS KMS to encode and decode your data and metadata

## Encryption in Transit

- Uses TLS and SSL for encryption
- AWS Certificate Manager is a way to manage, deploy and renew TLS or SSL certificates
- HTTPS creates a secure tunnel for exchange of data

## Ways To Protect S3 Data

- Amazon S3 Block Public Access
- IAM Policies
- Bucket Policies
- Access Control Lists
- AWS Trusted Advisor

---

# Part 6: Working To Ensure Compliance

## AWS Compliance Programs

- AWS engages with certifying bodies and independent auditors to provide customers with detailed information about policies, processes and controls established and operated by AWS

## AWS Config

- Assess, audit and evaluate the configurations of AWS Resources
- Use for continuous monitoring of configurations
- Review configuration changes
- View detailed configuration histories
- Simplify compliance auditing and security analysis

## AWS Artifact

- A resource for compliance related information
- Provide access to security and compliance reports and select online agreements
- Can view and track AWS agreements and certifications