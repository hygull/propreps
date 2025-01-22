## Docker

Docker is a platform and tool designed to make it easier to create, deploy, and manage applications using containers. Containers are lightweight, standalone, and executable software packages that include everything needed to run a piece of software, including the code, runtime, libraries, and system tools. Containers provide a consistent and isolated environment for applications to run, regardless of the underlying system.


## What is the difference between Docker Image & Docker Container?

A Docker image and a Docker container are related concepts in the world of containerization, but they serve different purposes and have distinct characteristics:

#### Docker Image:

1. An image is a lightweight, standalone, and executable software package that includes all the necessary code, libraries, runtime, and dependencies required to run an application.
2. Images are read-only and are used as templates for creating containers.
3. Images are created from a set of instructions specified in a Dockerfile, which defines how to build the image.
4. Images can be versioned and shared through container registries, making it easy to distribute and replicate consistent application environments.
5. Images are the building blocks for containers. When a container is created, it's instantiated from an image.

##### Docker Container:

1. A container is a runtime instance of a Docker image.
2. Containers are isolated environments where applications can run in an isolated and consistent manner, regardless of the underlying host system.
3. Containers are lightweight, as they share the host system's kernel while having their own isolated user space.
4. Containers can be started, stopped, paused, and deleted. They can also be scaled up or down to accommodate different workloads.
5. Changes made within a container (such as writing files or modifying settings) are isolated to that container and do not affect other containers or the host system.
6. Containers provide process isolation and resource management, making it possible to run multiple applications on the same host without conflicts.

In summary, a Docker image is a static snapshot that encapsulates an application and its dependencies, while a Docker container is a running instance of that image, providing an isolated and consistent environment for the application to execute. Images are used as the basis for creating containers, and containers are the actual runtime instances where applications operate.