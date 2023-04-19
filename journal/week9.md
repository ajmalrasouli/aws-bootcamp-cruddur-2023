# Week 9 — CI/CD with CodePipeline, CodeBuild and CodeDeploy

## Required Homework/Tasks

### Automate your software delivery process using continuous integration and delivery (CI/CD) pipelines

What Is CI/CD on AWS?

A continuous integration / continuous delivery (CI/CD) pipeline that lets you submit new code on one end, build it, automatically test it, and deploy it to a production environment. Each stage is a logical unit within the delivery process, acting as a gate that validates a certain aspect of your code. 

As your code progresses through the CI/CD pipeline, quality should increase as more aspects are verified. Test results are received immediately due to automation, and the pipeline stops builds and releases if they do not pass predetermined quality thresholds.

Many CI/CD pipelines are implemented in public cloud environments. Amazon Web Services (AWS) provides a collection of CI/CD tools to help accelerate software development and release lifecycles. AWS CodePipeline, for example, can automate the build, testing, and deployment phases for every code change according to defined release models. You can integrate CodePipeline with other AWS Services, such as Amazon S3, or third parties like GitHub.


### AWS CI/CD Tools and Services
#### AWS CodePipeline

AWS CodePipeline is a cloud-based continuous delivery service. It can automatically compile, build, and test your code, and continuously deliver container-based applications to the AWS cloud. It can perform pre-deployment validation of the artifacts (container images, descriptors, etc.) needed for network service or cloud native network functions.

AWS CodePipeline can also help you run various tests for containerized network function / virtual network function (CNF/VNF), such as baseline and regression testing. You can also use this service to run functional testing, performance testing, and reliability and disaster recovery (DR) testing.

![week-9-CICD-01](https://user-images.githubusercontent.com/88502375/233170384-50f18107-8410-4189-8b81-a89f26e3ebba.jpg)


### AWS CodeCommit
AWS CodeCommit is a managed source control service that lets you store private Git repositories and various managed assets, including source code, binary files, and documents, in the AWS cloud. The service is highly scalable and secure and eliminates the need to self-manage source control systems and scale the underlying infrastructure.


### AWS CodeBuild
AWS CodeBuild is a fully managed continuous integration (CI) service that builds services in the cloud. It compiles source code, runs unit tests, and creates deployment-ready artifacts. There is no need to provision, scale, and manage the build servers—CodeBuild offers pre-packaged build environments for commonly-used programming languages and scales automatically to meet peaks in build requests. It provides build tools like Apache Maven and Gradle and also lets you customize build environments and use your existing build tools.


### AWS CodeDeploy
CodeDeploy is a cloud-based deployment service that automatically deploys applications to various targets, including Amazon EC2 instances, serverless Lambda functions, Amazon ECS services, and on-premises instances. It can deploy application content running on a server and stored in GitHub or Bitbucket repositories and Amazon S3 buckets and deploy serverless Lambda functions. There is no need to make changes to your code to use CodeDeploy.




### Best practices when automating CI/CD with Codepipeline
- Keep your CI/CD secure. Track logins, use SAST tools, and scan the code for vulnerabilities.
- Use a combination of manual and automation testing. Integrate CI/CD pipeline with automation test suite.
- Commit the code on a daily basis, reduce branching, and aim for small commit sizes.
- You should build only once instead of building at every stage. Build once, run everywhere.
- Test the code in the early stages instead of testing after the deployment.
- Fail fast. As soon as code breaks due to a code push, immediately rollback and get the issues fixed.
- Preferably use trunk-based development. Keep your branches short, and merge into the trunk as fast as possible.
- If you create a pipeline or action configuration that uses API keys or secrets, use the secrets manager to reference the secret in the pipeline and action      configuration. Do not specify secrets directly inside the action configuration.
- If you use codepipeline that uses an S3 bucket, then you must configure server-side encryption for that S3 bucket using AWS KMS keys.

### References:

https://aws.amazon.com/getting-started/hands-on/set-up-ci-cd-pipeline/

https://codefresh.io/learn/ci-cd/ci-cd-on-aws-the-basics-and-4-best-practices/


cruddur-backend-flask-bake-image.
![week-9-CodeBuild-1](https://user-images.githubusercontent.com/88502375/233171021-bf9d3b0d-72b8-44dc-afb0-0af4831bb9e7.jpg)


CodeBuild Phase details.
![week-9-CodeBuild-2](https://user-images.githubusercontent.com/88502375/233171033-3b9833e9-fb98-46d5-98f0-507c75cc95ca.jpg)


creating cruddur-backend-fargate Pipeline.
![week-9-Pipelines-3](https://user-images.githubusercontent.com/88502375/233171050-7d1bd6df-891c-4aff-9b68-21a4aec533ca.jpg)

Pipeline created successfully.
![week-9-Pipelines-4](https://user-images.githubusercontent.com/88502375/233171073-4bfe3aca-7eee-48db-9b58-0317fe2dd52d.jpg)

#### buildspec.yml to build new images from our GitHub repository

```sh
# Buildspec runs in the build stage of your pipeline.
version: 0.2
phases:
  install:
    runtime-versions:
      docker: 20
    commands:
      - echo "cd into $CODEBUILD_SRC_DIR/backend"
      - cd $CODEBUILD_SRC_DIR/backend-flask
      - aws ecr get-login-password --region $AWS_DEFAULT_REGION | docker login --username AWS --password-stdin $IMAGE_URL
  build:
    commands:
      - echo Build started on `date`
      - echo Building the Docker image...          
      - docker build -t backend-flask .
      - "docker tag $REPO_NAME $IMAGE_URL/$REPO_NAME"
  post_build:
    commands:
      - echo Build completed on `date`
      - echo Pushing the Docker image..
      - docker push $IMAGE_URL/$REPO_NAME
      - cd $CODEBUILD_SRC_DIR
      - echo "imagedefinitions.json > [{\"name\":\"$CONTAINER_NAME\",\"imageUri\":\"$IMAGE_URL/$REPO_NAME\"}]" > imagedefinitions.json
      - printf "[{\"name\":\"$CONTAINER_NAME\",\"imageUri\":\"$IMAGE_URL/$REPO_NAME\"}]" > imagedefinitions.json

env:
  variables:
    AWS_ACCOUNT_ID: 804789588521
    AWS_DEFAULT_REGION: us-east-1
    CONTAINER_NAME: backend-flask
    IMAGE_URL: 804789588521.dkr.ecr.us-east-1.amazonaws.com
    REPO_NAME: backend-flask:latest
artifacts:
  files:
    - imagedefinitions.json

```

To get everything working properly, I had to add a few permissions to the backend-flask CodeBuild service role.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "VisualEditor0",
      "Effect": "Allow",
      "Action": [
        "ecr:BatchCheckLayerAvailability",
        "ecr:CompleteLayerUpload",
        "ecr:GetAuthorizationToken",
        "ecr:InitiateLayerUpload",
        "ecr:PutImage",
        "ecr:UploadLayerPart",
        "ecr:BatchGetImage",
        "ecr:GetDownloadUrlForLayer"
      ],
      "Resource": "*"
    }
  ]
}
```
