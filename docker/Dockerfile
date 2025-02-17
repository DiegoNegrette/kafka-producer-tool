FROM python:3.9-slim

ARG APP_USER="app"
ARG APP_GROUP="app"

ENV \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONFAULTHANDLER=1

WORKDIR /code

# Copy requirements
COPY requirements/common.txt requirements/constraints.txt requirements/development.txt /code/requirements/

# Install dependencies
RUN python -m pip install --upgrade pip setuptools wheel
RUN python -m pip install --no-cache-dir -r /code/requirements/constraints.txt
# RUN python -m pip install --no-cache-dir -r /code/requirements/common.txt
# RUN python -m pip install --no-cache-dir -r /code/requirements/development.txt

# Create a non-root user
RUN addgroup --system ${APP_GROUP} --gid 1000 && \
    adduser --system ${APP_USER} \
    --ingroup ${APP_GROUP} \
    --shell /usr/sbin/nologin \
    --uid 1000 \
    --home /code

# Copy application source code
COPY src/ /code/

# Switch to the non-root user
USER ${APP_USER}

# Start the application
CMD ["python", "app.py"]
