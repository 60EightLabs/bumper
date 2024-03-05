ARG ARCH=amd64
# https://hub.docker.com/_/python/tags
ARG PY_VERSION=3.12.2-alpine3.19
# https://hub.docker.com/_/alpine/tags
ARG ALPINE_VERSION=3.19
FROM ${ARCH}/python:${PY_VERSION}

LABEL org.opencontainers.image.source=https://github.com/60EightLabs/bumper
LABEL org.opencontainers.image.description="bumper"
LABEL org.opencontainers.image.licenses=GPLv3


RUN apk add --no-cache bash git openssl

WORKDIR /bumper
COPY . .

RUN pip3 install .

EXPOSE 443
EXPOSE 5223
EXPOSE 8007
EXPOSE 8883

# Setup entrypoint
ENTRYPOINT ["python3", "-m", "bumper"]
