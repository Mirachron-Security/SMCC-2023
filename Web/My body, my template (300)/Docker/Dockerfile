FROM python:3.7-alpine

RUN pip install flask && mkdir /app
#RUN echo "flag{Server_Side_Template_Injection_is_4_cool_kids_only}" > /flag.txt
COPY app.py /app
WORKDIR /app

ENTRYPOINT ["python"]
CMD ["app.py"]
