# Python 3.13 slim-based
FROM python:3.13-slim

WORKDIR /ai-booking


# Copy the requirements.txt file first
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project files
COPY . .

# Expose port 8000
EXPOSE 8000

# Use uvicorn to run the FastAPI app
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
