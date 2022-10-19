# Pull base image
FROM python:3.10.8

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# ENV PYTHONPATH "${PYTHONPATH}:/app"

WORKDIR /project

# Install dependencies
RUN pip install pipenv
COPY Pipfile Pipfile.lock /project/
RUN pipenv install --system --dev

COPY . .

EXPOSE 8000