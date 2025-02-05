# Usar una imagen base oficial de Python
FROM python:3.11-slim

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar los archivos del proyecto al contenedor
COPY . .

# Instalar dependencias del proyecto
RUN pip install --no-cache-dir -r requirements.txt

# Exponer el puerto en el que se ejecutará Flask
EXPOSE 5000

# Comando para iniciar la aplicación
CMD ["python", "app.py"]
