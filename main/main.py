import telebot
from telebot.types import Message
import os
bot = telebot.TeleBot('7883819968:AAHrl4WoYU0Ax1u8OXLTA7fVxxtU5fiJvxI')
@bot.message_handler(commands=['start'])
def start(message: Message):
    bot.reply_to(message, 'Привет я бот который поможет тебе подобрать идей для подделок из ненужный вещей 😊')


@bot.message_handler(commands=['Bottle'])
def Bottle(message: Message):
    bot.reply_to(message, "Вот какую подделку можно сделать из бутылки 🍶: Цветочные горшки: Обрежьте пластиковую бутылку пополам. Используйте нижнюю часть как горшок, добавив землю и цветы или растения. Вы можете украсить горшок красками или обернуть его веревкой. 2. Кормушка для птиц: Сделайте несколько отверстий в бутылке и вставьте деревянные палочки как перила. Налейте немного корма для птиц внутри и повесьте кормушку на дереве. Подставки для карандашей: Обрежьте верхнюю часть бутылки и используйте ее для хранения канцелярских принадлежностей. Вы можете украсить подставку снаружи цветной бумагой или краской. 4. Игрушки для детей: Наполните бутылку крупами или бусинами и закройте крышку. Это получится шумовая игрушка. Сделайте несколько отверстий и вставьте веревку - получится забавная игрушка для домашнего использования.5. Лампа: Обрежьте верхнюю часть бутылки, вставьте небольшую лампочку и оформите по своему вкусу.Убедитесь, что использованный кабель безопасен для использования с электрическими устройствами. 6. Декоративный жираф: Используйте несколько бутылок разного размера, чтобы создать фигуру жирафа. Раскрасьте и добавьте детали, такие как глаза и пятна. 7. Водяная бомбочка: Вы можете сделать «бомбочки» из бутылки, заполнив ее водой и немного сжав, чтобы сбрасывать на улице в жаркий день")


@bot.message_handler(commands=['commands'])
def start(message: Message):
    bot.reply_to(message, 'Вот все команды 😊: /Bottle, /Shirt, /Bottle_feeders, /Bottle_flower_pots')

@bot.message_handler(commands=['Shirt'])
def start(message: Message):
    bot.reply_to(message, 'Вот семь интересных идей для поделок из старой одежды: 1. Мягкие игрушки:Используйте остатки ткани, чтобы создать мягкие игрушки. Например, можно сшить мишку, собаку или любое другое животное. Это отличный способ сохранить любимую одежду в новой форме. 2. Сумки и рюкзаки: Превратите старые джинсы или футболки в стильные сумки или рюкзаки. Просто обрежьте, сшейте и добавьте ремешки. Вы можете также использовать детали карманов как декоративные элементы. 3. Подушки: Соедините куски ткани от старой одежды, чтобы создать уникальные наволочки или декоративные подушки. Это может стать отличным дополнением для интерьера. 4. Ковер или плед: Сшейте много разных кусочков из старой одежды, чтобы создать уютный ковер или плед. Можно комбинировать разные цвета и текстуры для интересного эффекта. 5. Гардероб для кукол: Используйте остатки ткани, чтобы создать одежду для кукол. Это создаст отличный способ развить творческие навыки у детей. 6. Заплатки для новых вещей: Используйте ткань из старой одежды, чтобы сделать заплатки для других, более поврежденных вещей. Это не только полезно, но и экологически чисто. 7. Браслеты и аксессуары: Переработайте старые футболки или блестящие ткани в стильные браслеты, ободки для волос или ожерелья. Для этого можно заплести косички или использовать технику ткань в клетку.')

@bot.message_handler(commands=['Bottle_feeders'])
def send_gojo_image(message: Message):
    pictures=os.listdir('Подделки')
    with open('Подделки/Bottle feeders.png', 'rb') as file:
        bot.send_photo(message.chat.id, file)

@bot.message_handler(commands=['Bottle_flower_pots'])
def send_gojo_image(message: Message):
    pictures=os.listdir('Подделки')
    with open('Подделки/Bottle flower pots.png', 'rb') as file:
        bot.send_photo(message.chat.id, file)

bot.polling()
