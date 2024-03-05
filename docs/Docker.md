# Docker

To download the image from Docker Hub you can run the following:

`docker pull docker pull ghcr.io/60eightlabs/bumper:develop`

[View Bumper on GHCR](https://github.com/60EightLabs/bumper/pkgs/container/bumper)

## Docker-compose

Run the complete project with docker-compose.

The docker-compose starts two services:

- bumper itself
- nginx proxy, which redirects MQTT traffic on port `443` to port `8883`

The redirection is required as the app v2+ and robots with a newer firmware
are connecting to the mqtt server on port 433.

### default mode

create `.env` file:

> for more detailed version check main `README.md`

```env
BUMPER_ANNOUNCE_IP=0.0.0.0 # replace with the server public ip
```

than run:

```sh
$docker-compose up -d
```

### swarm mode

create `.env` file:

> for more detailed version check main `README.md`

```env
NETWORK_MODE=overlay
BUMPER_ANNOUNCE_IP=0.0.0.0 # replace with the server public ip
```

than run:

```sh
$docker-swarm-compose: aliased to DOCKER_BUILDKIT=1 docker compose config | sed '1{/^name:/d}' | sed 's/published: "\(.*\)"/published: \1/' | DOCKER_BUILDKIT=1 CONFIG_VERSION=1 docker stack deploy --resolve-image=never --with-registry-auth --compose-file -
```

## Build a Docker image

To build the docker image yourself you can run the following:
`docker build -t 60eightlabs/bumper .`

This requires Docker 17.09 or newer, but has also been tested with podman.

## Docker usage

To run the image in docker some environment settings and port mappings are required:

**Ports Required: (-p)**

- 443 - `-p 443:443`
- 8007 - `-p 8007:8007`
- 8883 - `-p 8883:8883`
- 5223 - `-p 5223:5223`

**Environment Settings: (-e)**

`BUMPER_ANNOUNCE_IP` should be used so the actual host IP is reported to bots that checkin.

- BUMPER_ANNOUNCE_IP - `-e "BUMPER_ANNOUNCE_IP=X.X.X.X"`

**Volume Settings: (-v)**

Optionally you can map existing directories for logs, data, and certs.

- data/logs/certs
- Data - `-v /home/user/bumper/data:/bumper/data`

**Full Example:**

```sh
$docker run -it -e "BUMPER_ANNOUNCE_IP=X.X.X.X" -p 443:443 -p 8007:8007 -p 8883:8883 -p 5223:5223 -v /home/user/bumper/data:/bumper/data --name bumper 60eightlabs/bumper
```
