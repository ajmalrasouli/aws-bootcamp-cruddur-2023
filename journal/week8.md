# Week 8 — Serverless Image Processing

## Required Homework/Tasks

### An Introduction To AWS Cloud Development Kit (CDK)

You have two options when starting to develop a cloud-based back-end system for your application: either manually using a graphical user interface (GUI) or command-line interface (CLI), or programmatically. You may simply manage your application using the GUI console if it only makes use of a small number of cloud resources. The underlying infrastructure will expand along with the complexity of your system, making manual management of it impossible. Additionally, it is vulnerable to user error; even a minor mistake could negatively impact the system. No matter if you are an independent developer using a modest number of cloud resources or a large corporation, managing your infrastructure programmatically is a far superior solution.


AWS CloudFormation templates or AWS CDK can be used to manage AWS infrastructure programmatically. In order to launch and configure the desired resources as a stack, AWS CloudFormation templates provide a YAML- or JSON-based configuration file that lists the desired resources and their dependencies. Utilising Google Cloud's Deployment Manager to manage your infrastructure is advised. The Google Cloud Deployment Manager templates are YAML templates that may be used to define your resources, much as AWS CloudFormation.

To deploy and manage Azure services, Microsoft Azure provides Azure Resource Manager (ARM) templates. Resources and their relationships can be defined using ARM templates, which are JSON templates. Additionally, you may manage your infrastructure with Terraform, an open-source IaC tool that supports hundreds of cloud providers like AWS, Google Cloud, and Microsoft Azure. Terraform configurations are kept up to date in.tf files and are built using the syntax of the HashiCorp configuration language.


## Introduction To AWS CDK

Utilising the programming language of your choice, you may model and provide AWS cloud resources using the open-source WS CDK framework. It allows you to represent the architecture of an application in TypeScript, Python, Java, or.NET. Behind the scenes, it makes use of AWS CloudFormation to reliably and securely provide resources.

The workflow for infrastructure management using AWS CDK is depicted in the diagram below.

