from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters, ConversationHandler
from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove

SEARCH_FOR_EDIT,NEW_CONTACT = range(2)

def edit (update:Update, context:CallbackContext):
    """
    Действия при вводе команды edit
    приглашение к вводу строки для поиска строки для редактирования   
    """
    print('Введите строку для поиска контакта для редактирования')
    update.message.reply_text ('Введите строку для поиска контакта для редактирования')   
    return SEARCH_FOR_EDIT

def search_for_edit (update:Update, context:CallbackContext):
    """
    Поиск строки для редактирования в файле directory.log
    """
    search_str=update.message.text
    print(search_str)
    with open('directory.log','r') as file:
        #update.message.reply_text('Список контактов')
        for line in file:
            if search_str in line:
                print(line)
                update.message.reply_text (line)
    update.message.reply_text ('Скопируйте контакт в поле ввода\nи отредактируйте его.\nВведите новый контакт')
    return NEW_CONTACT

def new_contact(update:Update, context:CallbackContext): 
    """
    Ввод новой строки для записи в файл directory.log
    """
    new_contact=update.message.text
    print(new_contact)
    new_contact=new_contact.split()
    print('Записываю в справочник directory.log')
    update.message.reply_text ('Записываю в справочник')
    with open('directory.log','a') as file:
        file.writelines(s + '\t\t' for s in new_contact)
        file.writelines('\n')
    
    reply_keyboard=[
                    ['/start','/cancel']
                    ]
    markup_key=ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True, one_time_keyboard=True,)
    update.message.reply_text('Выберите действие',
        reply_markup=markup_key,)

    return ConversationHandler.END