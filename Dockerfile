FROM python:3.11-slim as builder

WORKDIR /src

COPY . /src

RUN pip3 install poetry && poetry build

FROM python:3.11-slim

WORKDIR /app

COPY main.py *.json /app/
COPY --from=builder /src/dist/devportal-*.whl /src/dist/devportal-*.tar.gz /app/

RUN pip3 install /app/devportal-*.whl && rm -rf /app/devportal-*

CMD ["python3", "/app/main.py"]
