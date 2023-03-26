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

