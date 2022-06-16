from . import reg_signal


@reg_signal('chat_members')
def chat_members(**kwargs):
    return str(kwargs['vk'].method('messages.getChat', {'chat_id': kwargs['db'].get_chat_uid(kwargs['event']['object']['chat_id'])})['users'])
    