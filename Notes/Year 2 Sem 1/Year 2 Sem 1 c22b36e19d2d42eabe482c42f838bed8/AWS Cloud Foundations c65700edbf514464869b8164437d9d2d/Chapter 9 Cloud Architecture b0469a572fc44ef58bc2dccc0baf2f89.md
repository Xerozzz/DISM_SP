# Chapter 9: Cloud Architecture

# Part 1: AWS Well-Architected Framework

## Architecture: Designing and Building

- Engage with decision makers to identify the business goal and the capabilities that need improvement
- Ensure alignment between technology deliverables of a solution and the business goals
- Work with delivery teams that are implementing the solution to ensure that the technology features are appropriate

## What is the AWS Well-Architected Framework?

- A guide for designing infrastructures that are secure, high-performing, resilient and efficient
- A consistent approach to evaluating and implementing cloud architectures
- A way to provide best practices that were developed through lessons learned by reviewing customer architectures

## Pillars of the AWS Well-Architected Framework

- Operational Excellence
- Security
- Reliability
- Performance Efficiency
- Cost Optimization

## Operational Excellence Pillar

- Run and monitor systems to deliver business value, and to continually improve supporting processes and procedures

### Key Topics

- Managing and automating changes
- Responding to events
- Defining standards to successfully manage daily operations

### Design Principles

- Perform operations as code
- Annotate documentation
- Make frequent, small, reversible changes
- Refine operations procedures frequently
- Anticipate failure
- Learn from all operational events and failures

### Questions (Just Read)

- How do you determine what your priorities are?
- How do you design your workload so that you can understand its state?
- How do you reduce defects, ease remediation and improve flow into productions?
- How do you mitigate deployment risks
- How do you know that you are ready to support a workload?
- How do you understand the health of your workload?
- How do you understand the health of your operations?
- How do you manage workload and operations events?
- How do you evolve operations?

## Security Pillar

- Protect information, systems and assets while delivering business value through risk assessments and risk mitigation strategies

### Key Topics

- Identifying and managing who can do what
- Establishing controls to detect security events
- Protecting systems and services
- Protecting confidentiality and integrity of data

### Design Principles

- Implement a strong identity foundation
- Enable traceability
- Apply security at all layers
- Automate security best practices
- Protect data in transit and at rest
- Keep people away from data
- Prepare for security events

### Security Questions (Just Read)

- How do you manage credentials and authentication?
- How do you control human access?
- How do you control programmatic access?
- How do you detect and investigate security events?
- How do you defend against emerging security threats
- How do you protect your networks?
- How do you protect your compute resources?
- How do you classify your data?
- How do you protect data at rest and in transit?
- How do you respond to an incident

## Reliability Pillar

- Prevent and quickly recover from failures to meet business and customer demand

### Key Topics

- Setting up
- Cross-project requirements
- Recovery planning
- Handling charge

### Design Principles

- Test recovery procedures
- Automatically recover from failures
- Scale horizontally to increase aggregate system availability
- Stop guessing capacity
- Manage change in automation

### Questions (Just Read)

- How do you manage service limits and network topology?
- How does your system adapt to changes on demand?
- How do you monitor your resources and implement change?
- How do you back up data?
- How does your system withstand component failure?
- How do you test resilience and plan for disaster recovery?

## Performance Efficiency Pillar

- Use IT and computing resources efficiently to meet system requirements and to maintain that efficiently as demand changes and technologies evolve

### Key Topics

- Selecting the right resource types and sizes based on workload requirements
- Monitoring performance and making informed decisions to maintain efficiency as business needs evolve

### Design Principles

- Democratize advanced technologies
- Go global in minutes
- Use serverless architecture
- Experiment more often
- Have mechanical sympathy

### Questions (Just Read)

- How do you select the best performing architecture?
- How do you select your compute, storage, database and networking solution?
- How do you evolve your workload to take advantage of new releases?
- How do you monitor your resources to ensure they are performing as expected?
- How do you use tradeoffs to improve performance?

