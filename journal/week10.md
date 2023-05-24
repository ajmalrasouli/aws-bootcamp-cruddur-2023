# Week 10 — CloudFormation Part 1

## Required Homework/Tasks


Before we run any templates, we have to create an S3 bucket to contain all of our artifacts for CloudFormation.
Also, bucket names are unique.

```sh
aws s3api create-bucket \
    --bucket cfn-artifacts-ar \
    --region us-east-1
```

***add cfn bucket to our environment:***

```sh
export CFN_BUCKET="cfn-artifacts-ar"
gp env CFN_BUCKET="cfn-artifacts-ar"

```


#### UpdateReplacePolicy options
***Delete***
CloudFormation deletes the resource and all its content if applicable during resource replacement. You can add this policy to any resource type. By default, if you don't specify an UpdateReplacePolicy, CloudFormation deletes your resources. However, be aware of the following consideration:

For Amazon S3 buckets, you must delete all objects in the bucket for deletion to succeed.

***Retain***
CloudFormation keeps the resource without deleting the resource or its contents when the resource is replaced. You can add this policy to any resource type. Resources that are retained continue to exist and continue to incur applicable charges until you delete those resources.

If a resource is replaced, the UpdateReplacePolicy retains the old physical resource but removes it from CloudFormation's scope.

***Snapshot***
For resources that support snapshots, CloudFormation creates a snapshot for the resource before deleting it. Snapshots that are created with this policy continue to exist and continue to incur applicable charges until you delete those snapshots.





#### Setting a stack policy
You can use the console or AWS CLI to apply a stack policy when you create a stack. You can also use the AWS CLI to apply a stack policy to an existing stack. After you apply a stack policy, you can't remove it from the stack, but you can use the AWS CLI to modify it.

Stack policies apply to all AWS CloudFormation users who attempt to update the stack. You can't associate different stack policies with different users.

For information about writing stack policies, see Defining a stack policy.

***To set a stack policy when you create a stack (console)***
1. Open the ***AWS CloudFormation*** console at https://console.aws.amazon.com/cloudformation.

2. On the ***CloudFormation Stacks*** page, choose ***Create stack***.

3. In the Create Stack wizard, on the ***Configure stack options*** page, expand the ***Advanced*** section and then choose ***Stack policy***.

4. Specify the stack policy:

  - To write a policy directly in the console, choose ***Enter stack policy*** and then type the stack policy directly   in the text field.

  - To use a policy defined in a separate file, choose ***Upload a file***, then ***Choose file*** to select the file containing the stack policy.

***To set a stack policy when you create a stack (AWS CLI)***
- Use the aws cloudformation create-stack command with the --stack-policy-body option to type in a modified policy or the --stack-policy-url option to specify a file containing the policy.

***To set a stack policy on an existing stack (AWS CLI only)***
- Use the aws cloudformation set-stack-policy command with the --stack-policy-body option to type in a modified policy or the --stack-policy-url option to specify a file containing the policy.

***deploy***
```sh
#! /usr/bin/env bash
set -e # stop the execution of the script if it fails

CFN_PATH="/workspace/aws-bootcamp-cruddur-2023/aws/cfn/template.yaml"

cfn-lint $CFN_PATH
aws cloudformation deploy \
  --stack-name "my-cluster" \
  --s3-bucket "cfn-artifacts-ar" \
  --template-file $CFN_PATH \
  --no-execute-changeset \
  --capabilities CAPABILITY_NAMED_IAM

```

***ecs-cluster.guard***
```sh
let aws_ecs_cluster_resources = Resources.*[ Type == 'AWS::ECS::Cluster' ]
rule aws_ecs_cluster when %aws_ecs_cluster_resources !empty {
  %aws_ecs_cluster_resources.Properties.CapacityProviders == ["FARGATE"]
  %aws_ecs_cluster_resources.Properties.ClusterName == "MyCluster"
}
```

***template.yaml***

```sh
AWSTemplateFormatVersion: 2010-09-09
Description: |
  Setup ECS Cluster
Resources:
  ECSCluster: #LogicalName
    Type: 'AWS::ECS::Cluster'
    Properties:
      ClusterName: MyCluster1
      CapacityProviders:
        - FARGATE
#Parameters:
#Mappings:
#Outputs:
#Metadata:

```



### Using redirects

