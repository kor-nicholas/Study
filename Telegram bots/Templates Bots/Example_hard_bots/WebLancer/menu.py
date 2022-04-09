import telebot
from telebot import types
import sqlite3, db

main_menu = types.InlineKeyboardMarkup(row_width=3)
main_menu.add(
    types.InlineKeyboardButton(text='🛒 Товары', callback_data='shop'),
    types.InlineKeyboardButton(text='💵 Баланс', callback_data='balance'),
    types.InlineKeyboardButton(text='👕 Профиль', callback_data='profile')
)
main_menu.add(
    types.InlineKeyboardButton(text='⁉️ Инструкция', callback_data='faq'),
    types.InlineKeyboardButton(text='🔴 Информация', callback_data='info')
)
main_menu.add(types.InlineKeyboardButton(text='🤵 Тех. Поддержка', url='https://t.me/mr_towel'))
main_menu.add(types.InlineKeyboardButton(text='🔹 Реферальная система', callback_data='ref_system'))
main_menu.add(types.InlineKeyboardButton(text='⭐️ Наличие', callback_data='naluser'))

adm_main_menu = types.InlineKeyboardMarkup(row_width=3)
adm_main_menu.add(
    types.InlineKeyboardButton(text='🛒 Товары', callback_data='shop'),
    types.InlineKeyboardButton(text='💵 Баланс', callback_data='balance'),
    types.InlineKeyboardButton(text='👕 Профиль', callback_data='profile')
)
adm_main_menu.add(
    types.InlineKeyboardButton(text='⁉️ Инструкция', callback_data='faq'),
    types.InlineKeyboardButton(text='🔴 Информация', callback_data='info')
)
adm_main_menu.add(types.InlineKeyboardButton(text='🤵 Тех. Поддержка', url='https://t.me/mr_towel'))
adm_main_menu.add(types.InlineKeyboardButton(text='🔹 Реферальная система', callback_data='ref_system'))
adm_main_menu.add(
    types.InlineKeyboardButton(text='🟢📊 Статистика 📊🟢', callback_data='stat'),
    types.InlineKeyboardButton(text='🟢🔰 Админ меню 🔰🟢', callback_data='exit_to_adm_menu')
)
adm_main_menu.add(types.InlineKeyboardButton(text='⭐️ Наличие', callback_data='nal'))

kur_main_menu = types.InlineKeyboardMarkup(row_width=3)
kur_main_menu.add(
    types.InlineKeyboardButton(text='🛒 Товары', callback_data='shop'),
    types.InlineKeyboardButton(text='💵 Баланс', callback_data='balance'),
    types.InlineKeyboardButton(text='👕 Профиль', callback_data='profile')
)
kur_main_menu.add(
    types.InlineKeyboardButton(text='⁉️ Инструкция', callback_data='faq'),
    types.InlineKeyboardButton(text='🔴 Информация', callback_data='info')
)
kur_main_menu.add(types.InlineKeyboardButton(text='🤵 Тех. Поддержка', url='https://t.me/mr_towel'))
kur_main_menu.add(types.InlineKeyboardButton(text='🔹 Реферальная система', callback_data='ref_system'))
kur_main_menu.add(
    types.InlineKeyboardButton(text='📊 Статистика', callback_data='stat'),
    types.InlineKeyboardButton(text='🔰 Меню курьера', callback_data='exit_to_kur_menu')
)
kur_main_menu.add(types.InlineKeyboardButton(text='⭐️ Наличие', callback_data='nalkur'))

def replenish_balance():
    replenish_balance = types.ReplyKeyboardRemove()
    replenish_balance = types.InlineKeyboardMarkup()
    if db.get_value('need_kuna') == 1:
        replenish_balance.add(types.InlineKeyboardButton(text="🏪 Kuna Code", callback_data="kuna_code"))
    if db.get_value('need_ltc') == 1:
        replenish_balance.add(types.InlineKeyboardButton(text="♦️ LiteCoin", callback_data="aperon_code"))
    if db.get_value('need_btc') == 1:
        replenish_balance.add(types.InlineKeyboardButton(text="⚜️ BitCoin", callback_data="BitCoin"))
    if db.get_value('need_btc_c') == 1:
        replenish_balance.add(types.InlineKeyboardButton(text="🔱 BitCoin (CASH)", callback_data="bitcoin_cash"))
    if db.get_value('need_qiwi') == 1:
        replenish_balance.add(types.InlineKeyboardButton(text='💳 Qiwi', callback_data='qiwi_money'))
    if db.get_value('need_easypay') == 1:
        replenish_balance.add(types.InlineKeyboardButton(text='💵 EasyPay', callback_data='easypay_money'))
    if db.get_value('need_global24') == 1:
        replenish_balance.add(types.InlineKeyboardButton(text='🌐 GlobalMoney', callback_data='global24_money'))
    if db.get_value('need_promo') == 1:
        replenish_balance.add(types.InlineKeyboardButton(text='♻️Активировать промокод', callback_data='promo'))

    replenish_balance.add(types.InlineKeyboardButton(text='↩️ В меню', callback_data='exit_to_menu'))

    return replenish_balance


