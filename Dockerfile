FROM centos:latest
MAINTAINER Michael Lawrenson

RUN echo "==> Installing Base Dependencies" && \
    yum -y --setopt=tsflags=nodocs update && \
    yum -y --setopt=tsflags=nodocs install \
      epel-release python3-devel python3-pip && \
    yum clean all

RUN echo "==> Updating Python Core" && \
    python3 -m pip install --upgrade \
        pip wheel setuptools

ADD ./requirements.txt /tmp/requirements.txt
RUN pip3 install --no-cache-dir -q -r /tmp/requirements.txt

COPY src /opt/app
WORKDIR /opt/app

CMD gunicorn --bind 0.0.0.0:$PORT wsgi:application
