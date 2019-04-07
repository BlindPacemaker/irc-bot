#!/usr/bin/python3

import socket
ircsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server = "irc.freenode.net"
channel = "##botname-testing"
botnick = "botname"
adminname = "username"
exitcode = "bye " + botnick

ircsock.connect((server, 6667))
ircsock.send(bytes("USER " + botnick + " " + botnick +
                   " " + botnick + " " + botnick + "\n", "UTF-8"))
ircsock.send(bytes("NICK " + botnick + "\n", "UTF-8"))
