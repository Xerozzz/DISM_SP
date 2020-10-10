# Module 6: Compute

# Learning Outcomes

- Compute Services Overview
- Amazon EC2
- Amazon EC2 Cost Optimization
- Container Services
- Introduction to AWS Lambda
- Introduction to AWS Elastic Beanstalk

---

# Part 1: Compute Services Overview

![Module%206%20Compute%205e405ef45bae4d53bbada87300ca836f/Annotation_2020-05-21_140751.jpg](Module%206%20Compute%205e405ef45bae4d53bbada87300ca836f/Annotation_2020-05-21_140751.jpg)

## Choosing The Optimal Compute Service

### Aspects To Consider

- What is your app design?
- What are your usage patterns?
- Which configuration settings will you want to manage?

---

# Part 2: Amazon EC2 Part 1

## Example Uses

- Application server
- Web Server
- Database Server
- Game Server
- Mail Server
- Media Server
- Game Server
- Many mores

## Overview

- Provides virtual machines in the cloud
- Gives you full control over the guest OS (Windows or Linux)
- You can launch any number of instances of any size into any AZ in the world
- Launch instances with a few clicks or line of code
- Control traffic in and out of these instances

## 1. Select an AMI

### AMI (Amazon Machine Image) is a template used to create an EC2 instance

- Contains an OS
- Often have software pre-installed

### AMI Choices:

- Quick start — AMIs provided by AWS
    - My AMIs — That you created
    - AWS Marketplace — Pre-configured templates from third parties
    - Community AMIs — AMIs shared by others, not checked, use at your own risk
- Creating a new AMI example:

![Module%206%20Compute%205e405ef45bae4d53bbada87300ca836f/Annotation_2020-05-21_141501.jpg](Module%206%20Compute%205e405ef45bae4d53bbada87300ca836f/Annotation_2020-05-21_141501.jpg)

## 2. Select an instance type

- Consider how your EC2 Instance will be used

### Instance type you choose determines:

- RAM
- Processing Power
- Disk space and disk type
- Network performance

### Different instance type categories:

- General purpose (a1,m4,m5,t2,t3) — Broad
- Compute optimized (c4,c5) — High Performance
- Memory optimized (r4,r5,x1,z1) — In-memory Databases
- Storage optimized (f1,g3,g4,p2,p3) — Machine Learning
- Accelerated computing (d2,h1,i3) — Distributed File Systems

### Networking Features:

- Network bandwidth varies by instance types
- Enhanced networking types are supported on most instance types to get higher performance and lower latency

### Enhanced networking types:

- Elastic Network Adapter (ENA) — Supports network speeds up to 100Gbps
- Intel 82599 Virtual Function Interface — Supports network speeds up to 10Gbps

---

# Part 3: Amazon EC2 Part 2

## 3. Specify Network Settings

### Where should the instance be deployed?

- Identify the VPC and optionally the subnet

### Should a public IP address be automatically assigned?

- To make it internet-accessible

## 4. Attach IAM Role (Optional)

### Will software on EC2 instances need to interact with other AWS services?

- If yes, attach an appropriate IAM role

### Instance profile

- An AWS IAM role that is attached to an EC2 instance is kept in an instance profile
- You are not restricted to attaching a role only at instance launch
- You can attach a role to an instance already running

## 5. User Data Script (Optional)

- Optionally specify a user data script at instance launch
- Use user data scripts to customize the runtime environment of your instance
- The script is run the first time the instance starts
- Can be used strategically to install required packages or update software
- Easier to use than creating custom AMIs

## 6. Specify Storage

- Configure the root volume where the OS is installed
- Attach additional storage volumes if you want to

### For each volume, specify:

- Size of the disk in GB
- Volume type, SSD or HDD
- If the volume will be deleted when instance is terminated
- If encryption should be used?

### Amazon EC2 Storage Options

- Amazon Elastic Block Store (EBS):
    - Durable block-level storage volume
    - Data remains when you stop and start the isntance
- Amazon EC2 Instance Store:
    - Storage provided on disks that are attached to the host computer where the EC2 instance is running
    - If instance stops, data stored here is deleted
    - If instance reboots intentionally or unintentionally, data is not lost
