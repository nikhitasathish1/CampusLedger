# Use an official Python runtime as a parent image
FROM python:3.12

# Set the working directory inside the container
WORKDIR /app

# Copy only requirements first (for caching layers)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project files
COPY . .

# Expose port 8000 for the Django application
EXPOSE 8000

# Run migrations and start the application
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "dcrm.wsgi:application"]
