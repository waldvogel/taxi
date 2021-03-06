from settings import settings
from remote import ZebraRemote

class Pusher:
    def __init__(self, base_url, username, password):
        self.remote = ZebraRemote(base_url, username, password)

    def push(self, entries):
        self.remote.send_entries(entries)
