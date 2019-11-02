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

COPY ./code code
WORKDIR code

RUN adduser -d guru
USER guru

EXPOSE 5000
ENTRYPOINT ["python3"]
CMD ["app.py"]

# #Grab the latest alpine image
# FROM alpine:latest
#
# # Install python and pip
# RUN apk add --no-cache --update python3 py3-pip bash
# ADD ./webapp/requirements.txt /tmp/requirements.txt
#
# # Install dependencies
# RUN pip3 install --no-cache-dir -q -r /tmp/requirements.txt
#
# # Add our code
# ADD ./webapp /opt/webapp/
# WORKDIR /opt/webapp
#
# # Expose is NOT supported by Heroku
# # EXPOSE 5000
#
# # Run the image as a non-root user
# RUN adduser -D myuser
# USER myuser
#
# # Run the app.  CMD is required to run on Heroku
# # $PORT is set by Heroku
# CMD gunicorn --bind 0.0.0.0:$PORT wsgi