- Other options for storage that is not the root volume
    - Mount an Amazon Elastic File System (EFS)
    - Connect an Amazon S3 bucket

### Example Storage Options

![Module%206%20Compute%205e405ef45bae4d53bbada87300ca836f/Annotation_2020-05-21_143106.jpg](Module%206%20Compute%205e405ef45bae4d53bbada87300ca836f/Annotation_2020-05-21_143106.jpg)

---

# Part 4: Amazon EC2 Part 3

## 7. Add Tags

- Tags are a label you assign to an AWS resource
- Consists of key and optional value
- Lets you attach metadata to an EC2 instances

### Potential Benefits

- Filtering
- Automation
- Cost allocation
- Access control

## 8. Security Group Settings

- A set of firewall rules that control traffic to the instance
- Exists outside of the instance OS

### How does it work?

- Create rules that specify the source and which ports that network communications can use
- Specify the port number and protocol, such as TCP, UDP or ICMP
- Specify the source that is allowed to use the rule

## 9. Identify Or Create The Key Pair

- Key pair consists of a public key AWS stores and a private key you store
- Enables secure connections to the isntance
- You have to specify an existing key pair or new key pair

### Connecting to Windows AMIs

- Use the private key to obtain the administrator password that you need to log in to your instance

### Connecting to Linux AMIs

- Use the private key to use SSH to securely connect to the instance

## Launching EC2 Instances Through The Command Line Interface (CLI)

- EC2 instances can also be created programmatically

### Example Commands

- This example assumes that key pair and security groups already exist
- More options can be specified, view *AWS CLI Command Reference* for details

![Module%206%20Compute%205e405ef45bae4d53bbada87300ca836f/Annotation_2020-05-21_144610.jpg](Module%206%20Compute%205e405ef45bae4d53bbada87300ca836f/Annotation_2020-05-21_144610.jpg)

## AWS EC2 Instance Lifecycle

![Module%206%20Compute%205e405ef45bae4d53bbada87300ca836f/Annotation_2020-05-21_144726.jpg](Module%206%20Compute%205e405ef45bae4d53bbada87300ca836f/Annotation_2020-05-21_144726.jpg)

## Consider Using An Elastic IP Address

- Rebooting an instance will not change any IP addresses or DNS hostnames
- When an instance is stopped and then started again, the public IPv4 address and external DNS hostname will change
- Private IPv4 address and internal DNS hostnames will not change
- If you require a persistent public IP address, associate an Elastic IP address with the instance

### Elastic IP address characterisitcs

- Can be associated with instances in the Region as needed
- Remains allocated to your account until you choose to release it
- Default only allows 5 max

## EC2 Instance Metadata

- Data about your instance
- View in a browser by typing *http://ip_address/latest/meta-data*
- View in terminal window with *curl http://ip_address/latest/meta-data/*
- Can be used to configure or manage a running instance

## Amazon CloudWatch For Monitoring

- Used to monitor EC2 Instances
- Provides near-real-time metrics
- Provides charts in the Amazon EC2 console Monitoring tab that you can view
- Maintains 15 months of historical data

### Basic Monitoring

- Default with no extra cost
- Metric data sent to CloudWatch every 5 minutes

### Detailed Monitoring

- Fixed monthly rate for seven pre-selected metrics
- Metric data delivered every 1 minute

---

# Part 5: Amazon EC2 Cost Optimization

## Pricing Models

### On-Demand Instances

- Paid by the hour
- No long-term commitments
- Lowest costs
- Eligible for Free Tier

### Dedicated Hosts

- A physical server with EC2 instance capacity fully dedicated to your use

### Dedicated Instances

- Instances that run in a VPC on a hardware that is dedicated to a single customer

### Reserved Instances

- Full, partial or no upfront payment for instance you reserve
- Discount on hourly charge for that instance
- 1-year or 3-year term

### Scheduled Reserved Instances

- Purchase a capacity reservation that is always available on a recurring schedule you specify
- 1 year term

### Spot Instances

- Instances run as long as they are available and your bid is above the price
- Can be interrupted by AWS with a 2 minute notification
- Interruption options include termination, stopping or hibernation
- Prices can be significantly less compared to On-Demand Instances
- Good choice when you have flexibility in when your application can run

