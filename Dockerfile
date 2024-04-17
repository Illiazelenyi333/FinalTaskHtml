# Specify the required Python version.
ARG PYTHON_IMAGE=python:3.12-alpine
FROM ${PYTHON_IMAGE}
ENV CAPITOL_PYTHON_EXECUTABLE=python3.12
EXPOSE 8000/tcp
# Required dependencies for compiling project's packages
RUN apk add --no-cache --virtual .build gcc libffi-dev musl-dev yaml-dev && \
    pip install --upgrade pip && \
    pip install setuptools && \
    apk del .build && \
    apk add git
# Create the working directory.
WORKDIR /usr/Website/
# Project files copy
COPY . .
# Install the project's dependencies.
RUN pip install -r requirements.txt
# Start
STOPSIGNAL SIGINT
ENTRYPOINT ["/bin/sh", "-c", "python3 src"]
