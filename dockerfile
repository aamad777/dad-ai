FROM python:3.10-slim

WORKDIR /app

# Copy and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the app code
COPY . .

# Expose Streamlit default port
EXPOSE 8501

# Start Streamlit properly
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]