# power glove driver

import serial
import time
import win32com.client as com
import win32api

def initSerial(baud, sPort):
    ser = serial.Serial(
        port=sPort,
        baudrate=baud,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS
    )
    return ser

def read(ser):
    while 1:
        try:
            return ser.read(ser.inWaiting())[-10:]
        except:
            pass # device is waiting

def handlePacket(id, data, autoit):
    # move mouse
    print str(id) + "\t\t" + str(data)
    if id in [0, 1]:
        if abs(data) < 3:
            return # do nothing
        mx, my = win32api.GetCursorPos()
        if id == 0:
            # move mouse up/down
            #win32api.SetCursorPos((mx, my + data))
            autoit.MouseMove(mx, my + (-float(data) / 5.0), 0)
        else:
            # move mouse left/right
            #win32api.SetCursorPos((mx + data, my))
            autoit.MouseMove(mx + (float(data) / 5.0), my, 0)
    
            

def eventLoop(ser, autoit):
    while 1:
        packets = read(ser)
        #print format(ord(packets[0]), 'b') # binary dump
        for packet in packets: # iterate through last 10 bits recived
            packet = ord(packet)
            idPacket = int(packet / (2 ** 5))
            dataPacket = packet - (idPacket * (2 ** 5))
            if dataPacket > 16:
                dataPacket-=32
            handlePacket(idPacket, dataPacket, autoit)

        # data packet and id packet are now collected
        
        
def initConnection():
    # FT232R USB is flakey as hell
    print "Initializing Serial..."
    for port in range(1, 11):
        count = 0
        while 1:
            count += 1
            try:
                ser = initSerial(9800, "COM" + str(port))
            except:
                break
            time.sleep(0.1)
            for data in read(ser):
                time.sleep(0.3)
                data = ord(data)
                id = int(data / (2 ** 5))
                if (id in [0, 1]): # for now
                    print "Initialized After " + str(count) + " Attempts"
                    return ser
            ser.close() # unsucessful
            try:
                ser = initSerial(115200, "COM" + str(port))
            except:
                break
            ser.close()
    exit(1)
        
    
    



def main():
    ser = initConnection()
    autoit = com.Dispatch("AutoItX3.Control")
    eventLoop(ser, autoit)
    ser.close()
    

if __name__ == "__main__":
    main()
