FROM python:3.9.5-slim-buster
RUN apt update -y && apt install awscli -y
WORKDIR / app
COPY . / app

RUN  pip install -r requirements.txt
RUN pip install --upgrade accelerate
RUN pip uninstall -y transformers accelerate
RUN pip install transformers accelerate

EXPOSE $PORT
CMD ["python3", "app.py"]
