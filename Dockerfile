FROM python:3.8-slim

RUN useradd --create-home --shell /bin/bash apiuser
WORKDIR /flask_api
COPY ./ .
RUN pip install -r requirements.txt
RUN chown -R apiuser:apiuser ./
USER apiuser

EXPOSE 5000
CMD ["python", "wsgi.py"]