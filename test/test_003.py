'''
Created on 8/29/2016

@author: ghou
'''


def paser(value):
    curPos = 0
    inQuote = False
    curChunk = None
    valueLen = len(value)
    print curPos, '111', valueLen, value
    while curPos < valueLen:
        ch = value[curPos]
        if ch == "\'":
            if (curPos < valueLen and value[curPos] == "\'"):
                curPos += 1
            inQuote = not inQuote
        elif ch == "{":
            if inQuote:
                continue
            argQuote = False
            while curPos < valueLen:
                ch = valueLen[curPos]
                if ch == "\'":
                    if curPos < valueLen and ch == "\'":
                        curPos += 1
                    else:
                        argQuote = not argQuote
                else:
                    if not argQuote and ch == '}':
                        break
            if ch != '}':
                raise Exception("Invalid message format - { not start of valid argument" + value, curPos)     
        elif ch in ['\n', '\r', '\\', '"']:
            break
        else:
            break
        curPos += 1
    if inQuote:
        raise Exception("Unterminated single quote: " + value, valueLen)    
 
            
def excape_char(value):
    excapeChar = "* . ? + $ ^ [ ] ( ) { } | \ /"
    excapeList = excapeChar.split(" ")
    for char in excapeList:
        if char in value:
            replaceChar = "\\%s" % char
            value = value.replace(char, replaceChar)
    return value


if __name__ == '__main__':
#     paser("'{'{0}'}'")
    value = 'adadad.sdad*dada<'
    print excape_char(value)