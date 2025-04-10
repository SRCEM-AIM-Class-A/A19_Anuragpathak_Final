FROM python:3.9

# Don't buffer stdout/stderr and don't write .pyc files
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set working directory
WORKDIR /app

# Copy project files
COPY . .

# Install dependencies from requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Run migrations
RUN python manage.py migrate

# Run development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
