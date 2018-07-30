#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
import telegram
from telegram.error import NetworkError, Unauthorized
from time import sleep


update_id = None

badw  = [line.lower().rstrip('\n') for line in open('bad.txt')]

def main():
    """Run the bot."""
    global update_id
    # Telegram Bot Authorization Token
    bot = telegram.Bot('NO_SHARE')

    # get the first pending update_id, this is so we can skip over it in case
    # we get an "Unauthorized" exception.
    try:
        update_id = bot.get_updates()[0].update_id
    except IndexError:
        update_id = None

    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    while True:
        try:
            echo(bot)
        except NetworkError:
            sleep(1)
        except Unauthorized:
            # The user has removed or blocked the bot.
            update_id += 1

def bwchec(text):
    try:
        words = text.split()
        for word in words:
            if word.lower() in badw:
                return True
        return False
    except:
        return False

def echo(bot):
    """Echo the message the user sent."""
    global update_id
    # Request updates after the last update_id
    for update in bot.get_updates(offset=update_id, timeout=10):
        update_id = update.update_id + 1

        if update.message:  # your bot can receive updates without messages
            # Reply to the message
            if  update.message.text:
                #print update.message.from_user.username
                if 'puto bot' in update.message.text.lower():
                    update.message.reply_text("@" + update.message.from_user.username + " succionamela" )
                if 'apple' in update.message.text.lower():
                    update.message.reply_text("https://www.youtube.com/watch?v=D1R-jKKp3NA")
                if bwchec(update.message.text):
                    try:
                        update.message.reply_text("@" + update.message.from_user.username + " piensa en los chamacos, no digas malas palabras\n" )
                    except:
                        pass


if __name__ == '__main__':
    main()
