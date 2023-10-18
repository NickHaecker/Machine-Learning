import subprocess

# Install pyspark using pip
subprocess.call(["pip", "install", "pyspark"])

# Upgrade PyDrive using pip
subprocess.call(["pip", "install", "-U", "-q", "PyDrive"])

# Install openjdk-8-jdk-headless using apt
subprocess.call(["apt", "install", "openjdk-8-jdk-headless", "-qq"])

# Set the JAVA_HOME environment variable
import os
os.environ["JAVA_HOME"] = "/usr/lib/jvm/java-8-openjdk-amd64"
