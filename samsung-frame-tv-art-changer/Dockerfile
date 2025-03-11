ARG BUILD_FROM
FROM $BUILD_FROM

# Install dependencies
RUN \
  apk add --no-cache \
    python3 py3-pip git curl tar

# Install Python dependencies
RUN \
    pip3 install git+https://github.com/NickWaterton/samsung-tv-ws-api.git pillow --break-system-packages

# Copy data for add-on
COPY run.sh /
COPY *.py /
RUN mkdir -p /sources/
COPY sources/*.py /sources/
RUN mkdir -p /utils/
COPY utils/*.py /utils/

RUN chmod a+x /run.sh

CMD [ "/run.sh" ]
