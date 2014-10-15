# !/usr/bin/bash
# coding=utf-8

"""
This package contains functions to make some operations easier or standardized
throughout the project.
"""

import csv  # For csv2fixture
import os  # For csv2fixture
import socket, struct  # For ip2Num_alt, num2ip
from datetime import date, datetime, timedelta  # For any functions involving time
from dateutil import parser  # For str2datetime
from random import randint  # For randomString
import re  # For coord2num


def birthday2age(birthday):
	if not isinstance(birthday, datetime) and not isinstance(birthday, date):
		return False
	today = date.today()
	return today.year - birthday.year - ((today.month, today.day) < (birthday.month, birthday.day))


def calcTimezone(dt):
	timestamp, offset = unicode(dt).split("+")
	offsetHour, offsetMin = offset.split(":")
	return str2datetime(timestamp) + timedelta(hours=int(offsetHour), minutes=int(offsetMin))


def coord2num(coordString):
	coordString = unicode(coordString.strip(), "UTF-8")
	coordRegex = re.compile(u"^(([0-9]{1,3}).([0-9]{1,2}).([0-9]{1,2}\.?[0-9]*).([NSEW])$)", re.UNICODE)
	result = coordRegex.findall(coordString)
	if result:
		result = result[0]
		degrees = float(result[1])
		minutes = float(result[2]) / 60
		seconds = float(result[3]) / 60 ** 2
		signal = 1 if (result[4] == "N" or result[4] == "E") else -1
	return (degrees + minutes + seconds) * signal


def coord2str(coordFloat, isLatitude=True):
	if isLatitude:
		direction = "N" if coordFloat > 0 else "S"
	else:
		direction = "E" if coordFloat > 0 else "W"
	coordFloat = abs(coordFloat)
	degrees = int(coordFloat)
	degRemainder = coordFloat - int(coordFloat)
	# se 1 grau é 60 minutos
	# entao 0.76 graus é x minutos
	minutes = degRemainder * 60
	minRemainder = minutes - int(minutes)
	# seconds
	seconds = minRemainder * 60
	return u"%d°%d'%2.3f\"%s" % (degrees, minutes, seconds, direction)


def csv2fixture(filePath, model, outputName=None, delimiter=";"):
	# Count the number of rows in
	def countRows(filePath):
		with open(filePath) as f:
			non_blank_count = 0
			for line in f:
				if line.strip():
					non_blank_count += 1
			return non_blank_count - 1
	if not outputName:
		outputName = os.path.basename(filePath) + '.json'
	fileHandle = open(filePath, 'r')
	outputFile = open(outputName, 'w')
	csvData = csv.DictReader(fileHandle, delimiter=delimiter)
	csvSize = countRows(filePath)
	pk = 0
	outputFile.write(unicode('[\n'))
	for row in csvData:
		pk += 1
		# Write the element opening bracket
		outputFile.write('\t{\n')
		# Write the refering model
		outputFile.write('\t\t"model": "%s",\n' % model)
		# Write the primary keyast iteratio
		outputFile.write('\t\t"pk": %d,\n' % pk)
		# Write the field list opening
		outputFile.write('\t\t"fields": {\n')
		size = len(row)
		i = 1
		for key, value in row.items():
			end = "" if i == size else ","
			if isinstance(value, list):
				value = " / ".join([str(item) for item in value])
			else:
				value = value if value.isdigit() else '"%s"' % value
			outputFile.write('\t\t\t"%s": %s%s\n' % (key, value, end))
			i += 1
		# Write the field list closing
		outputFile.write('\t\t}\n')
		# Write the element ending bracket
		outputFile.write('\t}%s\n' % ("," if pk < csvSize else ""))
	# Write the json list closing
	outputFile.write(']\n')
	# Close file handlers
	fileHandle.close()
	outputFile.close()


def datetime2str(datetime):
	return unicode(datetime)


def getEmailSender():
	return "contact@gamezord.com"


def getEmailReceiver():
	return "draken.emb@gmail.com"


def ip2Num(ip):
	"""
	This function requires no imports and is faster than ip2Num, but
	"""
	parts = ip.strip().split('.')
	return int(parts[0]) * 2 ** 24 + int(parts[1]) * 2 ** 16 + int(parts[2]) * 2 ** 8 + int(parts[3])


def ip2Number(ip):
	return struct.unpack("!L", socket.inet_aton(ip))[0]


def normalizeString(string, spaceSub="+", cutPrefix=False):
	normalString = ""
	string = string.lower()
	valid = u"0123456789abcdefghijklmnopqrstuvwxyz_"
	# Removes the word "THE" and trailing whitespace from the start of strings
	if cutPrefix and string.lower().startswith(u"the"):
		string = string[3:].strip()
	for char in string:
		if char in valid:
			normalString += char
		elif char == spaceSub:
			normalString += spaceSub
		elif char in u"áããâä":
			normalString += "a"
		elif char in u"éèẽêë":
			normalString += "e"
		elif char in u"íìĩîï":
			normalString += "i"
		elif char in u"óòõôö":
			normalString += "o"
		elif char in u"úùũûü":
			normalString += "u"
		elif char in u"ćç":
			normalString += "c"
		elif char in u"ńǹñ":
			normalString += "n"
		elif char in u"ẃẁŵẅ":
			normalString += "w"
		elif char in u"ýỳỹŷÿ":
			normalString += "y"
		elif char == " ":
			normalString += spaceSub
	return normalString


def num2ip(ipnumber):
	return socket.inet_ntoa(struct.pack('!L', ipnumber))


def prepareMessage(text, title=None, redirect=None, error=True):
	message = { "text" : text }
	if title is not None:
		message["title"] = title
	if redirect is not None:
		message['redirect'] = redirect
	if error:
		message['status'] = 'alert alert-danger'
	else:
		message['status'] = 'alert alert-success'
	return { "message" : message }


def randomString(size, uppercase=True, numeric=True, extra=None, numericDensity=2):
	chars = u"abcdefghijklmnopqrstuvwxyz"
	if uppercase:
		chars += u"ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	if numeric:
		for i in range(0, numericDensity):
			chars += u"0123456789"
			del i
	if extra is not None:
		chars += extra
	string = ""
	charSize = len(chars)
	for i in range(0, size - 1):
		string += chars[randint(0, charSize - 1)]
		del i
	return string


def str2datetime(string):
	return parser.parse(string)


if __name__ == '__main__':
# 	print coord2num("40°45'35.232\"N")
# 	print coord2str(40.76)
# 	print coord2num("73°59'01.4\"W")
# 	print coord2str(-73.983722, False)
	print normalizeString(u"Teste")








