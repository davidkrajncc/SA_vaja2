FROM python:3.12

RUN apt-get update && apt-get install -y libgl1-mesa-glx

ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt
CMD ["python", "naloga2.py"]