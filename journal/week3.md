# Week 3 — Decentralized Authentication

## Required Homework/Tasks

## What is Decentralized Authentication?
A form of authentication known as decentralized authentication verifies user identities without the aid of a central authority or server. Instead, it makes use of a distributed computer network, frequently based on blockchain technology, to peer-to-peer verify user identities.

Users of a decentralized authentication system are in charge of maintaining their own digital identities, which are stored on the blockchain network. The network requests identification documentation, such as a digital signature, when a user wants to authenticate themselves. The user's identity is then confirmed by the network using a consensus mechanism, such as a proof-of-work or proof-of-stake algorithm.

Compared to conventional centralized authentication techniques, decentralized authentication has a number of benefits. Since there is no single point of failure or attack, it is more secure, which is one of its main advantages. As there is no central authority that can block or restrict access to specific users, it is also more resistant to censorship. Decentralized authentication is also more privacy-friendly because users can decide to remain anonymous and have more control over their personal data.


## What is AWS Cognito?
Amazon Web Services (AWS) offers the managed authentication, authorization, and user management service known as AWS Cognito. It's made to make it simple for programmers to include user sign-up, sign-in, and access control in their web and mobile applications.

Numerous identity providers are supported by AWS Cognito, including business identity providers like Microsoft Active Directory as well as social identity providers like Google, Facebook, and Amazon. Developers can now give their users a selection of login options and integrate with existing identity systems thanks to this.

## What is AWS Amplify?
AWS Amplify is a set of tools and services provided by Amazon Web Services (AWS) to help developers build scalable and secure cloud-powered applications. It provides a streamlined development workflow and a set of pre-built UI components that can be used to build web and mobile applications quickly and easily.

To install AWS Amplify

```sh
npm i aws-amplify --save
```

To create a minimally configured user pool

This example creates a user pool named cruddur-user-pool using default values. There are no required attributes and no application clients. MFA and advanced security is disabled.

Command:

```
aws cognito-idp create-user-pool --pool-name cruddur-user-pool
```

