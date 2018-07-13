from python:3.6
RUN echo "deb http://cz.archive.ubuntu.com/ubuntu trusty main multiverse" >> /etc/apt/sources.list
RUN apt-get update && apt-get install opus-tools unzip libav-tools open-jtalk open-jtalk-mecab-naist-jdic hts-voice-nitech-jp-atr503-m001 -y --allow-unauthenticated
RUN wget https://sourceforge.net/projects/mmdagent/files/MMDAgent_Example/MMDAgent_Example-1.6/MMDAgent_Example-1.6.zip/download -O MMDAgent_Example-1.6.zip && unzip MMDAgent_Example-1.6.zip MMDAgent_Example-1.6/Voice/* && cp -r MMDAgent_Example-1.6/Voice/mei/ /usr/share/hts-voice
COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt
COPY . /app
ENTRYPOINT ["python", "domiko_client.py"]