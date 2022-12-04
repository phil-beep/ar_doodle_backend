FROM python:3.9

RUN python3 -m venv venv

COPY ./requirements.txt /requirements.txt

RUN . /venv/bin/activate && pip install --no-cache-dir -r /requirements.txt

COPY ./* /

COPY ./model/ ./model/

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]