# Set python version of docker image
FROM python:3.10.7

# Set working directory of image
WORKDIR /chatBot

# Copy necessary files and folders to the image
COPY src/ /chatBot/src
COPY config /chatBot/config
COPY app.py /chatBot/
COPY 07_Docker/requirements.txt chatBot/requirements.txt

# Install dependencies
RUN pip install --trusted-host pypi.python.org -r /chatBot/requirements.txt

# Run app.py when container launches
CMD [ "python", "app.py" ]