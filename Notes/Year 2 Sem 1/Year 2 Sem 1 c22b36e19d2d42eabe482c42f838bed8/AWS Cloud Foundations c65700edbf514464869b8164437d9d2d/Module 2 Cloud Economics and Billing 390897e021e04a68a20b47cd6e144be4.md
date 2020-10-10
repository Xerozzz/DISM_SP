# Module 2: Cloud Economics and Billing

# Learning Outcome

- Understand the AWS pricing philosophy
- Review fundamental pricing characteristics

---

# Part 1: Fundamentals of AWS Pricing

## AWS Pricing Fundamentals

### Three fundamental drivers of cost with AWS

- Compute (charged per hour/second, varies by instance type)
- Storage (Typically charged per GB)
- Outbound data transfer (Outbound is aggregated and charged)

### No charge

- Inbound data transfer
- Data transfer between services within the same region

## AWS Pricing

### Pay for what you use

- Pay only for services you consume with no large upfront expenses
- Save money on servers and infrastructure
- Available on demand

### Pay less when you reserve

- Save up to 75%
- Options:
    - All up-front reserved instance (AURI) → Largest discount
    - Partial up-front reserved instance (PURI) → Lower discounts
    - No up-front payments reserved instance (NURI)  → Smaller discount
- Benefits
    - Minimize risk
    - Predictably manage budget
    - Comply with policies that require long-term contracts

### Pay less when you use more

- Savings as usage increases
- Tiered pricing for services, the more you use, the less you pay per GB
- Data transfer IN is always free
- Multiple storage services deliver lower storage costs based on needs
- Benefits
    - Choosing the right combination of storage options helps you reduce cost while preserving performance, security and

### Pay even less as AWS grows

- AWS focuses on lowering cost of doing business
- Future higher-performing resources replace current resources for no extra charge
- AWS lowers prices as it grows

### Custom Pricing

- Meet varying needs through custom pricing
- Available for high-volume projects with unique requirements

## AWS Free Tier

- Helps customers get started in the cloud to try

### Limitations

- Only new customers
- Up to one year
- Applicable to only certain services and options

### Services with No Charge

- Amazon VPC
- AWS Identity and Access Management (IAM)
- Consolidated Billing
- AWS Elastic Beanstalk
- AWS CloudFormation
- Automatic Scaling
- AWS OpsWorks

---

# Part 2: Total Cost of Ownership (TCO)

## On-Premises vs Cloud

![Module%202%20Cloud%20Economics%20and%20Billing%20390897e021e04a68a20b47cd6e144be4/Annotation_2020-04-27_153322.jpg](Module%202%20Cloud%20Economics%20and%20Billing%20390897e021e04a68a20b47cd6e144be4/Annotation_2020-04-27_153322.jpg)

![Module%202%20Cloud%20Economics%20and%20Billing%20390897e021e04a68a20b47cd6e144be4/Annotation_2020-04-27_153505.jpg](Module%202%20Cloud%20Economics%20and%20Billing%20390897e021e04a68a20b47cd6e144be4/Annotation_2020-04-27_153505.jpg)

## What is Total Cost of Ownership (TCO)?

- TCO is the financial estimate to help identify direct and indirect costs of a system

### Why use TCO?

- To compare the costs of running an entire infrastructure environment or specific workload on-premises vs on AWS
- To budget and build the business case for moving to the cloud

### TCO Considerations

- Server costs (Hardware servers, software OS etc)
- Storage costs (Hardware storage disks, Storage administration)
- Network costs (Hardware LAN switches, Network admin costs)
- IT labor costs (Server admin costs)

### AWS Simple Monthly Calculator

- Estimates monthly costs
- Identify opportunities to reduce monthly costs
- Use templates to compare services and deployment models

---

# Part 3: AWS Organizations

## Definition

- Used for consolidated billing of multiple accounts
- Free account management service
- Organization security management capabilities

## Terminology

### Organizational Unit (OU)

- Branch for accounts
- Branch can contain other branches

### Root

- The very top

### Account

- Can only be under one branch

## Key Features and Benefits

- Policy-based account management
- Group based account management
- APIs that automate account management
- Consolidated billing

## Security with AWS Organizations

- Control access with AWS Identity and Access Management (IAM)
- IAM policies enable you to allow or deny access to AWS services for users, groups or roles
- Service control policies allow you to allow or deny access to AWS services for individuals or group accounts in an organizational unit

## Set Up

- Create organization in current AWS account as master account
- Create 2 organizational units and place member accounts in OU
- Create service control policies to allow or deny access to AWS services
- Test restrictions

## Accessing AWS Organizations

- AWS Management Console
- AWS CLI Tools
- Software Development Kits (SDKs)
- HTTPS Query API

---

# Part 4: AWS Billing and Cost Management

## AWS Billing Dashboard

- Used to see spend summary for the month
- Spend by Service, shows which service used most and how muc hit used

## Tools

### AWS Budgets

- Budgets can be tracked at monthly, quarterly etc
- Budget alerts can be configured to send via email or AWS SNS

### AWS Cost and Usage Report

- Provides detailed explanation of costs and tax
- Billing reports can be publish in Amazon S3

### AWS Cost Explorer

- Visualizes your cost and usage of services
- Provides forecasted numbers for the coming month

### AWS Bills Page

- Listed the cost of the previous month by which service and in which region
- Detailed break down of costs

---

# Part 5: AWS Technical Support Plans

## AWS Support Tools

### Provide unique combination of tools and expertise:

- AWS Support
- AWS Support Plans

### Support is provided for:

- Experimenting with AWS
- Production use of AWS
- Business-critical use of AWS

### Proactive guidance

- Technical Account Manager (TAM)

### Best Practices

- AWS Trusted Advisor

### Account Assistance

- AWS Support Concierge

## AWS Support Plans

### Basic Support

- Resource center access
- Service Health Dashboard
- Product FAQs
- Discussion forums
- Support for health checks
- Limited number of technical support cases

### Developer Support

- Support for early development on AWS
- Best practice guidance
- Client-side diagnostic tools
- Building block features support

### Business Support

- Customers that run production workloads
- Full access to AWS Trusted Advisor and use case guidance
- API to interact with Support Center and Trusted Advisor

### Enterprise Support

- Customers that run business and mission-critical workloads
- Full access to AWS Trusted Advisor and use case guidance
- API to interact with Support Center and Trusted Advisor
- Access to a technical account manager
- Management business reviews

---

# Summary

- Explored the fundamentals of AWS pricing
- Reviewed TCO concepts
- Introduced AWS Simple Monthly Calculator and TCO Calculator
- Reviewed the Billing Dashboard
- Reviewed  Technical Support options and costs