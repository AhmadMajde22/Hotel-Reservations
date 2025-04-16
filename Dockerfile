FROM python:slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# Install dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    libgomp1 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copy project files into the container
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -e .

# (Optional) Run training pipeline here if needed
# RUN python pipeline/training_pipeline.py

# Expose application port (assuming 5000)
EXPOSE 5000

# Start application
CMD ["python", "application.py"]
