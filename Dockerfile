From python:3.8-alpine

#WORKDIR /app
#COPY app.py .
#CMD ["python", "app.py"]

#WORKDIR /app
#Add app.py .
#CMD ["python", "app.py"]

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /app
Add . .
EnTRYPOINT ["python"]
CMD ["app.py"]