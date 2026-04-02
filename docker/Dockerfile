FROM ubuntu:22.04

ARG GID
ARG UID

# skip user interaction for apt-get
ENV DEBIAN_FRONTEND=noninteractive

SHELL ["/bin/bash", "-c"]

# install required packages
RUN <<EOF
	apt-get -y update

	apt-get -y upgrade

	apt-get install -y --no-install-recommends \
		build-essential libncurses-dev bc \
		flex bison libssl-dev \
		libelf-dev gcc-aarch64-linux-gnu \
		python3 python3-pip
EOF

# having a mix between user-owned and root-owned files in
# the working directory can cause trouble (e.g. you won't
# be able to delete root-owned files, kernel compilation
# might fail, etc...). Thus, create a user matching that
# from the host and switch to it. At this point, there
# shouldn't be a need to run anything else as root anyways.
RUN groupadd -g $GID lkss && useradd -u $UID -g $GID -m lkss

USER lkss

# create and switch to the working directory
WORKDIR /home/lkss

# copy required files
COPY ../requirements.txt ./requirements.txt

# install required python packages
RUN pip install -r requirements.txt
