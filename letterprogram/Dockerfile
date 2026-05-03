FROM python:3.14-slim

WORKDIR /app

# Add jinja2 to the install list
RUN ["pip", "install", "fastapi", "uvicorn", "jinja2"]

COPY . .

EXPOSE 8000

CMD ["python", "-m", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]