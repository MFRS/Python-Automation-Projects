import config
import socket
from collections import namedtuple
import datetime
import random
from pywinauto.application import Application
import win32api, win32con, subprocess
import time
from keyboardControls import keyboardControls as kc
import sys
import os.path

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from generalfunctions import generalFunctions as gf


TEMPLATE_COMMANDS = {
    '!discord':'Please join the {message.channel} discord server, {message.user}',
    '!so':'Check out {message.text_args[0]}, they are a nice streamer!',

}


Message = namedtuple(
    'Message',
    'prefix user channel irc_command irc_args text text_command text_args',


)



class Bot:
    appChrome = Application(backend='win32').connect(found_index=0,title_re='.*The Sims.*')
    time.sleep(2)
    dlg_specChrome = appChrome.window(found_index=0,title_re='.*The Sims.*')
    path_textBox = r"G:\My Drive\NOISE Creative\Noise purposed scripts\Avengers2-AgeofUltron\TwitchPlaysTheSims4\commands.txt"

    def __init__(self):
        self.irc_server = 'irc.twitch.tv'
        self.irc_port = 6667
        self.oauth_token = config.OAUTH_TOKEN
        self.username = 'twitchplaysthesims4'
        self.channels = ['twitchplaysthesims4']
        self.custom_commands = {
            '!date': self.reply_with_date,
            '!ping': self.reply_to_ping,
            '!randint': self.reply_with_randint,
        }

    def get_user_from_prefix(self,prefix):
        domain = prefix.split("!")[0]
        if domain.endswith(".tmi.twitch.tv"):
            return domain.replace(".tmi.twitch.tv","")
        if "tmi.twitch.tv" not in domain:
            return domain
        return None



    def send_privmsg(self,channel,text):
        self.send_command(f'PRIVMSG #{channel} :{text}')

    def send_command(self,command):
        if 'PASS' not in command:
            print(f'< {command}')
        self.irc.send((command + '\r\n').encode())

    def connect(self):
        self.irc = socket.socket()
        self.irc.connect((self.irc_server , self.irc_port))
        self.send_command(f'PASS {self.oauth_token}')
        self.send_command(f'NICK {self.username}')
        for channel in self.channels:
            self.send_command(f'JOIN #{channel}')
            self.send_privmsg(channel,'Hey there!')
        self.loop_for_messages()

    def parse_message(self,received_msg):
        parts = received_msg.split(" ")
        prefix = None
        user = None
        channel = None
        irc_command = None
        irc_args = None
        text = None
        text_command = None
        text_args = None

        if parts[0].startswith(":"):
            prefix = parts[0][1:]
            user = self.get_user_from_prefix(prefix)
            parts = parts[1:]

        text_start = next(
            (idx for idx, part in enumerate(parts) if part.startswith(":")),
            None
        )
        if text_start is not None:
            text_parts = parts[text_start:]
            text_parts[0] = text_parts[0][1:]
            text = " ".join(text_parts)
            text_command = text_parts[0]
            text_args = text_parts[1:]
            parts = parts[:text_start]

        irc_command = parts[0]
        irc_args = parts[1:]


        hash_start = next(
            (idx for idx, part in enumerate(irc_args) if part.startswith("#")),
            None
        )

        if hash_start is not None:
            channel = irc_args[hash_start][1:]


        message = Message(
            prefix = prefix,
            user = user,
            channel = channel,
            irc_command = irc_command,
            irc_args = irc_args,
            text = text,
            text_command = text_command,
            text_args = text_args
        )
        return message
        
    def handle_template_command(self, message, text_command, template):
        text = template.format(**{'message':message})
        self.send_privmsg(message.channel,text)

    def reply_with_date(self, message):
        formatted_date = datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')
        text = f'Here you go {message.user}, the date is: {formatted_date},'
        self.send_privmsg(message.channel, text)

    def reply_to_ping(self, message):
        text = f'Hey {message.user}, nice ping! PONG!'
        self.send_privmsg(message.channel, text)

    def reply_with_randint(self, message):
        text = str(random.randint(0,1000))
        self.send_privmsg(message.channel, text)

    def reply_with_wrongMessage(self, message):
        text =  f'Sorry, {message.user}, the command is wrong.'
        self.send_privmsg(message.channel, text)
    

    def handle_message(self,received_msg):
        if len(received_msg) == 0:
            return 

        message = self.parse_message(received_msg)
        print(f'> {message}')
        # print(message.text)
        # print(message.text_args)

       
        if message.user != None and message.text != None and message.text != message.user and "End of /NAMES list" not in message.text: #!and message.user != "twitchplaysthesims4":
            print("someone")

            # try:  
            #     # must look out for ping messages
            # print(finalCommand)

            if "click" in message.text:
            # try:
                splitT = str(message.text).split(",")
                # print(splitT)
                
                kc.click(splitT)
                # except:
                #     Bot.reply_with_wrongMessage(Bot,message)
            else:
                finalCommand = kc.convertComment(1,message.text)
                addBraces = str(finalCommand)
                print(addBraces)
                Bot.dlg_specChrome.type_keys("{"+addBraces+" "+ "down}" "{"+addBraces+" "+ "up}")

                        
            



                # if "type" in str(message.text):
                #     f= open(Bot.path_textBox,"a")
                #     f.write("Press"+" " +str(message.text).split(" ")[1]+"\n")
                #     finalCommand = kc.convertComment(1,message.text)
                #     Bot.dlg_specChrome.type_keys(finalCommand)

                #     f.close()
                # else:
                #     f= open(Bot.path_textBox,"a")
                #     f.write("Click"+" " +str(message.text).split(" ")[1]+"\n")
                #     Bot.dlg_specChrome.type_keys("^l")
                #     f.close()
            
                # if "sc" in str(message.text):
                #     f= open(Bot.path_textBox,"a")
                #     f.write("Click"+" " +str(message.text).split(" ")[1]+"\n")
                    

                #     Bot.dlg_specChrome.type_keys()
                #     # Bot.dlg_specChrome.type_keys()
                #     f.close()

                # option for shortcut
                #     option to check shortcuts that may quit the computer
            # except:
            #     pass

        if message.irc_command == "PING":
            self.send_command("PONG :tmi.twitch.tv")

        if message.irc_command == "PRIVMSG":
            if message.text_command in TEMPLATE_COMMANDS:
                self.handle_template_command(
                    message, #Message(...)
                    message.text_command, #!discord
                    TEMPLATE_COMMANDS[message.text_command], #
                )
        if message.text_command in self.custom_commands:
            self.custom_commands[message.text_command](message)

    def loop_for_messages(self):
        while True:
            # If you want to test PING - received_msgs = 'PING :tmi.twitch.tv\r\n' + self.irc.recv(2048).decode()
            received_msgs = self.irc.recv(2048).decode()
            
            for received_msg in received_msgs.split('\r\n'):
                self.handle_message(received_msg)
           


def main():
    bot = Bot()
   
    bot.connect()

if __name__ == '__main__':
    main()