kuna_code = types.InlineKeyboardMarkup(row_width=3)
kuna_code.add(
    types.InlineKeyboardButton(text='❌ Отменить', callback_data='exit_to_menu')
)

aperon_code = types.InlineKeyboardMarkup(row_width=3)
aperon_code.add(
    types.InlineKeyboardButton(text='🔵 Проверить', callback_data='check_aperon_money'),
    types.InlineKeyboardButton(text='❌ Отменить', callback_data='exit_to_menu')
)

btс = types.InlineKeyboardMarkup(row_width=3)
btс.add(
    types.InlineKeyboardButton(text='🔵 Проверить', callback_data='check_bitcoin_payments_method'),
    types.InlineKeyboardButton(text='❌ Отменить', callback_data='exit_to_menu')
)
bitcoin_cash = types.InlineKeyboardMarkup(row_width=3)
bitcoin_cash.add(
    types.InlineKeyboardButton(text='🔵 Проверить', callback_data='check_bch_payments_method'),
    types.InlineKeyboardButton(text='❌ Отменить', callback_data='exit_to_menu')
)

qiwi_money = types.InlineKeyboardMarkup(row_width=3)
qiwi_money.add(
    types.InlineKeyboardButton(text='🔵 Проверить', callback_data='check_qiwi_money'),
    types.InlineKeyboardButton(text='❌ Отменить', callback_data='exit_to_menu')
)
easypay_check = types.InlineKeyboardMarkup()
easypay_check.add(
    types.InlineKeyboardButton(text='🔵 Проверить', callback_data='easypay_check'),
    types.InlineKeyboardButton(text='❌ Отменить', callback_data='exit_to_menu')
)

global24_check = types.InlineKeyboardMarkup()
global24_check.add(
    types.InlineKeyboardButton(text='🔵 Проверить', callback_data='global24_check'),
    types.InlineKeyboardButton(text='❌ Отменить', callback_data='exit_to_menu')
)

ref_system_standart = types.InlineKeyboardMarkup()
ref_system_standart.add(
    types.InlineKeyboardButton(text='✏ Изменить ссылку', callback_data='change_ref_code'),
    types.InlineKeyboardButton(text='🔺 Назад в меню', callback_data='exit_to_menu')
)
ref_system = types.InlineKeyboardMarkup()
ref_system.add(
    types.InlineKeyboardButton(text='✏ Изменить ссылку', callback_data='change_ref_code'),
    types.InlineKeyboardButton(text='🔄 Сбросить ссылку', callback_data='drop_ref_code')
)
ref_system.add(types.InlineKeyboardButton(text='↩️ Назад в меню', callback_data='exit_to_menu'))

faq = types.InlineKeyboardMarkup()
faq.add(
    types.InlineKeyboardButton(text='🌎 EasyPay', callback_data='help_easypay'),
    types.InlineKeyboardButton(text='🌐 KunaCode', callback_data='help_kunacode')
)
faq.add(types.InlineKeyboardButton(text='↩️ В главное меню', callback_data='exit_to_menu'))

adm_menu = types.InlineKeyboardMarkup()
adm_menu.add(types.InlineKeyboardButton(text='🔐 Управление магазином', callback_data='shop_config'))
adm_menu.add(types.InlineKeyboardButton(text='✏️ Настройки пользователей', callback_data='users_config'))
adm_menu.add(types.InlineKeyboardButton(text='💰 Настройки плат.систем', callback_data='payments_config'))
adm_menu.add(types.InlineKeyboardButton(text='✳️ Добавить промокод', callback_data='add_promo'))
adm_menu.add(types.InlineKeyboardButton(text='⚙️Настройка Apirone', callback_data='change_ltc_wallet'))
adm_menu.add(types.InlineKeyboardButton(text='💬 Рассылка', callback_data='sending_msg'))
adm_menu.add(types.InlineKeyboardButton(text='❌ Выйти', callback_data='exit_to_menu'))

