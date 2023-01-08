from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters, ConversationHandler
from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove
import logging

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO, filename="log_directory.log"
)
logger = logging.getLogger('log_directory')
logger.setLevel(logging.DEBUG)
stream = logging.StreamHandler()



data=[n for n in range(4)]

NAME, SURNAME, PHONE, NOTE = range(4)


def start(update:Update,_):
    """
    Действия при вводе команды start
    Вывод меню для выбора действия
    Выбор действия
    Логгирование в файл log_directory
    """
    user = update.message.from_user
    logger.info("start %s", user.username)

    reply_keyboard=[
                    ['/view','/enter'],
                    ['/search','/edit'],
                    ['/cancel']
                    ]
    markup_key=ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True, one_time_keyboard=True,)
    update.message.reply_text(
        'Вас приветствует телефонный справочник \n'
        'Выберите действие',
        reply_markup=markup_key,)
    action=update.message.text
    user = update.message.from_user
    logger.info("action %s: %s", update.message.text, user.username)
    
    return 

def enter(update:Update, context:CallbackContext):
    """
    Действия при вводе команды enter
    Приглашение к вводу данных контакта
    """
    update.message.reply_text ('Добавление контакта\nЛучше это делать латиницей\nВведите имя (до 10 символов)')
    return NAME

def name(update:Update, context:CallbackContext):
    """
    Ввод имени контакта
    Логгирование в файл log_directory
    """
    name=update.message.text 
    name=name[:10]
    print(name)
    data[0]=name
    user = update.message.from_user
    logger.info("name %s: %s", update.message.text, user.username)
    update.message.reply_text (f'Введите фамилию (до 15 символов)')

    return SURNAME

def surname(update:Update, context:CallbackContext):
    """
    Ввод фамилии
    Логгирование в файл log_directory
    """
    #update.message.reply_text (f'Введите фамилию')
    surname=update.message.text
    surname=surname[:15]
    user = update.message.from_user
    logger.info("surname %s: %s", update.message.text, user.username)
    print(surname)
    data[1]=surname
    update.message.reply_text (f'Введите телефон (до 15 символов) ')
    return PHONE
    
def phone (update:Update, context:CallbackContext):
    """
    Ввод телефона контакта
    Логгирование в файл log_directory
    """
    #update.message.reply_text (f'Введите телефон ')
    phone=update.message.text
    phone=phone[:15]
    user = update.message.from_user
    logger.info("phone %s: %s", update.message.text, user.username)
    print(phone)
    data[2]=phone
    update.message.reply_text (f'Введите комментарий\n(до 15 символов) ')
    return NOTE

def note (update:Update, context:CallbackContext):
    """
    Ввод кометария к контакту
    Логгирование в файл log_directory
    Запись данных о контакте в файл directory.log
    """
    note=update.message.text
    note=note[:15]
    user = update.message.from_user
    logger.info("note %s: %s", update.message.text, user.username)
    print(note)
    data[3]=note
    print(data)
    with open('directory.log','a+') as file:
            file.writelines(s + '\t\t' for s in data)
            file.writelines('\n')

    reply_keyboard=[
                    ['/start','/cancel']
                    ]
    markup_key=ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True, one_time_keyboard=True,)
    update.message.reply_text('Выберите действие',
        reply_markup=markup_key,)

    return ConversationHandler.END

def view (update:Update, context:CallbackContext):
    """
    Действия при вводе команды view
    Чтение файла directory.log
    """
    user = update.message.from_user
    logger.info("view %s", user.username)
    with open('directory.log','r') as file:
        print()
        print('Список контактов')
        update.message.reply_text('Список контактов')
        for line in file:
            print(line)
            update.message.reply_text (line)

    reply_keyboard=[
                    ['/start','/cancel']
                    ]
    markup_key=ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True, one_time_keyboard=True,)
    update.message.reply_text('Выберите действие',
        reply_markup=markup_key,)

    return

def search (update:Update, context:CallbackContext):
    """
    Действия при вводе команды search
    Приглашение к вводу строки для поиска
    """
    user = update.message.from_user
    logger.info("search %s", user.username)
    update.message.reply_text ('Введите строку для поиска')
    search_message
    return

def search_message (update:Update, context:CallbackContext):
    """
    Действия при вводе команды search
    Ввод строки для поиска
    Поиск строк со строкой ввода в файле directory.log
    """
    search_str=update.message.text
    user = update.message.from_user
    logger.info("search_str %s: %s", update.message.text, user.username)
    print(search_str)
    with open('directory.log','r') as file:
        for line in file:
            if search_str in line:
                print(line)
                update.message.reply_text (line)

    reply_keyboard=[
                    ['/start','/edit'],
                    ['/cancel']
                    ]
    markup_key=ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True, one_time_keyboard=True,)
    update.message.reply_text(
        'Выберите действие',
        reply_markup=markup_key,)
    return

def cancel (update:Update, context:CallbackContext):
    """
    Действия при вводе команды cancel
    Завершение работы
    """
    user = update.message.from_user
    logger.info("cancel %s", user.username)
    update.message.reply_text (f'Работа окончена\nДля возобновления работы введите /start')
    return ConversationHandler. END
