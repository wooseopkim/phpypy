FROM debian:bookworm-slim AS build

RUN apt update -y
RUN apt install -y python3-dev git cmake
# https://github.com/php/php-src/blob/2ebef11/README.md#building-php-source-code
RUN apt install -y pkg-config build-essential autoconf bison re2c libxml2-dev libsqlite3-dev

WORKDIR /workspace

COPY ./php-src ./php-src
COPY ./scripts/compile_php ./scripts/compile_php
RUN cd ./php-src && sh ../scripts/compile_php

COPY ./phpy ./phpy
COPY ./scripts/compile_phpy ./scripts/compile_phpy
RUN cd ./phpy && sh ../scripts/compile_phpy

FROM scratch AS output
COPY --from=build /workspace/phpy/lib/phpy.so /
COPY --from=build /workspace/php-src/libs/libphp.so /