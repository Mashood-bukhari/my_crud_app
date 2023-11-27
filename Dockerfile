# Use a Python base image
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Copy the entire project directory to the container
COPY . .

# Expose the port on which your Flask app runs (e.g., 5000)
EXPOSE 5000

# Define the command to run your Flask app
CMD ["python", "main.py"]