## Pricing Model Benefits

### On-Demand

- Low cost and flexibility with no contract

### Spot Instances

- Large scale and dynamic workload

### Reserved Instances

- Predictability ensures compute capacity is available when needed

### Dedicated Hosts

- Save money on licensing costs
- Helps meet compliance and regulatory requirements

## Pricing Model Use Cases

### On-Demand

- Short term or spiky unpredictable workloads
- App development or testing

### Spot Instances

- Application with flexible start and end times
- Apps only feasible at low compute prices
- Users with urgent computing needs for large amounts of additional capacity

### Reserved Instances

- Steady state or predictable usage pattern
- Apps that require reserved capacity including disaster recovery
- Users able to make upfront payments to reduce total computing costs in future

### Dedicated Hosts

- Bring your own license
- Compliance and regulatory restricitons
- Usage and licensing tracking
- Control instance placement

## Four Pillars Of Cost Optimization

### Right Size

- Provision instances to match the need (CPU, Storage etc)
- Pick the right instance type for your use
- Use amazon CloudWatch metrics to find out how idle are instances and when
- Best practice: Find the right size, then reserve

### Increase Elasticity

- Stop or hibernate Amazon EBS-backed instances that are not in use
- Use automatic scaling to match needs based on usage for automated and time-based elasticity

### Optimal Pricing Model

- Leverage the right pricing model for your use case
- Optimize and combine purchase types
- For example
    - Use On-Demand and Spot Instances for variable workloads
    - Use Reserved for predictable workloads
- Consider serverless solutions like AWS Lambda

### Optimize Storage Choices

- Reduce costs while maintaining storage performance and availability
- Resize EBS Volumes and change EBS Volume Types to meet performance requirements with less expensive options
- Delete EBS Snapshots that are no longer needed
- Identify the most appropriate destination for specific types of data
    - Do you need to use EBS?
    - Using Amazon S3 or Glacier with lifecycle policies can reduce costs

## Measure, Monitor and Improve

- Cost optimization is an ongoing process

### Recommendations

- Define and enforce cost allocation tagging
- Define metrics, set targets and review regularly
- Encourage teams to architect for costs
- Assign the responsibility of optimization to an individual or team

---

# Part 6: Container Services

## Definitions

- A method of OS virtualization

## Benefits

- Repeatable
- Self-Contained execution environments
- Software can run the same in different environemnts
- Faster to launch, stop and terminate than virtual machines

## What is Docker?

- A software platform that enables you to build, test and deploy applications quickly
- You can run containers on Docker created from templates called image
- A container has everything a software app needs to run

## Containers vs Virtual Machines

![Module%206%20Compute%205e405ef45bae4d53bbada87300ca836f/Annotation_2020-05-21_151854.jpg](Module%206%20Compute%205e405ef45bae4d53bbada87300ca836f/Annotation_2020-05-21_151854.jpg)

- One VM runs on one EC2 instance
- Multiple containers can run on one EC2 instance with process isolation and docker engines

## Amazon Elastic Container Service (ECS)

- A highly scalable fast container management service

    ![Module%206%20Compute%205e405ef45bae4d53bbada87300ca836f/Annotation_2020-05-21_152128.jpg](Module%206%20Compute%205e405ef45bae4d53bbada87300ca836f/Annotation_2020-05-21_152128.jpg)

### Key Benefits

- Orchestrates the execution of Docker containers
- Maintains and scales the fleet of nodes that run your containers
- Removes the complexity of setting up the infrastructure

### Features Integrated that are familiar to EC2 users

- Elastic Load Balancing
- Amazon EC2 Security Groups
- Amazon EBS Volumes
- IAM Roles

### ECS Cluster

- A group of EC2 Instances that run containers
- Distributes containers into EC2 instances in a way that accounts for CPU and memory capacity available on cluster nodes

### ECS Cluster Options

- Backed by AmazonEC2 to provide more granular control over infrastructure
- Backed by AWS Fargate to have easier maintenance and allow you to focus on your applications

    ![Module%206%20Compute%205e405ef45bae4d53bbada87300ca836f/Annotation_2020-05-21_152352.jpg](Module%206%20Compute%205e405ef45bae4d53bbada87300ca836f/Annotation_2020-05-21_152352.jpg)

