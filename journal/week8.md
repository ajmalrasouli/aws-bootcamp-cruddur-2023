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

### Create The App
The cdk init command can be used to initialize a new application in the language of your choice. Each CDK app maintains its own set of module dependencies and should be created in its own directory. For example, we can create a TypeScript CDK application with the cruddur-app template by using the following command:

```py
cdk init cruddur-app --language=typescript
```

The $\color{color-blue}{cdk init}$ command also initializes the project as a Git repository, along with the $\color{color-blue}{.gitignore}$ file. Apart from that, it generates a $\color{color-blue}{package.json}$ file for managing project dependencies and a $\color{color-blue}{tsconfig.json}$ file for TypeScript configuration.

Once you have initialized the project, you can run the build command to manually compile the app. This step isn’t mandatory, because the cdk toolkit does it for you before you deploy the changes, but a manual build can sometimes help in catching syntax errors. Here’s how it can be done:

