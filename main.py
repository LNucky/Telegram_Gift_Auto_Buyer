from telethon.sync import TelegramClient, functions, types
from config import API_ID, API_HASH, MY_CHANNEL_ID, MIN_SUPPLY, MAX_SUPPLY, MIN_PRICE, MAX_PRICE, CYCLES
from time import sleep

# cheapest_gift_id = '5170145012310081615' # for tests
print(type(MIN_PRICE))
    
def buy_gift(client, channel_id: int, gift_id: int):
    peer = client.get_input_entity(channel_id)

    invoice = types.InputInvoiceStarGift(
        peer=peer,
        gift_id=gift_id,
        hide_name=False,
    )
    payment_form = client(functions.payments.GetPaymentFormRequest(invoice=invoice))
    form_id = payment_form.form_id

    result = client(functions.payments.SendStarsFormRequest(
        form_id=form_id,
        invoice=invoice
    ))
    return result


def check_new_gifts(client) -> list[dict]:
    new_gifts = []
    result = client(functions.payments.GetStarGiftsRequest(hash=0))
    with open('dark_list.txt', 'r') as file:
        dark_list = file.read().splitlines()
    # print("Dark List:")
    # print(dark_list)
    for gift in result.gifts:
        gift_data = gift.to_dict()
        gift_id = gift_data['id']
        if not str(gift_id) in dark_list:
            new_gifts.append(gift_data)
    print(f'Available gifts: {len(new_gifts)}')
    return new_gifts


def create_dark_list(client, file_name: str = 'dark_list'):
    """Creates a new dark_list using all existing gifts"""
    result = client(functions.payments.GetStarGiftsRequest(hash=0))
    
    with open(f'{file_name}.txt', 'w') as file:
        for gift in result.gifts:
            gift_data = gift.to_dict()
            file.write(f'{gift_data['id']}\n')


def gift_filter(gift_data: dict, 
                min_supply: int,
                max_supply: int,
                min_price: int, 
                max_price: int) -> bool:
    if not gift_data['limited']:
        return False
    
    gift_supply = gift_data['availability_total']
    gift_price = gift_data['stars']
    if (min_supply <= gift_supply <= max_supply) and (min_price <= gift_price <= max_price):
        return True
    return False


def main():
    with TelegramClient(api_id=API_ID, api_hash=API_HASH, session='session') as client:
        tries = 0
        monitor = True
        while monitor:
            new_gifts = check_new_gifts(client)
            if new_gifts:
                print(f'{len(new_gifts)} new gifts were found')
                for cycle in range(int(CYCLES)):
                    for gift_data in new_gifts:
                        print(gift_data['id'])
                        if gift_filter(gift_data, int(MIN_SUPPLY), int(MAX_SUPPLY), int(MIN_PRICE), int(MAX_PRICE)):
                            gift_id = gift_data['id']
                            buy_gift(client, MY_CHANNEL_ID, gift_id)
                            print(f'Bought a gift: {gift_data['id']}\n'
                                f'supply: {gift_data['availability_total']}\n'
                                f'price: {gift_data['stars']}\n')
                        else:
                            print('There are no filter-available gifts')
                monitor = False
            tries += 1
            print(f'Try {tries}')
            sleep(1)

if __name__ == '__main__':
    main()

#todo: сделать цикл с настраиваемым в конфиге количеством итераций и обернуть в него покупку подарков
#todo: обернуть установку сессии в while True + try/except на случай проблем/блоков API
#todo: придумать и сделать безопасный режим запуска при отсутствии dark list'а
#todo: добавить возможность настройки задержки