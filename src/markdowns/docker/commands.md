1. docker --version
2. docker pull <image_name>:<tag> `docker pull ubuntu:20.04`
3. docker images
4. docker ps
5. docker ps -a
6. docker run <options> <image_name> `docker run -it ubuntu:20.04 /bin/bash`
7. docker stop <container_id> `docker stop abc123def456`
8. docker start <container_id> `docker start abc123def456`
9. docker rm <container_id> `docker rm abc123def456`
10. docker rmi <image_id> `docker rmi xyz789uvw123`
11. docker exec -it abc123def456 /bin/bash
12. docker logs abc123def456
13. docker network ls
14. docker volume ls



### What are main docker commands that a beginner should first learn (With brief explanations and examples)?

```bash
As a beginner learning Docker, it's essential to start with the fundamental 
Docker commands. These commands will help you create, manage, and interact 
with containers and images. Here are some of the main Docker commands along 
with brief explanations and examples:

docker --version:

Description: Displays the Docker version installed on your system.
Example:
docker --version
docker pull <image_name>:<tag>:

Description: Pulls a Docker image from a container registry (like Docker Hub) to your local machine.
Example:
docker pull ubuntu:20.04
docker images:

Description: Lists all the Docker images available on your local machine.
Example:
docker images
docker ps:

Description: Lists all running containers.
Example:
docker ps
docker ps -a:

Description: Lists all containers, including those that are stopped or exited.
Example:
docker ps -a
docker run <options> <image_name>:

Description: Runs a container from an image.
Example:
docker run -it ubuntu:20.04 /bin/bash
Explanation: This command runs an Ubuntu 20.04 container in interactive mode with a shell (/bin/bash) as the entry point. The -it flags enable interactive mode and allocate a pseudo-TTY for the shell.
docker stop <container_id>:

Description: Stops a running container by specifying its ID.
Example:
docker stop abc123def456
docker start <container_id>:

Description: Starts a stopped container by specifying its ID.
Example:
docker start abc123def456
docker rm <container_id>:

Description: Removes a container by specifying its ID.
Example:
docker rm abc123def456
docker rmi <image_id>:

Description: Removes an image by specifying its ID.
Example:
docker rmi xyz789uvw123
docker exec -it <container_id> <command>:

Description: Executes a command inside a running container.
Example:
docker exec -it abc123def456 /bin/bash
docker logs <container_id>:

Description: Displays the logs of a running or stopped container.
Example:
docker logs abc123def456
docker network ls:

Description: Lists Docker networks.
Example:
docker network ls
docker volume ls:

Description: Lists Docker volumes.
Example:
docker volume ls


These are some of the essential Docker commands for beginners. 
They provide the foundation for creating, managing, and interacting 
with containers and images. As you become more comfortable with Docker, 
you can explore more advanced commands and features to enhance your 
containerization skills.
```