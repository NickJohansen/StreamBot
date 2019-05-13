#################################################
# Author: Nick Johansen
# Title: Streambot
# Description: This will take messages from chat and display them in terminal
# Version: 0.1
#################################################

from datetime import datetime
import socket
import time
import sys
import re

server = 'irc.chat.twitch.tv'
port = 6667
nickname = 'itsmepnd'
token = 'oauth:' #you put your auth code here: https://dev.twitch.tv/docs/authentication/getting-tokens-oauth/
channel = '#itsmepnd'
client_id = '' #put client iD here, in later version will allow to change title

hello = 'Why hello there'
com = 'current commands are: !commands, !hello, !YT, !sched'
YouTube = 'you can find my youtube channel here: https://www.youtube.com/channel/UCVIYclP3ElsMi2tNfED6XJQ?'
sched = 'yea...'

sock = socket.socket()
sock.connect((server, port))

sock.send("PASS {}\r\n".format(token).encode("utf-8"))
sock.send("NICK {}\r\n".format(nickname).encode("utf-8"))
sock.send("JOIN {}\r\n".format(channel).encode("utf-8"))

run = True
connected = False

def chat(s, msg):
    s.send("PRIVMSG {} :{}\r\n".format(channel, msg).encode("utf-8"))

while run:
    response = sock.recv(2048).decode("utf-8")
    if response == "PING :tmi.twitch.tv\r\n":
        sock.send("PONG :tmi.twitch.tv\r\n".encode("utf-8"))
    else:
        username = re.search(r"\w+",response).group(0)
        CHAT_MSG = re.compile(r"^:\w+!\w+@\w+\.tmi\.twitch\.tv PRIVMSG #\w+ :")
        message = CHAT_MSG.sub("",response).rstrip('\n')
        
        if 'End of /NAMES list' in message:
            connected = True
        if connected == True:
            if 'End of /NAMES list' in message:
                pass
            else:
                if 'hello pnd' in message:
                    chat(sock,"{} {}".format(hello,username))
                if '!commands' in message:
                    chat(sock,com)
                if '!hello' in message:
                    chat(sock,hello)
                if '!YT' in message:
                    chat(sock,YouTube)
                if '!sched' in message:
                    chat(sock,sched)
                print('{}: {}'.format(username,message))