kur_menu = types.InlineKeyboardMarkup()
kur_menu.add(types.InlineKeyboardButton(text='🔐 Управление магазином', callback_data='shop_config1'))
kur_menu.add(types.InlineKeyboardButton(text='💬 Рассылка', callback_data='sending_msg_kur'))
kur_menu.add(
    types.InlineKeyboardButton(text='↩️ Выйти', callback_data='exit_to_menu')
)

payments_config = types.InlineKeyboardMarkup(row_width=1)
payments_config.add(
    types.InlineKeyboardButton(text='📎Добавление\\удаление кошельков', callback_data='add_remove_payments'),
    types.InlineKeyboardButton(text='▶Включение\\выключение плат.систем', callback_data='on_off_payments'),
    types.InlineKeyboardButton(text='↩Назад', callback_data='exit_to_adm_menu')
)


def on_off_payments():
    if db.get_value('need_kuna') == 1:
        kuna_text = '🟢Выключить KUNA-Code'
    else:
        kuna_text = '🔴Включить KUNA-Code'
    if db.get_value('need_ltc') == 1:
        ltc_text = '🟢Выключить LiteCoin'
    else:
        ltc_text = '🔴Включить LiteCoin'
    if db.get_value('need_btc') == 1:
        btc_text = '🟢Выключить BitCoin'
    else:
        btc_text = '🔴Включить BitCoin'
    if db.get_value('need_btc_c') == 1:
        btc_c_text = '🟢Выключить BitCoin CASH'
    else:
        btc_c_text = '🔴Включить BitCoin CASH'
    if db.get_value('need_qiwi') == 1:
        qiwi_text = '🟢Выключить QiwiMoney'
    else:
        qiwi_text = '🔴Включить QiwiMoney'
    if db.get_value('need_easypay') == 1:
        easy_text = '🟢Выключить EasyPay'
    else:
        easy_text = '🔴Включить EasyPay'
    if db.get_value('need_global24') == 1:
        global_text = '🟢Выключить GlobalMoney'
    else:
        global_text = '🔴Включить GlobalMoney'
    if db.get_value('need_promo') == 1:
        promo_text = '🟢Выключить Промокоды'
    else:
        promo_text = '🔴Включить Промокоды'
    on_off_payments = types.InlineKeyboardMarkup(row_width=2)
    on_off_payments.add(
        types.InlineKeyboardButton(text=kuna_text, callback_data='kuna_config'),
        types.InlineKeyboardButton(text=ltc_text, callback_data='ltc_config'),
        types.InlineKeyboardButton(text=btc_text, callback_data='btc_config'),
        types.InlineKeyboardButton(text=btc_c_text, callback_data='btc_c_config'),
        types.InlineKeyboardButton(text=qiwi_text, callback_data='qiwi_config'),
        types.InlineKeyboardButton(text=easy_text, callback_data='easy_config'),
        types.InlineKeyboardButton(text=global_text, callback_data='global_config'),
        types.InlineKeyboardButton(text=promo_text, callback_data='promo_config'),
        types.InlineKeyboardButton(text='↩ Назад', callback_data='exit_to_adm_menu')
    )
    return on_off_payments


add_remove_payments = types.InlineKeyboardMarkup(row_width=2)
add_remove_payments.add(types.InlineKeyboardButton(text='➕Добавить кошелек', callback_data='add_replenish_number'),
                        types.InlineKeyboardButton(text='✖Удалить кошелек', callback_data='remove_replenish_number'),
                        types.InlineKeyboardButton(text='↩️ Назад', callback_data='exit_to_adm_menu'))

add_replenish_number = types.InlineKeyboardMarkup(row_width=3)
add_replenish_number.add(
    types.InlineKeyboardButton(text='💳 QiwiMoney', callback_data='add_qiwi'),
    types.InlineKeyboardButton(text='💵 EasyPay', callback_data='add_easy'),
    types.InlineKeyboardButton(text='🌐 GlobalMoney', callback_data='add_global'),
    types.InlineKeyboardButton(text='↩ Назад', callback_data='exit_to_adm_menu')
)

