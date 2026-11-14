# Jupyter Lab with Python 3.13 and all packages from requirements.txt.
# Build from the repo root (docker-compose.yml does this for you).
FROM python:3.13-slim

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Create user 'nina'
RUN useradd -m -u 1000 nina

# Install Python packages (the build context is the repo root)
COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt

USER nina
WORKDIR /home/nina/work

EXPOSE 8888

CMD ["jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--ServerApp.token=", "--ServerApp.password="]
