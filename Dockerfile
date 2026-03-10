FROM python:3.12-slim
WORKDIR /code
COPY pyproject.toml main.py /code/
COPY clients /code/clients
COPY core /code/core
RUN pip install --no-cache-dir --upgrade pip && pip install /code
EXPOSE 8080
CMD ["python", "-m", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]