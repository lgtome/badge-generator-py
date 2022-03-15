FROM python:3.10.2

WORKDIR /code

COPY . /code


RUN pip install --no-cache-dir -r requirements.txt


# COPY . .

CMD ["python3","./src/execute.py"]