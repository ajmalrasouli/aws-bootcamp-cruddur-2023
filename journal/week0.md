# Week 0 — Billing and Architecture

## Accounts
-------------------------

1. Registered an account with the following online cloud services:

| Account                           | Status |
| :---------------------------------| :----: |
| GitHub Account                    |   ✅   |
| Gitpod Account                    |   ✅   |
| Github Codespaces Account         |   ✅   |
| AWS Account                       |   ✅   |
| Momento Account                   |   ✅   |
| Custom Domain Name                |   ✅   |
| Lucid Charts                      |   ✅   |
| HoneyComb.io                      |   ✅   |
| Rollbar Account                   |   ✅   |


On AWS created a group called Admin and assigned Administrative role to this group, Also a new user created and dropped this new user into the admin group.
Created MFA for root and new user. But, only created Access Key for the new user.

![image](https://user-images.githubusercontent.com/88502375/219152913-619663a3-e40b-4ad0-9381-2d969a1274a3.png)



Installed AWS CLI on GitPod and windows OS.
```bash
tasks:
  - name: aws-cli
    env:
      AWS_CLI_AUTO_PROMPT: on-partial
    init: |
      cd /workspace
      curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
      unzip awscliv2.zip
      sudo ./aws/install
      cd $THEIA_WORKSPACE_ROOT
```
 

#### aws --cli-auto-prompt
#### aws sts get-caller-identity

[cloudshell-user@ip-10-6-121-215 ~]$ aws --cli-auto-prompt
> aws sts get-caller-identity
```
{
    "UserId": "AIDA3FGHHGFFGHGBJFWVN",
    "Account": "8065767565521",
    "Arn": "arn:aws:iam::8065767565521:user/ajmal"
```
## Launching AWS CloudShell and looking at AWS CLI

![image](https://user-images.githubusercontent.com/88502375/219484865-cb4088a1-3cb3-4dbe-926c-dfd7860de768.png)


#### visit site for more cli commands: Command Line Interface - AWS CLI
docs.aws.amazon.com/cli/latest/reference or for version 2
https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html

[cloudshell-user@ip-10-6-121-215 ~]$ aws account get-contact-information 
```
{
    "ContactInformation": {
        "AddressLine1": "11 Trace Court",
        "City": "Birmingham",
        "CountryCode": "GB",
        "FullName": "Ajmal Rasouli",
        "PhoneNumber": "+44 07517694097",
        "PostalCode": "UJ9 8BM",
        "StateOrRegion": "UK"
    }
}
```

## Install AWS CLI

on Windows
I installed the AWS CLI for Windows 10 via command in **Command Prompt**:

I followed the instructions on the [AWS CLI Install Documentation Page](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)

#### PS C:\Windows\system32> msiexec.exe /i https://awscli.amazonaws.com/AWSCLIV2-2.0.30.msi
#### PS C:\Windows\system32> aws --version
#### aws-cli/2.9.22 Python/3.9.11 Windows/10 exe/AMD64 prompt/off

on Linux

#### curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
```
   1  ls
   2  unzip awscliv2.zip
   3  clear
   4  ls
   5  sudo ./aws/install 
   6  ls
   7  clear
   8  cd $THEIA_WORKSPACE_ROOT
   9  ls
   10  history
```

#### gitpod /workspace/aws-bootcamp-cruddur-2023 (main) $ 


### environment variables

echo $PATH

#### gitpod /workspace/aws-bootcamp-cruddur-2023 (main) $ echo $PATH

/home/gitpod/.sdkman/candidates/maven/current/bin:/home/gitpod/.sdkman/candidates/java/current/bin:/home/gitpod/.sdkman/candidates/gradle/current/bin:/workspace/.cargo/bin:/home/gitpod/.rvm/gems/ruby-3.1.2/bin:/home/gitpod/.rvm/gems/ruby-3.1.2@global/bin:/home/gitpod/.rvm/rubies/ruby-3.1.2/bin:/home/gitpod/.pyenv/shims:/workspace/go/bin:/home/gitpod/.nix-profile/bin:/ide/bin/remote-cli:/home/gitpod/go/bin:/home/gitpod/go-packages/bin:/home/gitpod/.nvm/versions/node/v16.19.0/bin:/home/gitpod/.yarn/bin:/home/gitpod/.pnpm:/home/gitpod/.pyenv/bin:/workspace/.rvm/bin:/home/gitpod/.cargo/bin:/home/linuxbrew/.linuxbrew/bin:/home/linuxbrew/.linuxbrew/sbin/:/home/gitpod/.local/bin:/usr/games:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/home/



#### gitpod /workspace/aws-bootcamp-cruddur-2023 (main) $ env
```
PYENV_HOOK_PATH=/home/gitpod/.gp_pyenv.d
PIPENV_VENV_IN_PROJECT=true
GP_PREVIEW_BROWSER=/ide/bin/remote-cli/gitpod-code --preview
PYENV_SHELL=bash
rvm_prefix=/home/gitpod
SUPERVISOR_ADDR=localhost:22999
```

To store environment variables in GitPod.
```
gp env AWS_ACCESS_KEY_ID=AKIAJHDFGFHGDDFGXTDV
gp env AWS_SECRET_ACCESS_KEY=74545345435yGSHF3H8/iwfLA4YCX/Udzn1bVz
gp env AWS_DEFAULT_REGION=us-east-1
```


## AWS Budgets, AWS Cost Explorer, Billing Alarms

AWS Budgets is the simplest way to monitor your AWS spend and be alerted when you exceed or are forecasted to exceed your desired spending limit.

I have set my Billing alarm to $5.00.


![week 0 AWS Budget](https://user-images.githubusercontent.com/88502375/219490959-5eaf5493-910d-438d-a2c4-59bd7c305749.jpg)

![image](https://user-images.githubusercontent.com/88502375/219152725-74e24cc5-e130-4721-b719-267f76db377d.png)

### The AWS Well-Architected Tool
The AWS Well-Architected Tool is designed to help us review the state of our applications and workloads against architectural best practices, identify opportunities for improvement, and track progress over time.

![image](https://user-images.githubusercontent.com/88502375/219160553-36ac068a-acb9-4a16-a253-cc9d031cf96c.png)

![image](https://user-images.githubusercontent.com/88502375/219160778-981545fb-71b3-4d1c-95f7-4f14eeceb1a7.png)

### Cruddur Conceptual Diagram using Lucid
https://lucid.app/lucidchart/18f1cd83-e869-494e-9a3b-55c956e6f8c6/edit?invitationId=inv_1211e7d2-aeb6-4d38-b083-aa9e400d35dc

![image](https://user-images.githubusercontent.com/88502375/219166184-bf55ea4a-5d7f-43be-9323-0c4c5a0eac4d.png)


### Cruddur Conceptual Napkin Diagram

![Napkin Diagram](assets/week%200%20Cruddur%20Conceptual%20Napkin%20Diagram.jpg)


### Cruddur Logical Diagram
https://lucid.app/lucidchart/d9649fda-e579-4971-a256-e3ddf6fdb17e/edit?viewport_loc=-780%2C-2622%2C3328%2C1548%2C0_0&invitationId=inv_2884eefe-6857-41b6-8ee1-2999303ddbd5

![week 0 Cruddur Logical Diagram](https://user-images.githubusercontent.com/88502375/219493282-5213350c-68a3-4d49-8b3c-cef05406795e.jpeg)


