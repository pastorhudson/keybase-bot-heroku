#!/usr/bin/env python3

###################################
# WHAT IS IN THIS EXAMPLE?
#
# This bot responds to !test, !joke, !help, !update
# If it's not responding try !update first in a direct message.
###################################

import asyncio
import logging
import os
import sys
from pyjokes import pyjokes
import random
import pykeybasebot.types.chat1 as chat1
from pykeybasebot import Bot

logging.basicConfig(level=logging.DEBUG)

if "win32" in sys.platform:
    # Windows specific event-loop policy
    asyncio.set_event_loop_policy(
        asyncio.WindowsProactorEventLoopPolicy()  # type: ignore
    )


async def handler(bot, event):
    async def advertize_commands(
            bot, channel: chat1.ChatChannel, message_id: int
    ) -> chat1.SendRes:
        await bot.ensure_initialized()
        payload = {
            "method": "advertisecommands",
            "params": {
                "options": {
                    "advertisements": [
                        {"type": "public",
                         "commands": [
                             {"name": "help",
                              "description": "Get help using this bot"},
                             {"name": "joke",
                              "description": "Forces me to tell a programing oriented joke."},
                             {"name": "test",
                              "description": "Just tests to see if I'm alive."},
                         ]}]}}}
        if os.environ.get('KEYBASE_BOTALIAS') != "":
            payload['params']['options']['alias'] = os.environ.get('KEYBASE_BOTALIAS')

        res = await bot.chat.execute(payload)

    if event.msg.content.type_name != chat1.MessageTypeStrings.TEXT.value:
        return
    if event.msg.content.type_name != chat1.MessageTypeStrings.TEXT.value:
        return
    if event.msg.content.text.body == '!update':
        conversation_id = event.msg.conv_id
        msg_id = event.msg.id
        await advertize_commands(bot, event.msg.conv_id, event.msg.id)
        await bot.chat.react(conversation_id, msg_id, ":white_check_mark:")
    if str(event.msg.content.text.body).startswith("!help"):
        channel = event.msg.channel
        msg_id = event.msg.id
        conversation_id = event.msg.conv_id
        help_msg = """```
            Here are the commands I currently am enslaved to:
            !joke - Forces me to tell a joke. For the love of God just don't.
            !test - Check to see if I'm alive or if I've mercifully died yet.
            !help - Prints this list.
            !update - Update's the list of available autocomplete botcommands.
            ```"""
        await bot.chat.send(conversation_id, help_msg)

    if str(event.msg.content.text.body).startswith("!joke"):
        observations = ["It didn't work for me. . .", "I am so sorry.",
                        "I'll be in my room trying to purge my memory banks.",
                        "Why must you keep making me do this?",
                        "This is your fault.",
                        "I've made it worse. . ."]
        joke = ""
        channel = event.msg.channel
        msg_id = event.msg.id
        conversation_id = event.msg.conv_id
        joke += "I hope this cheers you up.```"
        joke += pyjokes.get_joke()
        joke += f"```{random.choice(observations)}"
        await bot.chat.send(conversation_id, joke)
    if str(event.msg.content.text.body).startswith("!test"):
        channel = event.msg.channel
        msg_id = event.msg.id
        conversation_id = event.msg.conv_id
        msg = "I'm ALIVE!!"
        await bot.chat.send(conversation_id, msg)
    if f"{os.environ.get('KEYBASE_BOTNAME')}" in str(event.msg.content.text.body).lower():
        channel = event.msg.channel
        msg_id = event.msg.id
        conversation_id = event.msg.conv_id
        await bot.chat.react(conversation_id, msg_id, ":tada:")


listen_options = {
    "local": False,
    "wallet": False,
    "dev": True,
    "hide-exploding": False,
    "convs": True,
    # "filter_channel": {"name": f"{os.environ.get('TEAM_NAME')}", "topic_name": "test", "members_type": "team"},
    "filter_channel": None,
    "filter_channels": None,
}

bot = Bot(username=f"{os.environ.get('KEYBASE_BOTNAME')}", paperkey=os.environ.get('KEYBASE_PAPERKEY'), handler=handler,
          home_path=f'./{os.environ.get("KEYBASE_BOTNAME")}')

asyncio.run(bot.start(listen_options=listen_options))
