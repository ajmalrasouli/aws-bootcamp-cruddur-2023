# Week 6 — Deploying Containers

## Required Homework/Tasks

### What is ECR?

### Amazon Elastic Container Registry (ECR) is a managed Docker container registry that makes it easy to store, manage, and deploy Docker container images. ECR supports private Docker registries with resource-based permissions using AWS IAM, so specific users and instances can access images. Using ECR simplifies going from development to production, and eliminates the need to operate your own container repositories or worry about scaling the underlying infrastructure, while hosting your images in a highly available and scalable architecture.

### Creating and Configuring an AWS ECR Repository

Container images ideally are stored in repositories. Before deploying and hosting Docker images on AWS ECR, you’ll need first to create and configure a repository to store your Docker image.

1. Open your favorite web browser, navigate to AWS ECR, and log in with your AWS account.

2. Once logged in, click Get Started to initialize creating a repository.

3. Next, provide a unique repository name, we will use cloud-security-bootcamp.

![Create repository 1](https://user-images.githubusercontent.com/88502375/227785351-ef4f3db7-4f8b-4d4d-bff1-e7f2da585ffa.png)
![Create repository 2](https://user-images.githubusercontent.com/88502375/227785389-de5e79a7-7a7d-4476-b94a-79f06509ae69.png)

After creating the repository, you will see your newly created repository listed, as shown below.

![image](https://user-images.githubusercontent.com/88502375/227785496-68ef7b8a-c38b-40c8-b8cd-88a04d27ec1e.png)

### Creating an IAM User and Granting Access to ECR
We have successfully created a repository on AWS ECR, but how to manage our repository? We will need a dedicated IAM user granted with required access to perform tasks on our ECR repository.

To create an IAM user to interact with your ECR repository, follow these steps:

1. On the AWS Management Console, search for IAM, and select the first option, as shown below, to access the IAM dashboard.

![image](https://user-images.githubusercontent.com/88502375/227785619-e7001512-f764-46cf-9adb-d45227f39fc7.png)

2. Next, select Users (left panel) on your IAM dashboard, and click Add users (top-right) to initiate adding a new IAM user.

![image](https://user-images.githubusercontent.com/88502375/227785771-26bcc6f1-efb7-4d2d-b87c-587a0d5d2ea6.png)

3. Set the user details and AWS access type with the following:

- Provide a unique User name, but this tutorial’s choice is aws-ecr.
- Choose the Access key – Programmatic access option, so you will only need an access key ID and a secret access key to access your AWS ECR repository via the AWS CLI.
- Click Next: Permissions to proceed setting permissions for the IAM user.

3. On the pop-up Push commands window, copy the first command (aws ecr get-login-password).
4. Now, paste the command in your terminal and hit Enter. This command retrieves an authentication token and authenticates your Docker client to your AWS ECR.
If successful, you will see the following output with a message that says Login Succeeded.
5. Run the following commands to change your working directory (cd) to your project directory and build (docker build) a Docker image (node-app).
6. Copy the third push command (docker tag) in the Push commands window, and run the command in your terminal to add the latest tag to your image. Doing so allows you to push the image to your repository.
7. Finally, copy the fourth command (docker push), and run it on your terminal to push your Docker image to your repository on ECR.
8. 
![week-6-ECR-1](https://user-images.githubusercontent.com/88502375/227789019-ca3be32d-3ce6-4545-ab19-6cdf83d50600.jpg)

![week-6-ECR-2](https://user-images.githubusercontent.com/88502375/227789032-9124c37d-43e7-4d33-bb86-8f6007a29a6e.jpg)

![week-6-ECR-3](https://user-images.githubusercontent.com/88502375/227789078-4cb552f0-2efb-4c94-8a12-fa11586afc23.jpg)

![week-6-ECR-4](https://user-images.githubusercontent.com/88502375/227789085-b93f35ae-5fc1-479b-9a84-8fa616197a41.jpg)

![week-6-ECR-5](https://user-images.githubusercontent.com/88502375/227789092-420a77c1-5f5d-4bcc-bbab-2c15d3d7aa47.jpg)

![week-6-ECR-6](https://user-images.githubusercontent.com/88502375/227789094-fc73f00c-a181-4ec5-9100-c4e8ce5b0d44.jpg)

![week-6-CloudWatch-Log-7](https://user-images.githubusercontent.com/88502375/230061763-af6dc2d1-f82d-40bd-8ac8-82b9a4ba578d.jpg)


![week-6-ecs-cruddur-8](https://user-images.githubusercontent.com/88502375/230061829-dc18d330-9267-46ac-855d-28ba1419c828.jpg)

#### Checking if Flask server is running
![week-6-Flask-server-is-running](https://user-images.githubusercontent.com/88502375/230061948-2086b01c-50ae-4eda-9fe7-f1cb08a34b0b.jpg)

#### Creating cruddur-python repository on aws ecr. 
![week-6-ECR-10](https://user-images.githubusercontent.com/88502375/230062123-ada61b61-ad32-42d9-a5d1-5ddf8a629d31.jpg)


#### Pulling pyhon image called 3.10-slim-buster.
![week-6-pull-docker-11](https://user-images.githubusercontent.com/88502375/230062141-e6ab62c0-87e6-4f98-8498-013dc4a95cf1.jpg)

#### Confirmaing our image health check.
![week-6-flask-health-check-12](https://user-images.githubusercontent.com/88502375/230062155-fdc73fa0-16d9-490a-a95a-09ba11db7d31.jpg)

#### AWS Parameter settings.
![week-6-aws-parameter settings-12](https://user-images.githubusercontent.com/88502375/230062177-0337ac8e-2c03-45b6-a8fe-8ce81c03f723.jpg)


#### Storing cruddur app secrets on AWS Systems Manager / My parameters
![week-6-aws-parameter settings-13](https://user-images.githubusercontent.com/88502375/230062199-bd979cd5-3c75-40ed-b5df-e82160ce67f8.jpg)

#### Updating and creating Roles and Policy.
![week-6--iam-permissions-14](https://user-images.githubusercontent.com/88502375/230062230-bbb92baa-692b-465e-8b1e-87d58e24a813.jpg)

#### Creating Task definitions for backend-flask
![week-6--task-definition-15](https://user-images.githubusercontent.com/88502375/230062253-8fc6d93f-5716-46cb-9f65-a16d5accbfd2.jpg)

#### Issues with backend-flask deployemnt.
![week-6--error-backend-flask-deployemt-16](https://user-images.githubusercontent.com/88502375/230062274-be457aab-ea29-444e-9170-f6b3e3c6caad.jpg)

#### Error while backend-flask deployment
![week-6--error-backend-flask-deployemt-17](https://user-images.githubusercontent.com/88502375/230062289-8377d4bb-50c6-420e-86ec-da50bbfbd9b1.jpg)

#### Health check inside backend-flask container.
![week-6-health-check-inside-backend-flask-container-18](https://user-images.githubusercontent.com/88502375/230062346-b2323c8d-e39a-4319-84f9-7cd0bd6e0241.jpg)
