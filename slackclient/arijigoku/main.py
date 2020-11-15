import slack
import localenv

@slack.RTMClient.run_on(event='message')
def fortune(**payload):
    data = payload['data']
    web_client = payload['web_client']
    # textはreplyなどには含まれないので、subtypeがなし=親メッセージかを確認する
    if 'subtype' in data and data['subtype'] == "channel_leave":
        web_client.channels_invite(
            channel=data['channel'],
            user=data['user'],
        )
    print("ignore")

slack_token = localenv.SLACK_API_TOKEN
rtm_client = slack.RTMClient(token=slack_token)
rtm_client.start()