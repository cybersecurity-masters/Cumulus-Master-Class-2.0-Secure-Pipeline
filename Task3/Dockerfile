FROM masterclassregistry.azurecr.io/base-app:v3

COPY . .

RUN useradd -m appuser
USER appuser

CMD ["python", "app.py"]