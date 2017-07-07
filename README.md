Mick's Arduino projects
=======================

TSYS01 Temperature logger
-------------------------
Ardunio reads tempartures from a TSYS01 sensor and pushes the readings
over serial. A python client listens to the COM port and logs the read-
ings to a file, along with ISO timestamps.