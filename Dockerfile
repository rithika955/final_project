# Use a Python base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy all files from the local directory to the container's working directory
COPY . .

# Install dependencies
RUN pip install -r requirements.txt

# Install Jupyter Notebook (if required)
RUN pip install notebook

# Expose the port for Jupyter Notebook (or Flask if that's what you're using)
EXPOSE 5000

# Command to run the Flask app
CMD ["python", "app.py"]
