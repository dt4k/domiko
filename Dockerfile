from python:3.6
RUN apt-get update && apt-get install opus-tools libav-tools -y
# RUN sudo apt-get -y install software-properties-common && add-apt-repository ppa:mc3man/trusty-media && apt-get update && apt-get -y install ffmpeg
COPY . /app/
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python", "domiko_client.py"]