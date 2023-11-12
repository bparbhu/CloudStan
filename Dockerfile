# Use a Python 3.10 base image from the Python Docker Hub repository
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Set labels for metadata
LABEL authors="Brian Parbhu"

# Install system dependencies required for all Stan interfaces and additional tools
RUN apt-get update && apt-get install -y --no-install-recommends \
        build-essential \
        curl \
        ca-certificates \
        git \
        cmake \
        python3-dev \
        libeigen3-dev \
        && apt-get clean && rm -rf /var/lib/apt/lists/*

# Upgrade pip to the latest version
RUN pip install --upgrade pip

# Install the required Stan interfaces and their dependencies
# For CmdStanPy
RUN RUN pip install --upgrade cmdstanpy[all]
RUN python -m cmdstanpy.install_cmdstan

# For PyStan (Stan interface for Python, similar to CmdStanPy but different)
# PyStan requires httpstan, so it will be installed as a dependency
RUN pip install pystan

# For BridgeStan
RUN pip install bridgestan

# Install Dask, distributed, and Ray
RUN pip install dask distributed ray

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Install any other Python dependencies from your requirements.txt
RUN pip install -r requirements.txt

# Set environment variables for CmdStan location
ENV CMDSTAN=/root/.cmdstan/cmdstan-2.26.1
ENV CMDSTANPY_DIR=/usr/local/lib/python3.10/dist-packages/cmdstanpy
ENV AR=/usr/bin/ar

# Set the default command for the container
CMD ["python", "./your-daemon-or-script.py"]
