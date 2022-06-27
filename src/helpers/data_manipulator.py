# Возвращает номер карты в формате для просмотра автоплатежа
def card_number_for_look_at_payment(number):
    first_format = number[0:6], '...', number[12:16]
    last_format = ''.join(first_format).replace(' ', '')

    return last_format


# Возвращает номер карты в скрытом формате для карт которые во вкладке "Мои карты"
def card_number_hidden(card):
    first_format = card[:4], ' ', card[4:6], '**', ' ', '****', ' ', card[12:16]
    last_format = ''.join(first_format)

    return last_format


# Возвращает номер телефона в формате +7 (707) 220 97 25 Ex.
def full_phone_number_format(phone):
    number = f'+7 ({str(phone[0:3])}) {str(phone[3:6])} {str(phone[6:8])} {str(phone[8:10])}'

    return number


# Возвращает номер телефона в формате для главной страницы +7 (707) 220 9725 Ex.

def full_phone_number_main_page(phone):
    number = f'+7 ({str(phone[0:3])}) {str(phone[3:6])} {str(phone[6:8])}{str(phone[8:10])}'

    return number
