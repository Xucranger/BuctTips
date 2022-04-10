import win32con
import win32gui
import win32clipboard as w
import time
from random import choice
from random import randrange
import datetime

class sendMsg():
    def __init__(self,receiver,msg):
        self.receiver=receiver
        self.msg=msg
        self.setText()
    #设置剪贴版内容
    def setText(self):
        w.OpenClipboard()
        w.EmptyClipboard()
        w.SetClipboardData(win32con.CF_UNICODETEXT, self.msg)
        w.CloseClipboard()
    #发送消息
    def sendmsg(self):
        qq=win32gui.FindWindow(None,self.receiver)
        win32gui.SendMessage(qq,win32con.WM_PASTE , 0, 0)
        win32gui.SendMessage(qq, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
        print("sucessfuly send",self.msg)

def getmessage(fileName):
    f=open(fileName,'r',encoding='utf-8')
    lines=f.readlines()
    f.close()
    return choice(lines)

def main():
    receiver='大佬游戏分享群'#这里填入接收者的备注名
    while True:
        time1=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        # print(time1)
        hour=time1[11:13]
        minnute = time1[14:16]
        second = time1[17:19]
        # print(hour,minnute,second)

       
        # if int(hour)%2==0 and minnute=='00' and second=='30':
        if second=='30':
            print(time1)
            # msg = getmessage('C:\\Users\\Administrator\\Desktop\\message.txt')
            print(time1)
            msg = '探索五行草原'
            qq = sendMsg(receiver, msg)
            qq.sendmsg()
            time.sleep(50)
        # 测试案例  每5秒钟发送一次消息
        # if int(second)%5==0:
        #     msg = '时间:' + time1 + ',系统运行正常！'
        #     qq = sendMsg(receiver, msg)
        #     qq.sendmsg()
        #     time.sleep(3)

if __name__ == '__main__':
    main()

