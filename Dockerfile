FROM python:3.12

RUN apt-get update \
    && apt-get install -y \
        libgl1-mesa-glx \
        libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt
CMD ["python", "naloga2.py"]