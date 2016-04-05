FROM python:2-onbuild

EXPOSE 8080

CMD ["uwsgi", "--http", ":8080", "--wsgi-file", "wsgi.py"]