Redirects enable a web server to reroute navigation from one URL to another. Common reasons for using redirects include to customize the appearance of a URL, to avoid broken links, to move the hosting location of an app or site without changing its address, and to change a requested URL to the form needed by a web app.

### ***Types of redirects***
There are several types of redirects that support specific scenarios.

***Permanent redirect (301)***

301 redirects are intended for lasting changes to the destination of a web address. Search engine ranking history of the original address applies to the new destination address. Redirection occurs on the client-side, so a browser navigation bar shows the destination address after redirection.

Common reasons to use 301 redirects include:

- To avoid a broken link when the address of a page changes.

- To avoid a broken link when a user makes a predictable typo in an address.


***Temporary redirect (302)***

302 redirects are intended for temporary changes to the destination of a web address. Search engine ranking history of the original address doesn’t apply to the new destination address. Redirection occurs on the client-side, so a browser navigation bar shows the destination address after redirection.

Common reasons to use 302 redirects include:

- To provide a detour destination while repairs are made to an original address.

- To provide test pages for A/B comparison of a user interface.



### Cruddur Network Diagram
(I have used Draw.io as my trail has run out with Lucid charts).

![image](https://user-images.githubusercontent.com/88502375/235677956-55230cd4-17bc-47f0-a03c-3c7a84e4eae2.png)


```sh
aws cloudformation describe-change-set --change-set-name arn:aws:cloudformation:us-east-1:804789588521:changeSet/awscli-cloudformation-package-deploy-1683030723/d68bbec8-23ce-429c-a82d-a560eab91339
```

```yml
{
    "Changes": [
        {
            "Type": "Resource",
            "ResourceChange": {
                "Action": "Add",
                "LogicalResourceId": "ALBSG",
                "ResourceType": "AWS::EC2::SecurityGroup",
                "Scope": [],
                "Details": []
            }
        },
        {
            "Type": "Resource",
            "ResourceChange": {
                "Action": "Add",
                "LogicalResourceId": "ALB",
                "ResourceType": "AWS::ElasticLoadBalancingV2::LoadBalancer",
                "Scope": [],
                "Details": []
            }
        },
        {
            "Type": "Resource",
            "ResourceChange": {
                "Action": "Add",
                "LogicalResourceId": "ApiALBListernerRule",
                "ResourceType": "AWS::ElasticLoadBalancingV2::ListenerRule",
                "Scope": [],
                "Details": []
            }
        },
        {
            "Type": "Resource",
            "ResourceChange": {
                "Action": "Add",
                "LogicalResourceId": "BackendTG",
                "ResourceType": "AWS::ElasticLoadBalancingV2::TargetGroup",
                "Scope": [],
                "Details": []
            }
        },
        {
            "Type": "Resource",
            "ResourceChange": {
                "Action": "Add",
                "LogicalResourceId": "FargateCluster",
                "ResourceType": "AWS::ECS::Cluster",
                "Scope": [],
                "Details": []
            }
        },
        {
            "Type": "Resource",
            "ResourceChange": {
                "Action": "Add",
                "LogicalResourceId": "FrontendTG",
                "ResourceType": "AWS::ElasticLoadBalancingV2::TargetGroup",
                "Scope": [],
                "Details": []
            }
        },
        {
            "Type": "Resource",
            "ResourceChange": {
                "Action": "Add",
                "LogicalResourceId": "HTTPListener",
                "ResourceType": "AWS::ElasticLoadBalancingV2::Listener",
                "Scope": [],
                "Details": []
            }
        },
        {
            "Type": "Resource",
            "ResourceChange": {
                "Action": "Add",
                "LogicalResourceId": "HTTPSListener",
                "ResourceType": "AWS::ElasticLoadBalancingV2::Listener",
                "Scope": [],
                "Details": []
            }
        }
    ],
    "ChangeSetName": "awscli-cloudformation-package-deploy-1683030723",
    "ChangeSetId": "arn:aws:cloudformation:us-east-1:804789588521:changeSet/awscli-cloudformation-package-deploy-168303
0723/d68bbec8-23ce-429c-a82d-a560eab91339",
    "StackId": "arn:aws:cloudformation:us-east-1:804789588521:stack/CrdCluster/5811cdb0-e8e5-11ed-a3fb-0e452a9f4223",
    "StackName": "CrdCluster",
    "Description": "Created by AWS CLI at 2023-05-02T12:32:03.175748 UTC",
    "Parameters": [
        {
            "ParameterKey": "FrontendHealthCheckIntervalSeconds",
            "ParameterValue": "15"
        },
        {
            "ParameterKey": "BackendHealthCheckPort",
            "ParameterValue": "80"
        },
        {
            "ParameterKey": "BackendPort",
            "ParameterValue": "4567"
        },
        {
            "ParameterKey": "BackendHealthCheckIntervalSeconds",
            "ParameterValue": "15"
        },
        {
            "ParameterKey": "BackendHealthCheckPath",
            "ParameterValue": "/api/health-check"
        },
        {
            "ParameterKey": "FrontendHealthCheckProtocol",
            "ParameterValue": "HTTP"
        },
        {
            "ParameterKey": "BackendHealthCheckProtocol",
            "ParameterValue": "HTTP"
        },
        {
            "ParameterKey": "FrontendUnhealthyThresholdCount",
            "ParameterValue": "2"
        },
        {
            "ParameterKey": "NetworkingStack",
            "ParameterValue": "CrdNet"
        },
        {
            "ParameterKey": "FrontendHealthCheckPort",
            "ParameterValue": "80"
        },
        {
            "ParameterKey": "BackendHealthCheckTimeoutSeconds",
            "ParameterValue": "5"
        },
        {
            "ParameterKey": "BackendUnhealthyThresholdCount",
            "ParameterValue": "2"
        },
        {
            "ParameterKey": "FrontendHealthCheckPath",
            "ParameterValue": "/"
        },
        {
            "ParameterKey": "FrontendHealthyThresholdCount",
            "ParameterValue": "2"
        },
        {
            "ParameterKey": "BackendHealthyThresholdCount",
            "ParameterValue": "2"
        },
        {
            "ParameterKey": "FrontendPort",
            "ParameterValue": "3000"
        },
        {
            "ParameterKey": "FrontendHealthCheckTimeoutSeconds",
            "ParameterValue": "5"
        },
        {
            "ParameterKey": "CertificateArn",
            "ParameterValue": "arn:aws:acm:us-east-1:804789588521:certificate/2334c957-2ee6-4773-9748-aefbb3d415bd"
        }
    ],
    "CreationTime": "2023-05-02T12:32:04.421000+00:00",
    "ExecutionStatus": "AVAILABLE",
    "Status": "CREATE_COMPLETE",
    "StatusReason": null,
    "NotificationARNs": [],
    "RollbackConfiguration": {},
    "Capabilities": [
        "CAPABILITY_NAMED_IAM"
    ],
    "Tags": [
        {
            "Key": "group",
            "Value": "cruddur-cluster"
        }
    ],
    "ParentChangeSetId": null,
    "IncludeNestedStacks": false,
    "RootChangeSetId": null
}

```
✅️ ${\color{lightblue}awscli \space Cloudformation \space package \space deploy}$
---
![week-10-cloudformation-01](https://user-images.githubusercontent.com/88502375/235679064-33e34889-8339-4b00-b7ee-1b76af9d539e.jpg)

✅️ ${\color{lightblue}awscli \space Cloudformation \space package \space deploy \space change \space set}$
---
![week-10-cloudformation-change-set-02](https://user-images.githubusercontent.com/88502375/235679093-866f77e0-16a9-4f72-a165-e8fa078a69f1.jpg)

✅️ ${\color{lightblue}Amazon \space S3 \space Buckets \space (cfn-aritfacts-ar)}$
---
![week-10-cloudformation-deploy-stack-03](https://user-images.githubusercontent.com/88502375/235679105-c5748808-9c13-4616-b2a3-d90e494b2196.jpg)

✅️ ${\color{lightblue}Amazon \space S3 \space Buckets \space (cfn-aritfacts-ar)}$
---
![week-10-cfn-artifacts-ar-04](https://user-images.githubusercontent.com/88502375/235679118-a03a0b3b-5776-4d35-bd68-c4bc1f7db251.jpg)

✅️ ${\color{lightblue}List \space out \space the \space availability \space zone's \space for \space us-east-1 \space using \space ChatGPT)}$
---
![week-10-azs-for-us-east-05](https://user-images.githubusercontent.com/88502375/235679110-f64af6e4-dbd8-4e3b-bfff-2c7bbd419033.jpg)

✅️ ${\color{lightblue}Cruddur \space Cluster \space Stack \space change \space set}$
---
![week-10-crudur-stack-06](https://user-images.githubusercontent.com/88502375/235679341-f4947f75-8eb5-499f-80d4-b3c9eb186ef3.jpg)

✅️ ${\color{lightblue}Change \space set}$
---
![week-10-crudur-stack--changes-07](https://user-images.githubusercontent.com/88502375/235679348-32ee4b5f-eeaf-499a-b485-fbfb5596cdbc.jpg)

✅️ ${\color{lightblue}Cruddur \space stack \space info}$
---
![week-10-crudur-stack-info-08](https://user-images.githubusercontent.com/88502375/235679369-4f7c8e84-686c-4879-a398-9db8f3251b17.jpg)

✅️ ${\color{lightblue}Cruddur \space Stack \space Events}$
---
![week-10-crudur-stack-events-09](https://user-images.githubusercontent.com/88502375/235679355-eb0068eb-4fb7-4529-a60b-08a593fe5327.jpg)

✅️ ${\color{lightblue}Cruddur \space Stack \space Resources}$
---
![week-10-crudur-resources-10-1](https://user-images.githubusercontent.com/88502375/235679393-21247304-4b36-4ee7-9f0f-6383f8517dc1.jpg)

✅️ ${\color{lightblue}Cruddur \space Stack \space Resources \space more...}$
---
![week-10-crudur-stack-outputs-11](https://user-images.githubusercontent.com/88502375/235679373-bdc400e5-3fea-4845-a128-c52dd6fa7721.jpg)

✅️ ${\color{lightblue}Cloudformation \space deploy \space implementation}$
---
![week-10-crudur-stack-parameters-12](https://user-images.githubusercontent.com/88502375/235679384-8b0f64e0-481d-4d19-a761-9f3dc694574b.jpg)

✅️ ${\color{lightblue}Cloudformation \space deploy \space implementation}$
---
![week-10-crudurVPC-13](https://user-images.githubusercontent.com/88502375/235679832-76b418e9-f4d5-4a48-b3a4-48908b9fc1be.jpg)

✅️ ${\color{lightblue}Cloudformation \space deploy \space implementation}$
---
![week-10-CruddurVPC-Resource-map-14](https://user-images.githubusercontent.com/88502375/235679814-c3ff88c0-2732-4097-bf47-a4532e906793.jpg)

✅️ ${\color{lightblue}Cloudformation \space deploy \space implementation}$
---
![week-10-crudur-diagram-16](https://user-images.githubusercontent.com/88502375/235679829-0c92fe42-a7aa-4fef-8b5e-ef260fea50f4.jpg)

✅️ ${\color{lightblue}Cloudformation \space deploy \space implementation}$
---
![week-10-CrdNet-stack-info-17](https://user-images.githubusercontent.com/88502375/235679743-a97b0666-7fda-4bae-ad62-04a6fd065b88.jpg)

✅️ ${\color{lightblue}Cloudformation \space deploy \space implementation}$
---
![week-10-CrdNet-stack-outputs-18](https://user-images.githubusercontent.com/88502375/235679760-9b289dfb-800f-40cc-ad94-124760ab38ea.jpg)

✅️ ${\color{lightblue}Cloudformation \space deploy \space implementation}$
---
![week-10-CrdNet-stack-parameters-19](https://user-images.githubusercontent.com/88502375/235679783-033f36fa-33cb-490a-aac2-aa79671d8ec5.jpg)

✅️ ${\color{lightblue}Cloudformation \space deploy \space implementation}$
---
![week-10-networking-deploy-20](https://user-images.githubusercontent.com/88502375/235679843-b1feeb8b-df7b-4b00-8544-4ae50e9b2c55.jpg)

✅️ ${\color{lightblue}Cloudformation \space deploy \space implementation}$
---
![week-10-cluster-deploy-21](https://user-images.githubusercontent.com/88502375/235679873-b787f9ea-6600-4772-9fad-0d9e70eb1911.jpg)

✅️ ${\color{lightblue}Cloudformation \space deploy \space implementation}$
---
![week-10-cluster-deploy-22](https://user-images.githubusercontent.com/88502375/235679890-f3f7e5ad-80d5-4e56-8b98-d7ea4d10cb1c.jpg)

✅️ ${\color{lightblue}Cloudformation \space deploy \space implementation}$
---
![week-10-CrdNet-stacks-23](https://user-images.githubusercontent.com/88502375/235679799-9ffe3d2b-ad70-43b3-b456-76144e6e13ba.jpg)

✅️ ${\color{lightblue}Cloudformation \space deploy \space implementation}$
---
![week-10-CrdCluster-stack-info-24](https://user-images.githubusercontent.com/88502375/235679917-13a4dbc8-7af9-4fc2-9140-643f4cac8646.jpg)

✅️ ${\color{lightblue}Cloudformation \space deploy \space implementation}$
---
![week-10-CrdCluster-stack-resources-25](https://user-images.githubusercontent.com/88502375/235680000-1b0161b7-dc93-410f-abda-b2e0f5a54c34.jpg)

✅️ ${\color{lightblue}Cloudformation \space deploy \space implementation}$
---
![week-10-CrdCluster-stack-outputs-26](https://user-images.githubusercontent.com/88502375/235679960-7890833c-8171-485a-95f8-2c1876a415ce.jpg)

✅️ ${\color{lightblue}Cloudformation \space deploy \space implementation}$
---
![week-10-CrdCluster-stack-parameters-27](https://user-images.githubusercontent.com/88502375/235679976-b3ed7f8a-016b-4d8d-928f-81432e9ea8be.jpg)




### AWS CloudFormation Best Practices for Infrastructure as Code

1. ${\color{green}Modularity}$ - Break down stacks into smaller, reusable templates for flexibility and ease of managment.
2. ${\color{green}Parameters}$ - Use parameters to allow for customisation of stacks and avoid hardcoding values.
3. ${\color{green}Conditional Logic}$ - Utilise conditionals to control resource creation and updates based on specific circumstances.
4. ${\color{green}Resource Naming}$ - Follow a consistent naming convetion fo resources to aid in tracking and manangement.
5. ${\color{green}Validation}$ - Validate templates before deployment to catch errors and potential issues early on.
6. ${\color{green}Testing}$ - Test changes in a staging environment to ensure proper functionality and avoid issues in production.
7. ${\color{green}Documentation}$ - Document stacks thoroughly to aid in troubleshooting and understanding of the infrastructure.



### What Is AWS CloudFormation?

CloudFormation is an infrastructure automation platform for AWS that deploys AWS resources in a repeatable, testable and auditable manner.



### Benefits of CloudFormation

🔷 Deployment speed
🔷 Scaling up
🔷 Service integration
🔷 Consistency
🔷 Security
🔷 Easy updates
🔷 Auditing and change management


### Alternatives to CloudFormation

🟧 HashiCorp Terraform

🟧 Ansible



### CloudFormation Template Terms and Concepts


🟩 Template

A CloudFormation template is simply a text file, formatted in a specific way (see below for details on formatting), that defines how AWS services or resources should be configured and deployed.


🟩 Stacks

A stack is a term AWS uses to refer to a collection of multiple AWS resources -- such as EC2 virtual machines, S3 storage, and IAM access controls -- that you can manage together using a single template.


🟩 Formatting

CloudFormation supports templates that are formatted using either JSON or YAML. These are widely used file formats for structuring text files. Most other IaC tools use the same formatting languages, as do platforms like Kubernetes.


🟩 Parameters

If you need to apply unique settings for each deployment, you can do so using parameters. Parameters let you define custom values for each deployment that CloudFormation will apply at runtime.

🟩 Conditions

You can also fine-tune deployments by setting conditions, which let you define conditional rules to govern precisely how each deployment proceeds.


🟩 Change sets

If you want to update a deployment using CloudFormation, you can update the template you used to create the deployment. You can then create a change set, which summarizes the changes that the updated template will apply before making the change.


🟩 Functions

There are several ways to get data into a CloudFormation template, with parameters being the primary. But those parameters may not be known at deployment time. CloudFormation Functions allow CloudFormation Designers to retrieve data from resources deployed in the current CloudFormation or from external sources in the AWS account. Ref is used extensively to reference other resources inside the template like the example below. It creates an EIP for the instance created earlier in the template.



Manually setting up and deploying AWS resources is an unproductive use of your team's time. It also increases the risk of configuration oversights and inconsistencies that can lead to management problems and security risks. Furthermore, it makes it harder to update or scale resources quickly.

By leveraging an IaC tool such as CloudFormation, your team can streamline the AWS deployment process. You can define your resource configurations once, then deploy them as many times as you need. You can also quickly and predictably update resources via change sets, and you can use your CloudFormation templates to keep track of how you configure your resources and how they have changed over time.
