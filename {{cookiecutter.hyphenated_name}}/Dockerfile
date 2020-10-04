FROM python:3.8-slim

# Create app directory
WORKDIR /app

# Copy requiremnts file
COPY requirements.txt requirements.txt

# Install dependencies
RUN pip install -r requirements.txt

# Copies source code
COPY src /app

# Run your code
ENTRYPOINT ["python", "/app/app.py"]
