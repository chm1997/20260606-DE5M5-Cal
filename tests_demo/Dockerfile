FROM python:3.12-slim
WORKDIR /app
COPY calc.py /app
COPY calc_tests.py /app
ENTRYPOINT ["python3", "calc_tests.py"]