![image](https://user-images.githubusercontent.com/88502375/234672996-77ad96fc-fffc-41f9-b3e7-b2ceb6bbfd85.png)


### CDK Constructs
AWS CDK constructs are cloud components that provide configuration information and glue logic for one or more AWS services. The majority of the frequently used AWS services and capabilities are covered by the library of constructs offered by CDK. 

AWS CDK supports TypeScript, JavaScript, Python, Java, C# and .NET.

#### S3 Bucket Construct 

```py
import * as s3 from "@aws-cdk/aws-s3";
import * as iam from "@aws-cdk/aws-iam";

const bucket = new s3.Bucket(this, "CdkPlayBucket");
const result = bucket.addToResourcePolicy(
  new iam.PolicyStatement({
    actions: ["s3:GetObject"],
    resources: ["*"],
    principals: [new iam.AccountRootPrincipal()],
  })
);
```

### CDK STACKS
In the AWS CDK, a stack is the smallest deployable unit. The resources defined in a stack are all provisioned together. Similar constraints apply to CDK stacks as they do to AWS CloudFormation. Your AWS CDK app allows you to define an unlimited number of stacks. A sample stack's scaffolding is displayed in the code excerpt below:

```py
import * as cdk from "@aws-cdk/core";
export class CdkPlayStack extends cdk.Stack {
  constructor(scope: cdk.App, id: string, props?: cdk.StackProps) {
    super(scope, id, props);
    // resources
  }
}
```

### Using The CDK Toolkit 

AWS provides a CLI tool, which is the primary way to interact with your AWS CDK application. It builds, synthesizes, and deploys the resources defined in your CDK application.

### The standard AWS CDK development workflow

- The AWS CDK template can be used to create the app.

- Create resources within stacks by adding code to the application.

- Build the app. (If you forget, the AWS CDK Toolkit performs this action for you.)

- Synthesize one or more stacks in the app to create an AWS CloudFormation template.

- Deploy one or more stacks to your AWS account.


### Create The App
The cdk init command can be used to initialize a new application in the language of your choice. Each CDK app maintains its own set of module dependencies and should be created in its own directory. For example, we can create a TypeScript CDK application with the cruddur-app template by using the following command:

```py
cdk init cruddur-app --language=typescript
```

The $\color{color-blue}{cdk-init}$ command also initializes the project as a Git repository, along with the $\color{color-blue}{.gitignore}$ file. Apart from that, it generates a $\color{color-blue}{package.json}$ file for managing project dependencies and a $\color{color-blue}{tsconfig.json}$ file for TypeScript configuration.

Once you have initialized the project, you can run the $\color{color-blue}{build}$ command to manually compile the app. This step isn’t mandatory, because the $\color{color-blue}{cdk}$ toolkit does it for you before you deploy the changes, but a manual build can sometimes help in catching syntax errors. Here’s how it can be done:

```py
npm run build
```

We can verify that the project was initialized with a single stack by executing the following command:

```py
cdk ls
```
The ls command should return the name of our app’s directory as the name of the stack.


### Synthesize an aws cloudformation template

Once the project has been set up, you may use the build command to manually compile the application. The cdk toolkit performs this step for you before to deploying the modifications, so it is not required, although a manual build might occasionally be useful in identifying syntax mistakes. Here is how to accomplish it:

```py
cdk synth
```

This produces a cdk.out file with a YAML-formatted template and converts the resources defined in the stack to the corresponding AWS CloudFormation template. Below is a representation of where the YAML output starts:

```yml
Resources:
  MyFirstBucketB8884501:
    Type: AWS::S3::Bucket
    Properties:
      VersioningConfiguration:
        Status: Enabled
    UpdateReplacePolicy: Retain
    DeletionPolicy: Retain
    Metadata:...
```

### Deploy the Stack

Make sure the AWS CLI is installed and your AWS credentials are set up on your device before attempting to deploy the stack. 

```py
cdk deploy
```

### Screenshots of implementation

![week-8-Install-CDK-globally-1](https://user-images.githubusercontent.com/88502375/234807326-f0742c7c-172c-480e-983d-d64307b97138.jpg)


![week-8-CDK-synth-2](https://user-images.githubusercontent.com/88502375/234807362-c1a3c104-5a08-4a6f-b890-4bf79124601a.jpg)



![week-8-CDK-synth-3](https://user-images.githubusercontent.com/88502375/234807385-8681c2d4-ff84-4ede-98a0-8dca4df1cbc2.jpg)


![week-8-CDK-CloudFormation-4](https://user-images.githubusercontent.com/88502375/234807401-7704c8cb-2b02-4342-b8a3-b3291bfec207.jpg)


![week-8-CDKToolKit-5](https://user-images.githubusercontent.com/88502375/234807419-58085044-32fd-411a-864c-9cb3700d1281.jpg)


![week-8-CDK-Deploy-6](https://user-images.githubusercontent.com/88502375/234807438-3c1e1b68-4114-4608-9193-e183a20e173c.jpg)


![week-8-cdk-bootstrap-7](https://user-images.githubusercontent.com/88502375/234807460-e05e3a1a-f779-4fcc-91de-c813366da409.jpg)


![week-8-CDK-deploy - 1](https://user-images.githubusercontent.com/88502375/235297148-0486b183-e293-45f8-bc7f-a776b0f0f98b.jpg)



![week-8-CDK-deploy - 2](https://user-images.githubusercontent.com/88502375/235297153-f9b60926-a081-40e7-aa77-16aa5b4191c5.jpg)


![week-8-CDK-S3-bucket-3](https://user-images.githubusercontent.com/88502375/235297157-26d29e7e-6909-43e8-b28c-42e12805b79a.jpg)


![week-8-CDK-S3-bucket-4](https://user-images.githubusercontent.com/88502375/235297159-a478083f-ce5e-4123-a42e-009ebe8ef71b.jpg)



![week-8-CloudFront-5](https://user-images.githubusercontent.com/88502375/235297161-291537a7-3596-4918-9f42-c61d6e967f62.jpg)


![week-8-s3-bucket-policy-6](https://user-images.githubusercontent.com/88502375/235297165-c79f677b-4c1a-4c69-b7a0-a8ee0b56f11f.jpg)


![week-8-s3-bucket-7](https://user-images.githubusercontent.com/88502375/235297171-f72e0223-c1f2-4155-9332-52d1025451ff.jpg)


***We must allow access to CloudFront using this policy statement.***

```yml


{
        "Version": "2008-10-17",
        "Id": "PolicyForCloudFrontPrivateContent",
        "Statement": [
            {
                "Sid": "AllowCloudFrontServicePrincipal",
                "Effect": "Allow",
                "Principal": {
                    "Service": "cloudfront.amazonaws.com"
                },
                "Action": "s3:GetObject",
                "Resource": "arn:aws:s3:::assets.cloudproject.uk/*",
                "Condition": {
                    "StringEquals": {
                      "AWS:SourceArn": "arn:aws:cloudfront::804789588521:distribution/EQDLN0KTHJK88"
                    }
                }
            }
        ]
      }
```

![week-8-cruddurAvatarUpload_Lamba-8](https://user-images.githubusercontent.com/88502375/235314228-9e76f715-4441-4a70-a1a2-9341baa99b07.jpg)


![week-8-cruddurAvatarUpload_Lamba-test-9](https://user-images.githubusercontent.com/88502375/235314234-37146e57-5461-4fe3-beb8-8b3dc37fa1b2.jpg)


![week-8-cruddurAvatarUpload-10](https://user-images.githubusercontent.com/88502375/235314240-9c5240b6-ed6c-4453-91c3-7a366df51bd7.jpg)


![week-8-API-Gateway-11](https://user-images.githubusercontent.com/88502375/235314246-e6161a31-7f24-4083-9941-cb957d7eba56.jpg)


![week-8-CruddurApiGatewayLambdaAuthorizer-12](https://user-images.githubusercontent.com/88502375/235314254-20de1618-9871-4640-bf35-95dea1e387a3.jpg)


