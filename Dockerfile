FROM apache/superset:4.1.1

USER root

# Instalar dependencias
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copiar configuración
COPY superset_config.py /app/pythonpath/superset_config.py

# Ajustar permisos
RUN chmod 644 /app/pythonpath/superset_config.py

USER superset
