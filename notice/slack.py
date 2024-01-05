from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError


class Slack:
    def __init__(self, slack_token: str, slack_channel: str):
        self.token = slack_token
        self.channel = slack_channel

    def post(self, text: str) -> None:
        slack_client = WebClient(token=self.token)
        try:
            _ = slack_client.chat_postMessage(
                channel=self.channel,
                text=text,
            )
        except SlackApiError as e:
            raise Exception(f"error posting message: {e}")