## What is Kubernetes?

- Open source software for container orchestration
- Allows you to deploy and manage containerized applications at scale
- The same toolset can be used on premises and in the cloud

### Complements Docker

- Docker enables you to run multiple containers on a single OS host
- Kubernetes orchestrates multiple Docker host nodes

### Automates

- Container Provisioning
- Networking
- Load Distribution
- Scaling

## Amazon Elastic Kubernetes Service (EKS)

- Enables you to run Kubernetes on AWS
- Certified Kubernetes conformant for easy migration
- Supports Linux and Windows containers
- Compatible with Kubernetes community tools and support popular Kubernetes add-ons

### Used to

- Manage clusters of Amazon EC2 compute instances
- Run containers that are orchestrated by Kubernetes on those instances

### Why EKS and ECS?

- To provide flexibility and more options to best suit your needs

## Amazon Elastic Container Registry (ECR)

- Fully managed Docker container registry that makes it easy for developers to store, manage and deploy Docker container images
- Can be used with Amazon EKS also

---

# Part 7: Introduction to AWS Lambda

## Definition

- Event-Driven serverless compute service

    ![Module%206%20Compute%205e405ef45bae4d53bbada87300ca836f/Annotation_2020-05-21_152924.jpg](Module%206%20Compute%205e405ef45bae4d53bbada87300ca836f/Annotation_2020-05-21_152924.jpg)

    ## Benefits

    - Supports multiple programming languages
    - Completely automated administration
    - Built-in fault tolerance
    - Supports the orchestration of multiple functions
    - Pay-per-use pricing

    ## Lambda Event Sources

![Module%206%20Compute%205e405ef45bae4d53bbada87300ca836f/Annotation_2020-05-21_153138.jpg](Module%206%20Compute%205e405ef45bae4d53bbada87300ca836f/Annotation_2020-05-21_153138.jpg)

## Lambda Function Configuration

![Module%206%20Compute%205e405ef45bae4d53bbada87300ca836f/Annotation_2020-05-21_153233.jpg](Module%206%20Compute%205e405ef45bae4d53bbada87300ca836f/Annotation_2020-05-21_153233.jpg)

## Lambda Function Examples

### Schedule-Based Lambda Function Example

- Starting instances in the morning when people come to work
- Stop instances at night when people go home

![Module%206%20Compute%205e405ef45bae4d53bbada87300ca836f/Annotation_2020-05-21_153410.jpg](Module%206%20Compute%205e405ef45bae4d53bbada87300ca836f/Annotation_2020-05-21_153410.jpg)

### Event-Based Lambda Function Example

![Module%206%20Compute%205e405ef45bae4d53bbada87300ca836f/Annotation_2020-05-21_153455.jpg](Module%206%20Compute%205e405ef45bae4d53bbada87300ca836f/Annotation_2020-05-21_153455.jpg)

## Lambda Limits

- View additional limits in *AWS Lambda Limits Documentation*
- Soft limits can be lifted through requests
- Hard limits cannot be changed

### Soft Limits per Region

- Concurrent executions = 1000
- Function and layer storage =75 GB

### Hard Limit for individual functions

- Maximum function memory allocation = 3008 MB
- Function timeout = 1 sec to 15 mins
- Deployment Package size = 250 MB unzipped, including layers

---

# Part 8: Introduction to AWS Elastic Beanstalk

## Definition

- Easy way to get web applications up and running
- No additional charge for Elastic Beanstalk, only pay for the underlying resources that are used

## AWS Elastic Beanstalk Handles

- Infrastructure provisioning and configuration
- Deployment
- Load balancing
- Automatic scaling
- Health monitoring
- Analysis and debugging
- Logging

## AWS Elastic Beanstalk Deployments

### Languages Supported

- Java
- .NET
- PHP
- Node.js
- Python
- Ruby
- Go
- Docker

### Uploading your code

- Elastic Beanstalk automatically handles the deployment
- Deploys on servers such as Apache, NGINX. Passenger and more

## Benefits

- Fast and simple to start using
- Developer productivity
- Difficult to outgrow
- Complete resource control