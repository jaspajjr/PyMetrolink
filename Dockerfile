FROM python:3.7

COPY container-entrypoint.sh /entry
RUN chmod 0755 /entry

COPY requirements.txt /data/requirements.txt
RUN pip install -r /data/requirements.txt

CMD ["start"]
ENTRYPOINT ["/entry"]

COPY metrolink /data