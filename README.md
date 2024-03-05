# Bumper

![License GPLv3](https://img.shields.io/github/license/bmartin5692/bumper.svg?color=brightgreen)
[![Python code quality, tests and docker deploy](https://github.com/60EightLabs/bumper/actions/workflows/ci.yml/badge.svg)](https://github.com/60EightLabs/bumper/actions/workflows/ci.yml)
[![CodeQL](https://github.com/60EightLabs/bumper/actions/workflows/codeql-analysis.yml/badge.svg)](https://github.com/60EightLabs/bumper/actions/workflows/codeql-analysis.yml)
[![codecov](https://codecov.io/gh/60EightLabs/bumper/graph/badge.svg?token=8N89730Z1S)](https://codecov.io/gh/60EightLabs/bumper)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/60EightLabs/bumper/dev.svg)](https://results.pre-commit.ci/latest/github/60EightLabs/bumper/dev)

---

- [Bumper](#bumper)
  - [Build Status](#build-status)
  - [Why?](#why)
  - [Compatibility](#compatibility)
    - [Ecovacs Home `>= 2.4.4`](#ecovacs-home--244)
  - [Documentation and Getting Started](#documentation-and-getting-started)
  - [Pre setup](#pre-setup)
  - [Basic configs for docker](#basic-configs-for-docker)
    - [Create `.env` file](#create-env-file)
      - [Example short `.env`](#example-short-env)
  - [Development](#development)
    - [Local run](#local-run)
    - [Code quality check](#code-quality-check)
  - [NOTES](#notes)
    - [clean logs](#clean-logs)
  - [References](#references)
  - [Thanks](#thanks)

---

**Forked from [edenhaus](https://github.com/edenhaus/bumper) -> [bmartin5692](https://github.com/bmartin5692/bumper) -> [MVladislav](https://github.com/MVladislav/bumper)**

---

Bumper is a standalone and self-hosted implementation of the central server used by Ecovacs vacuum robots.
Bumper allows you to have full control of your Ecovacs robots,
without the robots or app talking to the Ecovacs servers and transmitting data outside of your home.

![Bumper Diagram](./docs/images/BumperDiagram.png "Bumper Diagram")

**Note:** The current master branch is unstable, and in active development.

## Build Status

**Community:**
A Gitter community has been created for Bumper so users can chat and dig into issues outside of Github, join us here:
[![Gitter chat](https://badges.gitter.im/gitterHQ/gitter.png)](https://gitter.im/ecovacs-bumper/community)

**_Testing needed:_**
Bumper needs users to assist with testing in order to ensure compatibility as bumper moves forward!
If you've tested Bumper with your bot, please open an issue with details on success or issues.

**Please note:**
_this software is experimental and not ready for production use. Use at your own risk._

## Why?

For fun, mostly :)

But seriously, there are a several reasons for eliminating the central server:

1. Convenience: It works without an internet connection or if Ecovacs servers are down
2. Performance: No need for messages to travel to Ecovacs server and back.
3. Security: We can completely isolate the robot from the public Internet.

## Compatibility

As work to reverse the protocols and provide a self-hosted central server is still in progress,
Bumper has had limited testing. There are a number of EcoVacs models that it hasn't been tested against.
Bumper should be compatible with most wifi-enabled robots that use either the Ecovacs Android/iOS app
or the Ecovacs Home Android/iOS app, but has only been reported to work on the below:

| Model           | Protocol Used | Bumper Version Tested | EcoVacs App Tested                                                 |
| :-------------- | :------------ | :-------------------- | :----------------------------------------------------------------- |
| Deebot 900/901  | MQTT          | main                  | Ecovacs/Ecovacs Home                                               |
| Deebot 600      | MQTT          | main                  | Ecovacs Home                                                       |
| Deebot Ozmo 950 | MQTT          | main                  | Ecovacs Home                                                       |
| Deebot T10      | MQTT          | main                  | Ecovacs Home                                                       |
| Deebot X1 Omni  | MQTT          | main                  | [Discussions](https://github.com/MVladislav/bumper/discussions/51) |
| Deebot Ozmo 601 | XMPP          | main                  | Ecovacs                                                            |
| Deebot Ozmo 930 | XMPP          | main                  | Ecovacs/Ecovacs Home                                               |
| Deebot M81 Pro  | XMPP          | v0.1.0                | Ecovacs                                                            |

Tested with:

| Service                        | Version  | Bot         | Works | Info                                                                                                   |
| :----------------------------- | :------- | :---------- | :---- | :----------------------------------------------------------------------------------------------------- |
| Ecovacs Home                   | 2.2.1    | 930/950/T10 | Y     |                                                                                                        |
| Ecovacs Home                   | 2.4.1    | 930/950/T10 | Y     | Works best                                                                                             |
| Ecovacs Home                   | 2.4.3    | 930/950/T10 | Y     |                                                                                                        |
| Ecovacs Home                   | >= 2.4.4 |             | N     | [Will possible not work](https://docs.mitmproxy.org/stable/concepts-certificates/#certificate-pinning) |
| Deebot 4 Home Assistant        | 2.1.2    | 950/T10     | Y     |                                                                                                        |
| EcovacsBumper (Home Assistant) | 1.5.3    | 930         | Y     |                                                                                                        |

### Ecovacs Home `>= 2.4.4`

Possible not work for url's `jmq-ngiot-eu.dc.robotww.ecouser.net` and `a2JaaxoKXLq.iot-as-mqtt.cn-shanghai.aliyuncs.com`
as it seams they are [certificate-pinned](https://docs.mitmproxy.org/stable/concepts-certificates/#certificate-pinning).

## Documentation and Getting Started

See the documentation on [Read the Docs](https://bumper.readthedocs.io)

---

## Pre setup

To run this application certificate is needed, which will not auto generated.

You can provide the certificated by following ways:

Provide your own cert files and store them into:

- `certs/ca.crt`
- `certs/bumper.crt`
- `certs/bumper.key`

or generate them over a script:

```sh
$cd certs
$. ../scripts/create_cert.sh
```

## Basic configs for docker

### Create `.env` file

```env
# GENERAL variables (mostly by default, change as needed)
# ______________________________________________________________________________
NODE_ROLE=manager
NETWORK_MODE=overlay # by default "bridge"

# GENERAL sources to be used (set by default, change as needed)
# ______________________________________________________________________________
RESOURCES_LIMITS_CPUS=0.25
RESOURCES_LIMITS_MEMORY=250m
RESOURCES_RESERVATIONS_CPUS=0.001
RESOURCES_RESERVATIONS_MEMORY=32m

# APPLICATION version for easy update
# ______________________________________________________________________________
VERSION_BUMPER=develop
VERSION_NGNIX=1.25.2-alpine3.18-slim

# APPLICATION general variable to adjust the apps
# ______________________________________________________________________________
PUID=1000
PGID=1000
TZ=Europe/Berlin
BUMPER_ANNOUNCE_IP=<Insert your IP>
BUMPER_LISTEN=0.0.0.0
BUMPER_DEBUG_LEVEL=INFO
BUMPER_DEBUG_VERBOSE=2
DEBUG_LOGGING_API_REQUEST_ALL=false
DEBUG_LOGGING_API_REQUEST=false
DEBUG_LOGGING_XMPP_REQUEST=false

# BUILD variable
# ______________________________________________________________________________
PY_VERSION=3.12.2-alpine3.19
ALPINE_VERSION=3.19
```

#### Example short `.env`

```env
NETWORK_MODE=overlay
BUMPER_ANNOUNCE_IP=0.0.0.0 # replace with the server public ip
```

## Development

### Local run

> create with virtual env and run python project local

```sh
$python3 -m pip install virtualenv --break-system-packages
$python3 -m venv venv
$source ./venv/bin/activate
$python3 -m pip install .

$python3 -m bumper
```

### Code quality check

```sh
$python3 -m pip install virtualenv --break-system-packages
$python3 -m venv venv
$source ./venv/bin/activate
$python3 -m pip install -e .
$python3 -m pip install -e .[dev]

$clear && pre-commit run --all-files
$clear && pytest
```

or

```sh
$docker-compose -f dev.docker-compose.yaml build
$docker-compose -f dev.docker-compose.yaml run bumper

$clear && pytest
```

---

## NOTES

### clean logs

clean logs are accessible without credentials by url:

`https://portal-eu.ecouser.net/api/lg/image/<DID>d@<REPLACED>@<RESOURCE>`

---

## References

- <https://github.com/bmartin5692/bumper>
- <https://github.com/edenhaus/bumper>
- <https://github.com/MVladislav/bumper>
- <https://github.com/Yakifo/amqtt>

---

## Thanks

A big thanks to the original project creator @torbjornaxelsson, without his work this project would have taken much longer to build.

Bumper wouldn't exist without [Sucks](https://github.com/wpietri/sucks), an open source client for Ecovacs robots. Thanks to @wpietri and contributors!
