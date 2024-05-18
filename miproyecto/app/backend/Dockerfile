FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

# Install dependencies
RUN pip install pymysql sqlalchemy jinja2

# Copy application files
COPY . /app

# Set the working directory
WORKDIR /app
