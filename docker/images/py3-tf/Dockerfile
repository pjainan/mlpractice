FROM python:3.6

#RUN python --version
#RUN pip --version
#RUN virtualenv --version

RUN apt-get update -y
RUN apt-get install -y git

# update pip
WORKDIR /remote
VOLUME /remote
ENV REPO ""


RUN pip install pip --upgrade
RUN pip install wheel
RUN pip install -U pip virtualenv
RUN virtualenv --system-site-packages -p python ./tensorflow && \
    sh ./tensorflow/bin/activate && \
    pip install --upgrade pip && \
    pip install --upgrade numpy && \
    pip install --upgrade scipy && \
    pip install --upgrade matplotlib && \
    pip install --upgrade pandas && \
    pip install --upgrade sklearn && \
    pip install --upgrade scikit-image && \
    pip install --upgrade tensorflow && \
    pip install --upgrade keras && \
    pip list
