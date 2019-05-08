FROM ubuntu:16.04
RUN apt-get update && apt-get install -y build-essential python-dev libmysqlclient-dev
RUN apt-get install -y python-mysqldb
ADD ./scripts /scripts
ENTRYPOINT ["python","/scripts/service_script.py"]
