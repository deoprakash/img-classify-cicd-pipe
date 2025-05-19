FROM python:3.12-slim

# Set the working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy everything from app/ into the current working directory (/app)
COPY app/ .

# Run the Flask app
CMD ["python", "app.py"]
