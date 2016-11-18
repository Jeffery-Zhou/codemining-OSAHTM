from JSParser import Parser
import codecs
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

__author__ = 'Robur'


# file = open('jssrc/script.js')
file = codecs.open('jssrc/script.js', 'r')

js = file.read()
file.close()

parser = Parser()
parser.src = js

tree = parser.buildAST()

