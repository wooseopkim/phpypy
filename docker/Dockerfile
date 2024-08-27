FROM debian:bookworm-slim AS build_php_src
RUN apt update
# https://github.com/php/php-src/blob/2ebef11/README.md#building-php-source-code
RUN apt install -y pkg-config build-essential autoconf bison re2c libxml2-dev libsqlite3-dev
WORKDIR /workspace
COPY ./php-src ./php-src
COPY ./scripts/compile_php ./scripts/compile_php
RUN cd ./php-src && sh ../scripts/compile_php

FROM debian:bookworm-slim AS build_phpy
RUN apt update
RUN apt install -y python3-dev git cmake
WORKDIR /workspace
COPY ./phpy ./phpy
COPY ./scripts/compile_phpy ./scripts/compile_phpy
RUN cd ./phpy && sh ../scripts/compile_phpy

FROM build AS run
COPY ./scripts ./scripts
RUN . ./scripts/os_functions \
  && LIB_PATH=./lib/$(os_name)/$(os_arch) \
  && mkdir -p $LIB_PATH \
  && mv /workspace/phpy/lib/phpy.so $LIB_PATH \
  && mv /workspace/php-src/libs/libphp.so $LIB_PATH
RUN apt install -y pipenv
COPY Pipfile* .
RUN pipenv sync --dev --python $(which python3)
COPY . .

FROM scratch AS output
COPY --from=build_phpy /workspace/phpy/lib/phpy.so /
COPY --from=build_php_src /workspace/php-src/libs/libphp.so /
