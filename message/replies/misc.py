from modules.commonMethods import Reply

def misc(data):
    message = data['text']
    
    if "粥粥直播" in message:
        return Reply("https://live.bilibili.com/22298865")