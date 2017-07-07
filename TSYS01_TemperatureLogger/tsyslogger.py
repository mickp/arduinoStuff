#!/usr/bin/python
# -*- coding: utf-8
"""Blue Robotics TSYS01 Temperature Logger client

Copyright Mick Phillips, 2017.

Receives temperature readings over serial from tsys_sender.ino and
logs to file with ISO-format date and time.

 Copyright 2017 Mick Phillips (mick.phillips@gmail.com)

 This program is free software: you can redistribute it and/or modify
 it under the terms of the GNU General Public License as published by
 the Free Software Foundation, either version 3 of the License, or
 (at your option) any later version.

 This program is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 GNU General Public License for more details.

 You should have received a copy of the GNU General Public License
 along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""
import argparse
import logging
import logging.handlers
import serial
import time

TIME_FORMAT = "%Y-%m-%dT%H:%M:%S"
LOG_FORMAT = "%(asctime)s\t%(message)s"
parser = argparse.ArgumentParser(description='Log readings from COM port to file.')
parser.add_argument('port', metavar='COM port', type=str, nargs='?', default='COM7')
parser.add_argument('filename', metavar='log file name', type=str, nargs='?', default='temperature.log')

args = parser.parse_args()

handler = logging.handlers.RotatingFileHandler(args.filename, maxBytes=100*1024*1024)
handler.setFormatter(logging.Formatter(LOG_FORMAT, TIME_FORMAT))
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.addHandler(handler)

serialport = serial.Serial(args.port, 9600)

while True:
    t = serialport.readline()
    t = t.decode().strip()
    if t.lower() == 'starting':
        continue
    logger.info(t)
    handler.close()