FROM python:3.11-rc-alpine
COPY hi.py /code/
WORKDIR /code/
ENTRYPOINT [ "python", "hi.py", "-pworld" ]
