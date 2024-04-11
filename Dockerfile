FROM python:3.12

ADD . /code
WORKDIR /code
RUN apt-get update && apt-get install -y libgl1-mesa-glx \
    && pip install -r requirements.txt
CMD ["python", "naloga2.py"]
