# import sys
# print('hello python and vs code')

# print(sys.path)
import string

longstring = 'g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr\'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj'
newstring = []
for i, item in enumerate(longstring):
    if item.isalpha():
        asc = ord(item)
        converted = asc + 2
        new = chr(converted)
        if new.isalpha():    
            newstring.append(new)
        elif item == 'y':
            newstring.append('a')
        elif item == 'z':
            newstring.append('b')
        
    else:
        newstring.append(item)

print(''.join(newstring))

# dict = 
table = str.maketrans('abcdefghijklmnopqrstuvwxyz','cdefghijklmnopqrstuvwxyzab')
mmm = longstring.translate(table)
print('2nd', mmm)

