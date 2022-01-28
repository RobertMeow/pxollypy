from . import reg_signal


@reg_signal('sync')
def sync(**kwargs):
    db = kwargs['db']
    event_obj, event_msg = kwargs['event']['object'], kwargs['event']['message']

    if db.receive(f"SELECT COUNT(*) FROM conversations WHERE local_id = '{event_obj['chat_id']}'"):
        # db.save(f"UPDATE conversations SET peer_id = {event_obj['chat_uid']} WHERE local_id = '{event_obj['chat_id']}'")
        return '5'
    else:
        text, cmi, date, from_id = event_msg['text'], event_msg['conversation_message_id'], event_msg['date'], event_msg['from_id']
        peer_id = kwargs['vk'].get_peer_id(text, cmi, date, from_id)
        db.save(f"INSERT INTO conversations (peer_id, local_id) VALUES ({peer_id}, '{event_obj['chat_id']}')")
    return kwargs['event']['success']
