import win32api, win32con
import subprocess
import pyautogui
from pywinauto.application import Application
class keyboardControls:


    def __init__(self) -> None:
        pass

    def getWords(number):
        array_commands = "{SCROLLLOCK}", "{VK_SPACE}", "{VK_LSHIFT}", "{VK_PAUSE}", "{VK_MODECHANGE}", "{BACK}", "{VK_HOME}", "{F23}", "{F22}", "{F21}", "{F20}", "{VK_HANGEUL}", "{VK_KANJI}", "{VK_RIGHT}", "{BS}", "{HOME}", "{VK_F4}", "{VK_ACCEPT}", "{VK_F18}", "{VK_SNAPSHOT}", "{VK_PA1}", "{VK_NONAME}", "{VK_LCONTROL}", "{ZOOM}", "{VK_ATTN}", "{VK_F10}", "{VK_F22}", "{VK_F23}", "{VK_F20}", "{VK_F21}", "{VK_SCROLL}", "{TAB}", "{VK_F11}", "{VK_END}", "{LEFT}", "{VK_UP}", "{NUMLOCK}", "{VK_APPS}", "{PGUP}", "{VK_F8}", "{VK_CONTROL}", "{VK_LEFT}", "{PRTSC}", "{VK_NUMPAD4}", "{CAPSLOCK}", "{VK_CONVERT}", "{VK_PROCESSKEY}", "{ENTER}", "{VK_SEPARATOR}", "{VK_RWIN}", "{VK_LMENU}", "{VK_NEXT}", "{F1}", "{F2}", "{F3}", "{F4}", "{F5}", "{F6}", "{F7}", "{F8}", "{F9}", "{VK_ADD}", "{VK_RCONTROL}", "{VK_RETURN}", "{BREAK}", "{VK_NUMPAD9}", "{VK_NUMPAD8}", "{RWIN}", "{VK_KANA}", "{PGDN}", "{VK_NUMPAD3}", "{DEL}", "{VK_NUMPAD1}", "{VK_NUMPAD0}", "{VK_NUMPAD7}", "{VK_NUMPAD6}", "{VK_NUMPAD5}", "{DELETE}", "{VK_PRIOR}", "{VK_SUBTRACT}", "{HELP}", "{VK_PRINT}", "{VK_BACK}", "{CAP}", "{VK_RBUTTON}", "{VK_RSHIFT}", "{VK_LWIN}", "{DOWN}", "{VK_HELP}", "{VK_NONCONVERT}", "{BACKSPACE}", "{VK_SELECT}", "{VK_TAB}", "{VK_HANJA}", "{VK_NUMPAD2}", "{INSERT}", "{VK_F9}", "{VK_DECIMAL}", "{VK_FINAL}", "{VK_EXSEL}", "{RMENU}", "{VK_F3}", "{VK_F2}", "{VK_F1}", "{VK_F7}", "{VK_F6}", "{VK_F5}", "{VK_CRSEL}", "{VK_SHIFT}", "{VK_EREOF}", "{VK_CANCEL}", "{VK_DELETE}", "{VK_HANGUL}", "{VK_MBUTTON}", "{VK_NUMLOCK}", "{VK_CLEAR}", "{END}", "{VK_MENU}", "{SPACE}", "{BKSP}", "{VK_INSERT}", "{F18}", "{F19}", "{ESC}", "{VK_MULTIPLY}", "{F12}", "{F13}", "{F10}", "{F11}", "{F16}", "{F17}", "{F14}", "{F15}", "{F24}", "{RIGHT}", "{VK_F24}", "{VK_CAPITAL}", "{VK_LBUTTON}", "{VK_OEM_CLEAR}", "{VK_ESCAPE}", "{UP}", "{VK_DIVIDE}", "{INS}", "{VK_JUNJA}", "{VK_F19}", "{VK_EXECUTE}", "{VK_PLAY}", "{VK_RMENU}", "{VK_F13}", "{VK_F12}", "{LWIN}", "{VK_DOWN}", "{VK_F17}", "{VK_F16}", "{VK_F15}", "{VK_F14}"
        return array_commands[number], len(array_commands)


    # @staticmethod
    # def singleCommand(message):
            
    @staticmethod    
    def click(cli):
            
            # this tries to get the number and take out the click
            spl = str(cli[0]).split(" ")[1]
            # print(spl)
            stripy = cli[1]
            x = int(spl)
            y = int(stripy)
            if x > 1876 and y < 48:
                print("no")
                pass
            else:
                win32api.SetCursorPos((x,y))
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)

    @staticmethod
    def convertComment(type,message):
        #1 - type , 2 - click - 3 shortcut
        # splitCommand = str(message).split(" ")[1]
        
        if "+" in message and len(message) >1 :
            # print("shortcut")
            array_AllStrings = []
            if str(message) == "ctrl++":
                pass
            else:
                splitPluses = str(message).split("+")
                if "ctrl" in message and "alt" in message and "delete" in message:
                    pass
                elif "ctrl" in message and "shift" in message and "c" in message:
                    pass
                elif "alt" in message and "f4" in message:
                    pass
                for count,value in enumerate(splitPluses):
                    if splitPluses[count] != "ctrl" and splitPluses[count] != "shift" and splitPluses[count] != "alt":
                        wordArray = keyboardControls.getWords(0)[1]
                        for i in range(wordArray):
                            currentWordInArray = keyboardControls.getWords(i)[0]
                            # print(currentWordInArray)
                            if message.upper() in currentWordInArray:
                                string = currentWordInArray
                                # print(message)
                                # print(currentWordInArray)
                                array_AllStrings.append(string)

                        
                    else:
                        array_AllStrings.append(value)
                joinString = "".join(splitPluses)
                repCtrl = joinString.replace("ctrl","^")
                repShift = repCtrl.replace("shift","+")
                repAlt = repShift.replace("alt","%")
                return repAlt
        else:
            print("check")
            # if message =="home" or message =="esc":
            return message
            # else:
            #     for count,value in enumerate(message):
            #         if message != "ctrl" and message != "shift" and message != "alt":
            #             wordArray = keyboardControls.getWords(0)[1]
            #             for i in range(wordArray):
            #                 currentWordInArray = keyboardControls.getWords(i)[0]
            #                 # print(currentWordInArray)
                            
            #                 if  message.upper() in currentWordInArray:
            #                     print("found")
            #                     string = currentWordInArray
            #                     return string
                                
            #             else:
            #                 #will be a click or type

            #                 return message

