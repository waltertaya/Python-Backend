# Docker Tutorial

- OS is divided into two parts:
    1. OS application layer
    2. OS kernel layer

- Docker visualize only OS application layer
- VM visualize both layers

- Docker container is an instance of running image

### Image Versioning

- Technologies changes (i.e the versions of the tools used changes)
- New images need to be build as the above also changes
- Docker images are versioned
- Different versions are identified by `tags`
- `latest` tag mostly refers to the newest release

## Common Commands

- `docker images`: Displays all images available locally
- `docker ps`: showing/List running containers(running images)

### Pulling an Image from docker hub to locally

- Locate the container we want in docker hub e.g nginx
- Pick specific tag for the image (Using a specific version is best practice in most cases) e.g version 1.23
- To download the image
    - `docker pull {name}:{tag}`
    - `docker pull nginx:1.23`
- Without specifying the tag, the latest image is pulled by default
```bash
$ docker pull nginx:1.23
$ docker pull nginx
$ docker images
REPOSITORY      TAG     IMAGE ID    CREATED     SIZE
nginx           1.23    a99xxx      4 days ago  142MB
nginx           latest  a99xxx      4 days ago  142MB
```

### Running the image
- `docker run {name}:{tag}`
- Creates a container from given image and starts it
- Running the above command without tag, by default the image with latest tag will be runned or with `<none>` tag

- `-d` or `--detach`
- Runs container in background and prints the container ID
```bash
$ docker run -d nginx:1.23
```

- N/B: You may still want to see the logs, which can be useful for debugging etc while running in detach mode(in the background)
- `docker logs {container ID}`
- View logs from the service running inside the container. (which are present at the time of execution)
```bash
$ docker ps
$ docker logs xxxxxxx

# To stop running container in the background
$ docker stop {container} # Stop one or more running containers
```

- Running docker image not available locally; `docker run {image not available locally}`, by default docker will first pull the image and run it

### Container Port vs Host Port

- Application inside container runs in an `isolated Docker network`
- This allows us to run the same app running on the `same port multiple times`
- We need to `expose` the container port `to the host` (the machine the container runs on)
- `Port Binding`: Bind the container's port to the host's port to make the service available to the outside world.

- `-p` or `--publish`: Publish a container's port to the host
- `-p {HOST_PORT}:{CONTAINER_PORT}`
```bash
$ docker run -d -p 8000:80 nginx:1.23
```

### Note

- `docker run`: 
    - Creates a new container
    - Doesn't re-use previous container

- `docker ps -a` or `docker ps --all`
- Lists all containers (stopped and running)

- Running a stopped container without creating a new one
- `docker start {container}`: Start one or more stopped containers

- Commands such as `docker logs`, `docker start`, `docker stop` etc uses container ID, but can also use the `NAMES` of the container generated instead.

- `--name`: Assign a custom name to the container
```bash
$ docker run --name web-server -d -p 8000:80 nginx:1.23
```

## Dockerfile - Create own Images

- We need to create a `definition` of how to build an image from our application
- `Dockerfile` is a text document that contains commands to assemble an image
- Docker can then build an image by reading those instructions

### Example

- We will `write a Dockerfile` for flask application
- Then, `builed a Docker image` from it

#### Structure of Dockerfile

- Dockerfiles start from a parent image or `base image`
- It's a Docker image that your image is based on
    - You choose the base image, depending on which tools you need to have available
- Every image consists of mutliple image layers
- This makes Docker so efficient, because image layers can be cached etc

- `FROM`: Build this image from the specified image
- `RUN` : Will execute any command in a shell inside the container environment


#### Building a docker image

- `docker build {path}`: Builds a Docker image from a Dockerfile

##### Options provided

1. `-t` or `--tag`
    - Sets a name and optionallya tag in the `name:tag` format

## Author

- [waltertaya](https://github.com/waltertaya)

