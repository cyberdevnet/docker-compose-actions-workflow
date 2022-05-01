FROM python:3.9

WORKDIR /code

ADD ./requirements.txt /code/requirements.txt




RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY . /code/app


CMD ["uvicorn", "app.app:app", "--host", "0.0.0.0", "--port", "8081"]