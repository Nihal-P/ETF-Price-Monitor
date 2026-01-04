# smaller python base image
From python:3.11-slim 

# create a directory inside the container
WORKDIR /app

# copy requirements first
COPY requirements.txt .

# install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# copy backend application code
COPY . .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

