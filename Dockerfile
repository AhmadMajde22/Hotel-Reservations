FROM python:slim

# Set environment variables to prevent bytecode and ensure proper buffering
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Set the working directory in the container
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    libgomp1 \
    libpq-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copy only the necessary files first (like requirements.txt)
COPY requirements.txt .

# Install Python dependencies (including psycopg2 or psycopg2-binary for PostgreSQL)
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project into the container
COPY . .

# Expose application port (assuming 5000)
EXPOSE 5000

# Set the entrypoint to run your application
CMD ["python", "application.py"]
