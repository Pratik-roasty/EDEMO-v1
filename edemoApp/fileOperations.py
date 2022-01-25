def fileRead(user):
    f_read=open("edemoApp/auth_data.txt","r")
    for data in f_read.readlines():
        dataList=data.split()
        if len(data)==0:
            break
        if dataList[3]==user:
            return False
    return True
    f_read.close()

def fileWrite(data):
    f_write=open("edemoApp/auth_data.txt","a")
    dataString=""
    for i in data:
        dataString=dataString+i+" "

    dataString=dataString+"\n"
    f_write.write(dataString)
    f_write.close()
