FROM python:3.10-slim

ENV APP_HOME /app
WORKDIR $APP_HOME

COPY . .

# Copy service account credentials file
COPY dataanalytics-347914-bdf4c7ccb267.json /app/dataanalytics-347914-bdf4c7ccb267.json

RUN pip install --no-cache-dir -r requirements.txt

# Set environment variable for service account credentials file: for local testing
ENV GOOGLE_APPLICATION_CREDENTIALS=/app/dataanalytics-347914-bdf4c7ccb267.json

# Set a default PORT value
ENV PORT 8080

CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 main:app