remove_replenish_number = types.InlineKeyboardMarkup()
remove_replenish_number.add(
    types.InlineKeyboardButton(text='💳 QiwiMoney', callback_data='remove_qiwi'),
    types.InlineKeyboardButton(text='💵 EasyPay', callback_data='remove_easy'),
    types.InlineKeyboardButton(text='🌐 GlobalMoney', callback_data='remove_global'),
    types.InlineKeyboardButton(text='↩ Назад', callback_data='exit_to_adm_menu')
)

cansel_button = types.InlineKeyboardMarkup()
cansel_button.add(types.InlineKeyboardButton(text='❌ Отмена', callback_data='cansel_button'))

promo_type = types.InlineKeyboardMarkup(row_width=2)
promo_type.add(
    types.InlineKeyboardButton(text='💲 Деньги', callback_data='promo_money'),
    types.InlineKeyboardButton(text='📊 Скидка', callback_data='promo_discount'),
    types.InlineKeyboardButton(text='❌ Отмена', callback_data='exit_to_adm_menu')
)

users_config = types.InlineKeyboardMarkup(row_width=2)
users_config.add(
    types.InlineKeyboardButton(text='📊 Установить скидку!', callback_data='set_discount'),
    types.InlineKeyboardButton(text='💲 Установить баланс!', callback_data='set_balance'),
    types.InlineKeyboardButton(text='🔓 Выдать админку', callback_data='add_adm'),
    types.InlineKeyboardButton(text='🔒 Забрать админку', callback_data='remove_adm'),
    types.InlineKeyboardButton(text='🔓 Выдать Курьера', callback_data='add_kur'),
    types.InlineKeyboardButton(text='🔒 Забрать Курьера', callback_data='remove_kur')
)
users_config.add(types.InlineKeyboardButton(text='↩ Назад', callback_data='exit_to_adm_menu'))

aperon_changes = types.InlineKeyboardMarkup(row_width=1)
aperon_changes.add(
    types.InlineKeyboardButton(text='🖍Сменить кошелек LTC', callback_data='change_ltc'),
    types.InlineKeyboardButton(text='🖍Сменить кошелек BTC', callback_data='change_btc'),
    types.InlineKeyboardButton(text='🖍Сменить кошелек BCH', callback_data='change_bch')
)
aperon_changes.add(types.InlineKeyboardButton(text='↩ Назад', callback_data='exit_to_adm_menu'))

shop_config = types.InlineKeyboardMarkup(row_width=3)
shop_config.add(
    types.InlineKeyboardButton(text='💵 Установить валюту', callback_data='set_money_value'),
    types.InlineKeyboardButton(text='📄 Изменить описание', callback_data='set_info_message'))
shop_config.add(types.InlineKeyboardButton(text='➗ Процент реферальной системы', callback_data='set_ref_percent')),
shop_config.add(types.InlineKeyboardButton(text='➕ Старшую категорию', callback_data='add_parent_category'))
shop_config.add(
    types.InlineKeyboardButton(text='♻️➕ Категорию', callback_data='add_category'),
    types.InlineKeyboardButton(text='♻️➕ Подкатегорию', callback_data='add_sub_category'))
shop_config.add(
    types.InlineKeyboardButton(text='♻️🛒 Создать товар', callback_data='add_product_to_category'),
    types.InlineKeyboardButton(text='♻️➕ Содержимое товара', callback_data='add_product'))

shop_config.add(
    types.InlineKeyboardButton(text='❌ Удалить категорию',callback_data='del_category'),
    types.InlineKeyboardButton(text='❌ Удалить товар',callback_data='del_product'))
shop_config.add(types.InlineKeyboardButton(text='↩️ Назад', callback_data='exit_to_adm_menu'))

shop_config1 = types.InlineKeyboardMarkup(row_width=2)
shop_config1.add(
    types.InlineKeyboardButton(text='♻️🛒 Создать товар', callback_data='add_product_to_category_kur')),
shop_config1.add(types.InlineKeyboardButton(text='♻️➕ Содержимое товара', callback_data='add_product_kur')),
shop_config1.add(types.InlineKeyboardButton(text='↩️ Назад', callback_data='exit_to_kur_menu'))
