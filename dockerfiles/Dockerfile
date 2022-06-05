FROM python:3.9

WORKDIR /code

ADD ./src/requirements.txt /code/requirements.txt




RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./src /code/app

RUN py.test -vv

CMD ["uvicorn", "app.app:app", "--host", "0.0.0.0", "--port", "8000"]