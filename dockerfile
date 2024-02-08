FROM python:3.11-bullseye

RUN apt update \
&& mkdir /SAS

WORKDIR /SAS


COPY src ./src
COPY commands ./commands
COPY requirements.txt ./requirements.txt

RUN python -m pip install --upgrade pip \
&& pip install -r ./requirements.txt

CMD ["bash"]