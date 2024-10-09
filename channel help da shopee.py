'''# bot_telegram.py

import telebot
import logging

TOKEN = '7189301524:AAGHm5cj0F27NHnf9u7oMbjxjTnES8BJ4OA'
ADMIN_IDS = [6230088395,5592756194]  # IDs dos administradores do grupo


bot = telebot.TeleBot(TOKEN)

# Configuração de logging
logger = telebot.logger
telebot.logger.setLevel(logging.INFO)

@bot.message_handler(commands=['ajuda'])
def send_help(message):
    help_text = """
    Bot de Monitoramento de Mensagens de Serviço:
    - Este bot apaga automaticamente mensagens de serviço no grupo.
    - Comandos disponíveis:
        /ajuda - Mostra esta mensagem de ajuda.
    """
    bot.reply_to(message, help_text)

@bot.message_handler(content_types=[
    'new_chat_members', 
    'left_chat_member', 
    'pinned_message', 
    'new_chat_title', 
    'new_chat_photo', 
    'delete_chat_photo', 
    'group_chat_created', 
    'supergroup_chat_created', 
    'channel_chat_created', 
    'migrate_to_chat_id', 
    'migrate_from_chat_id'
])
def handle_service_messages(message):
    try:
        bot.delete_message(message.chat.id, message.message_id)
        logger.info(f"Mensagem de serviço deletada do chat {message.chat.id}")
        notify_admins(f"Mensagem de serviço deletada do chat {message.chat.id}")
    except Exception as e:
        logger.error(f"Erro ao apagar mensagem: {e}")
        notify_admins(f"Erro ao apagar mensagem no chat {message.chat.id}: {e}")

def notify_admins(notification):
    for admin_id in ADMIN_IDS:
        try:
            bot.send_message(admin_id, notification)
        except Exception as e:
            logger.error(f"Falha ao notificar admin {admin_id}: {e}")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "Mensagem recebida")

if __name__ == '__main__':
    bot.polling(none_stop=True)'''

import telebot
import logging
import time

# @ do bot: @channel_help_shoppe_bot
# Substitua 'YOUR_TELEGRAM_BOT_TOKEN' pelo token do seu bot.
TOKEN = '7002296307:AAHxHHUXxYUZZvTiZ065TA92APOxFLJdzGQ'
ADMIN_IDS = [123456789, 987654321]  # IDs dos administradores do grupo

bot = telebot.TeleBot(TOKEN)

# Configuração de logging
logger = telebot.logger
telebot.logger.setLevel(logging.INFO)

@bot.message_handler(commands=['ajuda'])
def send_help(message):
    help_text = """
    Bot de Monitoramento de Mensagens de Serviço:
    - Este bot apaga automaticamente mensagens de serviço no grupo.
    - Comandos disponíveis:
        /ajuda - Mostra esta mensagem de ajuda.
    """
    bot.reply_to(message, help_text)

@bot.message_handler(content_types=[
    'new_chat_members', 
    'left_chat_member', 
    'pinned_message', 
    'new_chat_title', 
    'new_chat_photo', 
    'delete_chat_photo', 
    'group_chat_created', 
    'supergroup_chat_created', 
    'channel_chat_created', 
    'migrate_to_chat_id', 
    'migrate_from_chat_id'
])
def handle_service_messages(message):
    try:
        bot.delete_message(message.chat.id, message.message_id)
        logger.info(f"Mensagem de serviço deletada do chat {message.chat.id}")
    except Exception as e:
        logger.error(f"Erro ao apagar mensagem: {e}")
        notify_admins(f"Erro ao apagar mensagem no chat {message.chat.id}: {e}")

def notify_admins(notification):
    for admin_id in ADMIN_IDS:
        try:
            bot.send_message(admin_id, notification)
        except Exception as e:
            # Log the specific error if the bot cannot initiate conversation with the user
            if "bot can't initiate conversation with a user" in str(e):
                logger.warning(f"Não foi possível notificar admin {admin_id}: O bot não pode iniciar uma conversa com o usuário. Peça ao administrador para iniciar uma conversa com o bot.")
            else:
                logger.error(f"Falha ao notificar admin {admin_id}: {e}")

def run_bot():
    while True:
        try:
            bot.polling(none_stop=True, interval=0, timeout=20)
        except Exception as e:
            logger.error(f"Falha na execução do bot: {e}")
            notify_admins(f"Erro crítico na execução do bot: {e}")
            time.sleep(15)  # Espera antes de tentar novamente

if __name__ == '__main__':
    run_bot()





'''7189301524:AAGHm5cj0F27NHnf9u7oMbjxjTnES8BJ4OA'''