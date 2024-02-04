#!/bin/bash

docker run \
	-d \
	--rm \
	--env-file .env \
	cafe-uruguay:latest
