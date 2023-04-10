# Week 7 — Solving CORS with a Load Balancer and Custom Domain

## Required Homework/Tasks


#### What is AWS Route 53
AWS Route 53 lets developers and organizations route end users to their web applications in a very reliable and cost-effective manner. It is a Domain Name System (DNS) that translates domain names into IP addresses to direct traffic to your website.

The name for our service (Route 53) comes from the fact that DNS servers respond to queries on port 53 and provide answers that route end users to your applications on the Internet.

#### What is AWS ACM?
AWS Certificate Manager (ACM) is a service that lets you easily provision, manage, and deploy public and private Secure Sockets Layer/Transport Layer Security (SSL/TLS) certificates for use with AWS services and your internal connected resources.

#### Route53 hosted zone created
![week-7-route53-hosted-zones-1](https://user-images.githubusercontent.com/88502375/230876672-6e6687ba-3363-4a62-9e11-5223c494ffac.jpg)

#### domain name is cloudproject.uk
![week-7-route53-hosted-zones-2](https://user-images.githubusercontent.com/88502375/230876691-1f2e6840-5c81-405a-b1c6-c12d9c6efafc.jpg)

#### AWS Certificate Manager
![week-7-aws-acm-3](https://user-images.githubusercontent.com/88502375/230876713-d67db522-81b7-46ca-8086-186f1fa8f33c.jpg)

#### ACM is created
![week-7-aws-acm-4](https://user-images.githubusercontent.com/88502375/230876719-5d8614e1-cce2-4030-b2fb-a7ad8a71d580.jpg)

#### Application Load Balancer
![week-7-alb-5](https://user-images.githubusercontent.com/88502375/230879530-41a5b985-5f7d-4008-8d74-7ba6b9b2d7e5.jpg)

#### ALB
![week-7-alb-6](https://user-images.githubusercontent.com/88502375/230879549-2f484cac-d022-4b6c-af07-dafa22c0224e.jpg)

### Listeners
A listener checks for connection requests on its port and protocol. Traffic received by the listener is routed according to its rules.

#### Listener Rules
![week-7-443-listner rules-7](https://user-images.githubusercontent.com/88502375/230879596-cf95d51e-4050-4bc7-8903-89b8252e0473.jpg)

#### Target Groups
![week-7-target-groups-8](https://user-images.githubusercontent.com/88502375/230879631-e678768f-9020-4bbc-9eb4-60a8c66b8ed6.jpg)

#### cruddur-frontend-react-js target group status
![week-7-ec2-target-groups-cruddur-frontend-react-js-9](https://user-images.githubusercontent.com/88502375/230879664-431082f4-a815-4f7b-bc7b-1e86a543ba8d.jpg)


#### cruddur-backend-flask-tg target group status
![week-7-ec2-target-groups-cruddur-backend-flask-tg-10](https://user-images.githubusercontent.com/88502375/230879679-abcaf77c-574a-4f7c-ae12-79e97ef95802.jpg)

