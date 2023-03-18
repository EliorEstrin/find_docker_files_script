FROM python:3.9


# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

RUN apt-get update && apt-get install rsync -y


# Make port 8000 available to the world outside this container
EXPOSE 8000

# Run the Django application+
ENTRYPOINT [ "./entrypoint.sh" ]

