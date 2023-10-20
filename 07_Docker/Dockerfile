# Set python version of docker image
FROM python:3.10.7

# Set working directory of image
WORKDIR /chatBot

# Copy necessary files and folders to the image
COPY app.py /chatBot/
COPY static /chatBot/static
COPY templates /chatBot/templates
COPY 07_Docker/requirements.txt /chatBot/requirements.txt
COPY .env /chatBot/.env

# Install dependencies
RUN pip install --trusted-host pypi.python.org -r /chatBot/requirements.txt

# Set Flask environment variables
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Run flask application
CMD ["flask", "run"]
