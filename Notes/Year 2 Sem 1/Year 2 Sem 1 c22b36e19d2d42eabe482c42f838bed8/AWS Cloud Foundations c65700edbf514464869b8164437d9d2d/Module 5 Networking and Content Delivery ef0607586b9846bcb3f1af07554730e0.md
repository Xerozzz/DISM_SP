# Module 5: Networking and Content Delivery

# Part 1: Networking Basics

---

# Part 2: Amazon VPC

## Definition

- Enables you to provision a logically isolated section of the AWS cloud where you can launch resources in a virtual network you define

## Features

- Gives you control over virtual networking resources like IP address ranges, creation of subnets and configuration of route tables and network gateways
- Enables you to customize the network configuration for your VPC
- Enables you to use multiple layers of security

## Terms

### VPCs

- Logically isolated from other VPCs
- Dedicated to your AWS account
- Belong to a single AWS region and can span multiple AZs

### Subnets

- Range of IP addresses that divide a VPC
- Belong to a single AZ
- Can be public or private

## IP Addressing

- When creating VPCs, you assign an IPv4 CIDR block to it
- The largest is /16
- Smallest is /28
- IPv6 is also supported
- CIDR Blocks of subnets cannot overlap

### Reserved IPs

- 10.0.0.0 for network address
- 10.0.0.1 for internal communication
- 10.0.0.2 for DNS Resolution
- 10.0.0.3 for future use
- 10.0.0.255 network broadcast address

### IP address Types

- Public IPv4 Address
    - Manually assigned through an elastic IP address
    - Automatically Assigned through the auto-assign public IP address settings at a subnet level
- Elastic IP address
    - Associated with AWS account
    - Can be allocated and remapped anytime
    - Additional costs may apply

## Elastic Network Interface

- A virtual network interface that can be attached to an instance
- Its attributes follow when it is reattached to another instance
- Each instance in the VPC has a default network interface that is assigned a private IPv4 address from the IPv4 address range of your VPC

## Route Tables and Routes

- Route tables contain sets of rules that you can configure to direct network traffic from your subnet
- Each route specifies a destination and a target
- By default, each table contains a local route for communication within the VPC
- Each subnet must be associated with 1 and only 1 route table

---

# Part 3: VPC Networking

## VPC Peering

- Can connect VPCs in your own AWS account, between accounts or regions

### Restrictions

- IP Spaces cannot overlap
- Transitive peering is not supported
- You can only have one peering resource between the same two VPCs

## VPC Gateway

- Used to connect your VPC to your local network or data center

## Internet Gateway

- Used to access the internet
- Used to create a NAT Gateway

### NAT Gateway

- Allows private subnet instances from accessing the internet
- Public cannot access private

## AWS Direct Connect

- Establish dedicated private connection to improve bandwidth and throughput

## VPC Endpoints

### Gateway Endpoint

- Amazon S3
- Amazon DynamoDB

### Interface Endpoints

- AWS PrivateLink

---

# Part 4: VPC Security

## Security Group

- Controls outbound and inbound traffic like a firewall
- Works on an instance level, network interface card
- Default security groups are sealed shut to inbound traffic
- Security groups are stateful, outbound traffic is always allowed

## Network ACLs

- Works at a subnet level
- A network ACL has separate inbound and outbound rules, and each rule can allow or deny traffic
- Default network ACLs allow all inbound and outbound IPv4 traffic
- Network ACLs are stateless

---

# Part 5: Amazon Route 53

## Definition

- Is a highly available and scalable DNS web service that allows you to register domain names
- Used to route end users to internet apps by translating domain names into IP Addresses

## Features

- Fully compliant with IPv4 and IPv6
- Connects user requests to infrastructure running in AWS and out of AWS
- Used to check health of your resources
- Features traffic flow

## Supported Routing

### Simple Routing

- Use in single-server environments

### Weighted Routing

- Assign weights to resource record sets to specify the frequency

### Latency Routing

- Help improve your global applications

### Geolocation Routing

- Route traffic based on location of your users

### Geoproximity Routing

- Route traffic based on location of your resources

### Failover Routing

- Fail over to a backup site if primary site is unreachable

### Multi-value Answer Routing

- Respond to DNS queries with up to eight healthy records selected at random

## Route 53 DNS Failover

- Improve availability of your applications run on AWS
- Configure backup and failover scenarios for your apps
- Enable highly available multi-region architecture on AWS
- Creating health checks

---

# Part 6: Amazon CloudFront

## Definition

- Fast, global and secure CDN Service
- Global network of edge locations and regional edge caches
- Self service model with pay as you go pricin

## Infrastructure

### Edge Location

- Network of data centers that CloudFront uses to serve popular content quickly to customers

### Regional Edge Cache

- CloudFront location that caches content that is not popular enough for Edge Location
- Located in between origin server and global edge location