FROM python:3.11-alpine
EXPOSE 8000
WORKDIR /app

RUN pip3 install -r app/requirements.txt --no-cache-dir
ENTRYPOINT [ "python3" ]
CMD [ "app/manage.py" "runserver", "0.0.0.0:8000"]
