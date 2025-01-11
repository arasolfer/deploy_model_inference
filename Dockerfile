# Use an artificial python image
FROM python:3.11-slim

# Install system dependencies (necessary for building some packages)
RUN apt-get update && apt-get install -y build-essential libpq-dev

# Install poetry
RUN pip install poetry

# Set the working directory
WORKDIR /app

# Copy poetry files
COPY pyproject.toml poetry.lock /app/

# Install dependencies
RUN poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi

# Copy the rest of the project files
COPY . /app

# Command to run the inference script
CMD ["poetry", "run", "python", "src/model/inference.py"]
