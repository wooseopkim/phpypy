# syntax=docker.io/docker/dockerfile:1.7-labs

ARG BASE=ghcr.io/astral-sh/uv:bookworm-slim
FROM $BASE AS base
WORKDIR /workspace
RUN apt update -y
# https://github.com/php/php-src/blob/2ebef11/README.md#building-php-source-code
RUN apt install -y pkg-config build-essential autoconf bison re2c libxml2-dev libsqlite3-dev
# https://github.com/swoole/phpy/blob/85c43cf/docs/en/python/build.md#compilation-dependencies
RUN apt install -y python3-dev git cmake

FROM base AS build
COPY ./php-src ./php-src
COPY ./scripts/compile_php .
RUN cd ./php-src && sh ../compile_php
COPY ./phpy ./phpy
COPY ./scripts/compile_phpy .
RUN cd ./phpy && sh ../compile_phpy

FROM scratch AS output
COPY --from=build /workspace/phpy/lib/phpy.so /
COPY --from=build /workspace/php-src/libs/libphp.so /

FROM base AS run
COPY --from=output /*.so .
COPY ./scripts/os_functions .
RUN . ./os_functions \
  && LIB_PATH="./lib/$(os_name)/$(os_arch)" \
  && mkdir -p "$LIB_PATH" \
  && mv ./*.so "$LIB_PATH"
ENV UV_FROZEN=true
COPY --exclude=phpy --exclude=php-src . .
RUN uv sync
