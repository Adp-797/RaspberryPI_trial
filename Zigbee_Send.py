from serial import Serial
 
# Enable USB Communication
ser = Serial('/dev/ttyUSB0', 9600,timeout=.5)
 
while True:
    ser.write('Hello User \r\n'.encode('utf-8'))         # write a Data
    print("Data Sent")
    #incoming = ser.readline().strip()
    #print 'Received Data : '+ incoming