## Cost Optimization Pillar

- Run systems to deliver business value at the lowest price point

### Key Topics

- Understanding and controlling when money is being spent
- Selecting the most appropriate and right number of resource types
- Analyzing spending over time
- Scaling to meeting business needs without overspending

### Design Principle

- Adopt a consumption model
- Measure overall efficiency
- Stop spending money on data center operations
- Analyze and attribute expenditure
- Use managed and application-level services to reduce cost of ownership

### Questions (Just Read)

- How do you govern usage and monitor usage and cost?
- How do you decommission resources?
- How do you evaluate cost when you select services?
- How do you meet cost targets when you select resource types and size?
- How do you use pricing models to reduce costs?
- How do you plan for data transfer changes?
- How do you match supply of resources with demand?
- How do you evaluate new services?

## AWS Well-Architected Tool

- Helps you review the state of your workloads and compares them to the latest AWS architectural best practices
- Gives you access to knowledge and best practices used by AWS architects, whenever you need it
- Delivers an action plan with step-by-step guidance on how to build better workloads for the cloud
- Provides a consistent process for you to review and measure your cloud architectures

# Part 2: Reliability and Availability

## Reliability

- A measure of your system's ability to provide functionality when desired by the user
- System includes all system components, hardware, firmware and software
- Probability that your entire system will function as intended for a specified period
- Mean Time Between Failures = Total Time in Service/Number of Failures

### Understanding Reliability Metrics

![Chapter%209%20Cloud%20Architecture%20b0469a572fc44ef58bc2dccc0baf2f89/Annotation_2020-07-07_153008.png](Chapter%209%20Cloud%20Architecture%20b0469a572fc44ef58bc2dccc0baf2f89/Annotation_2020-07-07_153008.png)

## Availability

- Normal operation time/total time
- Percentage of uptime over time, for example 99.9% for 1 year

## High Availability

- System can withstand some measure of degradation while still remaining available
- Downtime is minimized
- Minimal human intervention is required

### Availability Tiers (Just Read)

![Chapter%209%20Cloud%20Architecture%20b0469a572fc44ef58bc2dccc0baf2f89/Annotation_2020-07-07_153251.png](Chapter%209%20Cloud%20Architecture%20b0469a572fc44ef58bc2dccc0baf2f89/Annotation_2020-07-07_153251.png)

### 3 Factors That Affect Availability

- Fault tolerance, the built-in redundancy of an application's components and its ability to remain operational
- Scalability, the ability of an application to accommodate increases in capacity needs without changing design
- Recoverability, the process, policies and procedures that are related to restoring service after catastrophic event

### Trade-off

- You can design your workloads and applications to be highly available, but usually means increased costs

# Part 3: AWS Trusted Advisor

## Definition

- Online tool that provides real-time guidance to help you provision your resources following AWS best practices
- Looks at your entire AWS environment and gives you real-time recommendations in five categories

    ![Chapter%209%20Cloud%20Architecture%20b0469a572fc44ef58bc2dccc0baf2f89/Annotation_2020-07-07_153633.png](Chapter%209%20Cloud%20Architecture%20b0469a572fc44ef58bc2dccc0baf2f89/Annotation_2020-07-07_153633.png)

## Categories

### Cost Optimization

- AWS Trusted Advisor looks at your resource use and makes recommendation to help you optimize cost by eliminating unused and idle resources, or by making commitments to reserved capacity

### Performance

- Improve the performance of your service by checking your service limits, ensuring that you take advantage of provisioned throughput and monitoring for overutilized instances

### Security

- Improve the security of your application by closing gaps, enabling various AWS security features, and examining your permissions

### Fault Tolerance

- Increase the availability and redundancy of your AWS application by taking advantage of automatic scaling, health checks, Multi-AZ deployments and backup capabilities

### Service Limits

- AWS Trusted Advisor checks for service usage that is more than 80% of the service limit
- Values are based on a snapshot, so your current usage might differ
- Limit and usage data can take up to 24 hours to reflect changes