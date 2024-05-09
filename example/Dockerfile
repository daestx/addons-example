# https://developers.home-assistant.io/docs/add-ons/configuration#add-on-dockerfile
ARG BUILD_FROM=ghcr.io/hassio-addons/debian-base/amd64:7.3.3
FROM $BUILD_FROM

# Execute during the build of the image
ARG BUILD_ARCH=amd64
RUN apt-get update && apt-get install -y --no-install-recommends \
    python3 \
    python3-pip \
    && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

#RUN python3 -m pip3 install urllib3

# Copy root filesystem
COPY rootfs /
