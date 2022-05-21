from . import reg_signal
import requests


@reg_signal('chat_photo_update')
def chat_photo_update(**kwargs):
    vk = kwargs['vk']
    event_obj = kwargs['event']['object']
    url = vk.method('photos.getChatUploadServer', {'chat_id': kwargs['get_chat_uid'](event_obj['chat_id'], kwargs['db'])})['upload_url']
    response = requests.post(url, files=[('file', ('file.png', requests.get(event_obj['photo_url']).content))]).json()['response']
    vk.method('messages.setChatPhoto', {'file': response})
    return '1'
