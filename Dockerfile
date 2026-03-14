FROM python:3.9

WORKDIR /app

COPY . .

RUN pip install boto3

CMD ["python", "lambda_function.py"]