import os,json
from langchain_core.messages import message_to_dict,messages_from_dict,BaseMessage, messages_to_dict
from langchain_core.chat_history import BaseChatMessageHistory
from typing import Sequence

def get_history(session_id):
    return FileChatMessageHistory(session_id,"./chat_history")


class FileChatMessageHistory(BaseChatMessageHistory):

    def __init__(self,session_id,storage_path):
        self.session_id = session_id
        self.storage_path = storage_path
       
        self.file_path = os.path.join(storage_path,self.session_id)

        os.makedirs(os.path.dirname(self.file_path),exist_ok=True)

    def add_messages(self,messages: Sequence[BaseMessage]) -> None:

        all_messages = list(self.messages)
        all_messages.extend(messages)
        
        #save all messages to file
        new_messages = [message_to_dict(message) for message in all_messages]
        with open(self.file_path, "w", encoding="utf-8") as f:
            json.dump(new_messages, f, ensure_ascii=False)

    @property
    def messages(self) -> list[BaseMessage]:
        try:
            with open(self.file_path, "r", encoding="utf-8") as f:
                messages = json.load(f)
            return messages_from_dict(messages)
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            return []

    def clear(self) -> None:
        with open(self.file_path, "w", encoding="utf-8") as f:
            json.dump([], f, ensure_ascii=False)