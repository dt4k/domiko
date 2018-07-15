# domiko

# Build & Run

This application requires several auth tokens as env variables.
Docker image is also available on dockerhub.

```
docker run -it --rm \
  -e DISCORD_TOKEN=${your_discord_token_for_your_bot} \
  -e VOICE_CHATROOM_ID=${discord_room_id_for_voice_chat_room} \
  -e GENERAL_CHANNEL_ID=${discord_room_id_to_post_text_message} \
  -e BLYNK_TOKEN=${token_for_your_blynk_app} \
  dtak1114/domiko:latest
```
