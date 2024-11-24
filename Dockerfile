# Use the official Python image as a base
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the Streamlit app and dataset to the container
COPY netflixapp.py /app/
COPY netflix_titles.csv /app/

# Install required Python packages
RUN pip install --no-cache-dir streamlit pandas

# Expose the Streamlit port
EXPOSE 8501

# Command to run the Streamlit app
CMD ["streamlit", "run", "netflixapp.py", "--server.port=8501", "--server.address=0.0.0.0"]
