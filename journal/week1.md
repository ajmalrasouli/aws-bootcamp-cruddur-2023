# Week 1 — App Containerization

## Required Homework/Tasks

### Docker
The best way to describe Docker is to use the phrase from the Docker web site—Docker is
“an open source project to pack, ship and run any application as a lightweight container.”
Thus the idea of Docker is to have an abstraction layer that allows the application
developers to package any application and then let the containerization technology take
care of the deployment aspects to any infrastructure.

### Why do we need containerized applications?
Containerization allows developers to create and deploy applications faster and more securely. With traditional methods, code is developed in a specific computing environment which, when transferred to a new location, often results in bugs and errors.


### What is DockerHub?
Understanding Docker Hub Registry
registry service that is cloud-based; the Docker Hub Registry allows the user to do the following:

- Link to code repositories
- Build images and test them
- Stores images that are manually pushed
- Links to Docker Cloud to help deploy images to a host.

In summary, we can understand the Docker Hub Registry as a tool that offers a centralized resource for discovering a container image, managing distribution and change, facilitating collaboration between the user and team, and automating workflow throughout the development pipeline.


## Cloud Development Environment (CDE)


### Gitpod
#### Up to 50 hours of usage/month
![Gitpod workspace](assets/week-1-gitpod-workspace.jpg)



### GitHub Codespaces
#### Up to 60 hours of usage/month
![Github workspace](assets/week-1-codespaces-workspace.jpg)


### AWS Cloud9: I am not using AWS Cloud9 
#### Avoid using Cloud9 in case of free tier instance in use for other purpose.
It's a tricky part if you are using your free tier instance somewhere else in the account avoid AWS Cloud9 because at the end of month the 
bill will be aggregated hours of uses so even if you use T2 micro with Cloud9 and you are using T2 micro or T3 micro for some other purposes
the bill will be there so, make sure to avoid.


### Common Docker Commands
- docker run – Used for running a command in a new container
- docker start – For starting one or more stopped containers
- docker stop – For stopping one or more running containers
- docker build – Used for building an image form in a Docker file
- docker pull – For pulling an image or a repository from a registry
- docker push – Given for pushing an image or a repository to a registry
- docker export – For exporting a container’s filesystem as a tar archive
- docker exec – To run a command in a run-time container
- docker search – For searching the Docker Hub for images
- docker volume- To create and attach to containers to store data.
- docker network- allows you to attach a container to as many networks as you like. You can also attach an already running container.
- docker attach – To attach to a running container
- docker commit – For creating a new image from a container’s changes
- docker daemon – Having listened for Docker API requests, the Docker daemon (dockerd) manages Docker objects. These include networks, volumes, containers, and images. It also communicates with other daemons when managing Docker services.
- docker Images – A read-only template, an image has instructions that are used to create a Docker container. Many times, images are based on other images and carry some degree of customization. An image-based on ubuntu can install the Apache web server, your application, and the configuration details that the application needs to run.


## Homework Challenges

#### Run the dockerfile CMD as an external script
#### Push and tag a image to DockerHub

- Create a docker hub account. 
![Docker Hub account](https://user-images.githubusercontent.com/88502375/221357166-8369c120-113c-453a-8a45-60910d17d4ea.png)

- Pull a docker image
![Docker Hub Pull image](https://user-images.githubusercontent.com/88502375/221357479-0c980fde-8395-459d-b158-2e6533bb6c53.png)

- create a custom tag to docker image
![Docker image tag](https://user-images.githubusercontent.com/88502375/221357806-d81c42e4-8483-40a1-961e-68c20913e8d3.png)


#### Use multi-stage building for a Dockerfile build
What are the benefits of multi-stage builds in Docker?
Some of the benefits of having multi-stage builds in Docker are as follows:

1. Multi-stage builds are ideal for deploying production-ready applications.
2. Multi-stage builds work with only one Dockerfile.
3. It allows us to build smaller images, and Dockerfile separates them into various build stages.
4. We have a uniform syntax to learn.
5. Muti-stage builds work on local machines as well as on the CI (Continuous Integration) server.
6. The multi-stage builds usually work with only one Dockerfile. In this Dockerfile, we use multiple FROM statements to define various stages of builds.
7. Using multi-stage builds, we can limit the size of the image we create. In single-stage builds, with each instruction executed, a new layer gets added to the image, making it bulky.
8. With multi-stage builds, we can name a particular stage, stop the build at a specific stage, use an external image, or switch between stages.

#### Implement a health check in the V3 Docker compose file
#### Research best practices of Dockerfiles and attempt to implement it in your Dockerfile
#### Learn how to install Docker on your local machine and get the same containers running outside of Gitpod / Codespaces
#### Launch an EC2 instance that has docker installed, and pull a container to demonstrate you can run your own docker processes. 
