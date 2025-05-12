# Bruk et lett Python‐image
FROM python:3.10-slim

# Kopier notebook og requirements
WORKDIR /app
COPY . /app

# Installer Python-pakkene
RUN pip install --no-cache-dir -r requirements.txt

# Eksponer porten som Spaces bruker
EXPOSE 8080

# Start Voila uten browser
CMD ["voila", "--port=8080", "--no-browser", "--Voila.ip=0.0.0.0", "Logaritmisk.ipynb"]
