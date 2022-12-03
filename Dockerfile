FROM python:3.9

COPY ./requirements.txt /requirements.txt

RUN pip install --no-cache-dir --upgrade -r /requirements.txt

COPY ./* /

COPY ./model/ ./model/

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]