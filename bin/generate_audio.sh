word=$1
docker run -it --rm \
  -v "$(pwd)"/audios:/app/audios \
  --entrypoint "/usr/local/bin/python" \
  dtak1114/domiko:latest \
  lib/audio.py $word
