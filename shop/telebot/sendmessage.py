import requests
from .models import TeleSettings


def send_telegram(tg_name, tg_phone, tg_order):
    if TeleSettings.objects.get(pk=1):
        settings = TeleSettings.objects.get(pk=1)
        token = str(settings.tg_token)
        chat_id = str(settings.tg_chat)
        text = str(settings.tg_message)
        api = 'https://api.telegram.org/bot'
        method = api + token + '/sendMessage'

        if text.find('{') and text.find('}') and text.rfind('{') and text.rfind('}'):
            part_1 = text[0:text.find('{')]
            part_2 = text[text.find('}') + 1:text.find('{', 2)]
            part_4 = text[text.find('}', 2) + 1:text.find('{', 3)]
            part_3 = text[text.rfind('}'):-1]

            text_slice = part_1 + "Mijoz ismi: " + tg_name + part_2 + "\nTelefon raqami: " + tg_phone + part_4 + "\nBuyurtma:" + tg_order + part_3
        else:
            text_slice = text
        req = None
        try:
            req = requests.post(method, data={
                'chat_id': chat_id,
                'text': text_slice
            })
        except:
            pass
        finally:
            if req.status_code != 200:
                print('Yuborishda xatolik!')
            elif req.status_code == 500:
                print('500 Xatolik')
            else:
                print("Hamasi OK habar yuborildi!")