Creat Cognito User Group
![week-3-userpool-1](https://user-images.githubusercontent.com/88502375/223562410-8d18c4e1-ad53-4206-b74a-49de0c339ca8.jpg)

![week-3-userpool-2](https://user-images.githubusercontent.com/88502375/223562813-f167dceb-d38d-4261-877e-1a1a45fb9031.jpg)

![week-3-code-1](https://user-images.githubusercontent.com/88502375/224171082-dbbaf0cc-058d-4135-a129-ebf3a802c02f.jpg)

![week-3-confirmatio-1](https://user-images.githubusercontent.com/88502375/224171084-f96bfc60-1a5d-420b-b7a6-8778b01d2b5c.jpg)

![week-3-signin-1](https://user-images.githubusercontent.com/88502375/224171086-2438f97c-9ec2-4a41-ad79-367b1d9c065e.jpg)



#### How to add a user in user pool?
1. Create a user
2. Navigate to the Amazon Cognito console , and choose User Pools.
3. Choose an existing user pool from the list, or create a user pool.
4. Choose the Users tab, and choose Create a user.


#### Create and Configure a Cognito User Pool from the AWS CLI

##### First install aws cli using following command
```
sudo pip install awscli
```

##### Configure AWS credentials, Run below commonond, system will ask following input AWS Access Key ID, AWS Secret Access Key, Default region name, Default output format
```
sudo aws configure
```

##### Create user pool
```
sudo aws cognito-idp create-user-pool --pool-name cruddur-user-pool
```

#### Steps to Create Cognito User in AWS

1. Create New User: First of all, add a new user in AWS Cognito with aws cognito-idp sign-up command line.

```sh
aws cognito-idp sign-up \
    --client-id 71tm9vt159vgckt8kml11up8cn \
    --username ajmalteq@gmail.com \
    --password Pa55w0rd! \
    --user-attributes Name="email",Value="ajmalteq@gmail.com" Name="name",Value="Ajmal" \
    --region us-east-1 \
    --profile default 
```

2. Confirm User as Admin: The confirm the newly added user with the below command.

```sh
aws cognito-idp admin-confirm-sign-up \
    --user-pool-id us-east-1_f8oSH5YI0 \
    --username ajmalteq@gmail.com \
    --region  us-east-1 \
    --profile geoff 
```


3. Verify Email Address: Finally, verify the email address of the newly added user with the below command.

```sh
aws cognito-idp admin-update-user-attributes \
    --user-pool-id us-east-1_f8oSH5YI0 \
    --username ajmalteq@gmail.com \
    --user-attributes Name=email_verified,Value=true \
    --region us-east-1 \
    --profile geoff 
```

4. A new user has been created in User Pool with the “CONFIRMED” status. You can visit the AWS Cognito service and check for the user


## User Lifecycle Management
User lifecycle management refers to the process of managing the various stages of a user's interaction with a system or service, from initial registration to account deletion. It involves creating, updating, and deleting user accounts and managing their access and permissions throughout their lifecycle.

The user lifecycle typically consists of the following stages:

1. Registration: This is the initial stage where a user creates an account and provides their personal information.

2. Verification: After registration, the user's identity is verified using various methods such as email or phone verification.

3. Access: Once the user's identity is verified, they are granted access to the system or service.

4. Permissions: Users may have different levels of access and permissions based on their role or the tasks they need to perform.

5. Updates: Over time, users may need to update their personal information or change their access and permissions.

6. Deactivation: If a user is no longer using the system or service, their account may be deactivated.

7. Deletion: When a user no longer needs their account, it may be deleted from the system or service.

Effective user lifecycle management involves implementing policies and procedures to ensure that user accounts are created and managed securely, and that access and permissions are granted and revoked as needed. It also involves monitoring user activity to identify and respond to security risks and other issues that may arise throughout the user lifecycle.



## Token lifecycle management
Token lifecycle management refers to the process of managing the various stages of a security token's lifespan, from creation to expiration or revocation. Tokens are used in various security protocols to authenticate users and grant them access to resources or services.

The lifecycle of a token typically consists of the following stages:

Generation: Tokens are generated by a trusted authority or authentication server, using a secure algorithm and key.

Issuance: Once a token is generated, it is issued to the user along with instructions for how to use it.

Validation: When a user presents a token, it is validated by the resource or service being accessed, to ensure that it is valid and has not been tampered with.

Access: If the token is validated successfully, the user is granted access to the requested resource or service.

Refresh: Tokens may have a limited lifespan, after which they must be refreshed or renewed to continue providing access.

Revocation: Tokens may be revoked if they are compromised, if the user's access privileges change, or if the token has expired.

Effective token lifecycle management involves implementing policies and procedures to ensure that tokens are generated and issued securely, and that they are validated and refreshed or revoked as needed. It also involves monitoring token usage to identify and respond to security risks and other issues that may arise throughout the token lifecycle.


### Amazon Cognito Security Best Practices
Amazon Cognito is a managed service that provides user authentication and authorization features to web and mobile applications. To ensure the security of your applications, it's important to follow some best practices when using Amazon Cognito. Here are some key security best practices for Amazon Cognito:

1. Use strong passwords and multifactor authentication (MFA): Encourage your users to use strong passwords and enable MFA to add an extra layer of security to their accounts.

2. Use HTTPS: Always use HTTPS when communicating with Amazon Cognito endpoints to encrypt data in transit.

3. Use SSL/TLS certificates: Use SSL/TLS certificates to encrypt data at rest and to ensure the integrity of communications between your application and Amazon Cognito.

4. Use IAM roles and policies: Use IAM roles and policies to control access to Amazon Cognito resources, such as user pools and identity pools.

5. Limit access: Limit access to your Amazon Cognito resources by configuring appropriate security groups and network access control lists (ACLs).

6. Monitor and log: Monitor and log Amazon Cognito API calls and events to detect suspicious activity and potential security breaches.

7. Follow Amazon Cognito security guidelines: Follow Amazon Cognito security guidelines, which include best practices for data protection, identity verification, and secure application design.

8. Keep your Amazon Cognito SDKs up to date: Always use the latest version of Amazon Cognito SDKs and keep them up to date to ensure that your application is using the latest security features and bug fixes.


## Required Homework Challenges
1. Implemented MFA which sends SMS (text message)

![week-3-mfa-1](https://user-images.githubusercontent.com/88502375/224497398-97c6b35c-a03a-4ea4-8be3-f21fd9739304.jpg)

