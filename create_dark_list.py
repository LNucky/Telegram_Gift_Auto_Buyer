from telethon.sync import TelegramClient, functions, types
from config import API_ID, API_HASH


def create_dark_list(client, file_name: str = 'dark_list'):
    """Creates a new dark_list using all existing gifts"""
    result = client(functions.payments.GetStarGiftsRequest(hash=0))
    
    with open(f'{file_name}.txt', 'w') as file:
        for gift in result.gifts:
            gift_data = gift.to_dict()
            file.write(f'{gift_data['id']}\n')


if __name__ == '__main__':
    with TelegramClient(api_id=API_ID, api_hash=API_HASH, session='session') as client:
        create_dark_list(client)