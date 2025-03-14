# Python 3.9 tabanlı bir imaj kullan
FROM python:3.9

# Çalışma dizini oluştur
WORKDIR /app

# Bağımlılıkları yükle
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# API dosyasını kopyala
COPY . .

# Flask uygulamasını başlat
CMD ["python", "app.py"]