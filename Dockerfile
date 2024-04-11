FROM python:3.12

RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /code

COPY . /code/

RUN pip install -r requirements.txt

CMD ["python", "naloga2.py"]
