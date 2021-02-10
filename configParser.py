
from configparser import ConfigParser, ExtendedInterpolation
parser = ConfigParser(interpolation=ExtendedInterpolation())

#import ConfigParser as parserparser = ConfigParser(interpolation=ExtendedInterpolation())
#
class Dog:
    kind = 'canine'         # class variable shared by all instances
    def __init__(self, name):
        self.name = name    # instance variable unique to each instance


d = Dog('Fido')
e = Dog('Buddy')

# print(d.kind)
# print(e.kind)
# print(d.name)
# print(e.name)


class Config:
    def __init__(self,filename):
        #self.filename = filename
        parser.read(filename)
        config_sections = parser.sections()
        for row_section in config_sections:
            #print(row_section)
            self.database = "data2"
            
#            code = compile('self.database = "data2"', "<string>", "exec")
#            print(code)
#            config_section_keys = list(parser.items(row_section))
#            for row_key in config_section_keys:
#                print(row_key[0])
#code = compile('def foo(self): print(“bar”)', "<string>", "exec")
c1 = Config('config.ini')
print(c1.database)
    # def database(self):
    #     return 'database'
    # def tns(self):
    #     return parser['database']['tns']

# class Database:
#     def __init__(self,filename):
#         parser.read(filename)
#         #self.tns = parser['database']['tns']
#         self.database_keys = dict(parser.items('database'))
#         # for row_key in config_section_keys:
#         #      self.key = ' ' + row_key[0] + '=' + row_key[1]



##################################################################
class Table:
    def __init__(self, l, w, h):
        self.length = l
        self.width = w
        self.height = h
class KitchenTable(Table):
    def setPlaces(self, p):
        self.places = p
class DeskTable(Table):
    def square(self):
        return self.width * self.length
kt1 = KitchenTable(100,50,80)
kt1.setPlaces(4)
#print(kt1.places)
##################################################################

#
#     def get_value(section,key):
#         return parser[section][key]
# #    parser.read('config')
#     class database:
#         tns = 0 #get_value('database','tns') #filename#parser['database']['tns']
#
#         def __config():
#             parser.read('config.ini')
#             config_sections = parser.sections()
#             for row_section in config_sections:
#                 print('[' + row_section + ']')
#                 config_section_keys = list(parser.items(row_section))
#                 for row_key in config_section_keys:
#                     print(' ' + row_key[0] + '=' + row_key[1])
#
#
# def rconfig(section,key):
#     parser.read('config.ini')
#     return parser[section][key]
#
# def o_config():
#     parser.read('config.ini')
#     config_sections=parser.sections()
#     for row_section in parser_sections:
#         print('['+row_section+']')
#         parser_section_keys=list(parser.items(row_section))
#         for row_key in config_section_keys:
#             print(' '+row_key[0]+'='+row_key[1])

#print (config.read('config.ini'))
#print(config.database.tns)
#pri''nt (config.__config())
#rconfig('database', 'tns'))
#print (config_.sections())
# print (config('database','tns'))
# print (config('database','user'))
# print (config('database','pass'))
# print (config('setting','ip'))
# print (config('setting','url'))
