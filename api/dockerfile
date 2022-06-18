FROM python:3.9.1

WORKDIR /app

ENV FLASK_APP=app.py

#ENV FLASK_ENV=development

ENV FLASK_ENV=production

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

CMD [ "flask", "run", "--host", "0.0.0.0" ]
