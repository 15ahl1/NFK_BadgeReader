#!/bin/sh
# Installs and sets up all prerequisites for the raspberry pi client, needs to run with sudo

apt-get update && apt-get upgrade -y  # Update the system before we do anything

# Install pre-requisite packages
PACKAGES="python3-setuptools pigpio python-pigpio python3-pigpio"
apt-get install $PACKAGES -y

# Run pigpiod and add it to startup
systemctl enable pigpiod
pigpiod

# Code to update the boot script to run the program on startup

