from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters, ConversationHandler
from telegram import Update
from config import TOKEN
from teldirbot_func import*
from edit import*

updater=Updater(TOKEN)
dispatcher=updater.dispatcher

start_handler=CommandHandler('start', start)
cancel_handler=CommandHandler('cancel',cancel)
view_handler=CommandHandler('view',view)
search_handler=CommandHandler('search',search)
#edit_handler=CommandHandler('edit', edit)

edit_handler=ConversationHandler(
    entry_points=[CommandHandler('edit', edit)],
    states={
        SEARCH_FOR_EDIT: [MessageHandler(Filters.text,search_for_edit)],
        NEW_CONTACT: [MessageHandler(Filters.text,new_contact)],
         },
        fallbacks=[CommandHandler('cancel',cancel)],
)


enter_handler=ConversationHandler(
    entry_points=[CommandHandler('enter', enter)],
    states={
        NAME: [MessageHandler(Filters.text,name)],
        SURNAME: [MessageHandler(Filters.text,surname)],
        PHONE: [MessageHandler(Filters.text,phone)],
        NOTE:[MessageHandler(Filters.text,note)]
        },
        fallbacks=[CommandHandler('cancel',cancel)],
)

#new_contact_message_handler=MessageHandler(Filters.text, new_contact)
search_message_handler=MessageHandler(Filters.text, search_message)
#search_message_for_edit_handler=MessageHandler(Filters.text, search_message_for_edit)
#new_contact_message_handler=MessageHandler(Filters.text, new_contact)


dispatcher.add_handler(enter_handler)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(cancel_handler)
dispatcher.add_handler(view_handler)
dispatcher.add_handler(search_handler)
dispatcher.add_handler(edit_handler)
dispatcher.add_handler(search_message_handler)
#dispatcher.add_handler(search_message_for_edit_handler)
#dispatcher.add_handler(edit_handler)



print('Сервер запущен')
updater.start_polling()
updater.idle()
