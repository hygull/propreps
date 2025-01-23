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

#### What if I have AWS RDS? Still db: is required in Docker compose. Please tell me what does it do?

If you are using AWS RDS (Relational Database Service) for your database, you typically do not need to include a db: service in your docker-compose.yml. Here's why and what db: in Docker Compose usually does:

###### What Does `db:` Do in Docker Compose?
In a Docker Compose file, the db: service is typically used to define a containerized database that runs alongside your application. For example:

```yml
services:
  db:
    image: postgres:13
    environment:
      POSTGRES_USER: user
      POSTGRES_PASSWORD: password
```

This `db:` service creates a PostgreSQL container where your application can connect to store data.

##### What Changes When Using AWS RDS?
If you're using AWS RDS, the database is already hosted and managed in the cloud. You don't need to containerize the database, as RDS provides the database as a service.

Instead of `db:`, you:
1. Configure your application to connect to the RDS endpoint and port.
2. Set the required credentials (username, password) in your application's configuration.
For example, in a Django app:

```yaml
services:
  web:
    build: .
    ports:
      - "8000:8000"
    environment:
      DATABASE_HOST: my-rds-instance.xxxxxx.amazonaws.com
      DATABASE_PORT: 5432
      DATABASE_USER: myuser
      DATABASE_PASSWORD: mypassword
      DATABASE_NAME: mydatabase
```

Why Might You Still Use db: Locally?
You might want to include a db: service in docker-compose.yml for local development or testing purposes. For instance:

- Running a PostgreSQL/MySQL container locally to mimic production.
- Avoiding direct connections to AWS RDS for every test (reduces costs and risks).
Example:

```yaml
services:
  web:
    build: .
    ports:
      - "8000:8000"
    environment:
      DATABASE_HOST: db
      DATABASE_PORT: 5432
      DATABASE_USER: user
      DATABASE_PASSWORD: password
      DATABASE_NAME: localdb

  db:
    image: postgres:13
    environment:
      POSTGRES_USER: user
      POSTGRES_PASSWORD: password
      POSTGRES_DB: localdb
```

In this example:

For production, the `DATABASE_HOST` points to the RDS endpoint.
For local development, it points to the db: service.

##### Best Practices for Using AWS RDS
1. Separate Production and Development Configurations:
	- Use .env files or environment variables to switch between RDS and local databases.

2. Use Secrets for Credentials:
	- Use secure methods (e.g., AWS Secrets Manager) to store sensitive information.

3. Avoid Hardcoding RDS Details:
	- Dynamically load the connection details using environment variables or configuration files.
