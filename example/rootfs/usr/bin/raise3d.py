
import hashlib
import time
import json
import urllib3

password = "7ad41f"

ip = "192.168.110.25"
port = "10800"
token = ""

class raise3d:
    def requestHttp(self, url):
        http = urllib3.PoolManager()
        response = http.request('GET', url)
        data = response.data
        values = json.loads(data)
        return values
        
    def calc_hash(self, plain):
        hash = hashlib.sha1(plain.encode('utf-8')).hexdigest()
        print (hash)
        hash = hashlib.md5(hash.encode('utf-8')).hexdigest()
        print (hash)
        return hash
    
    def getTime(self):
        millis_since_epoch = time.time_ns() // 1000000
        return str(millis_since_epoch)
        
        
    def getLogin(self):
        global ip
        global port
        global password
        global token

        
        time = self.getTime()
        #time = "1503477369615"
        #password_1 = "123456"
        plain = "password=" + password +"&timestamp=" + time 
        print (plain)
        hash = self.calc_hash(plain)
        url =  ip + ":" + port + "/v1/login?sign=" + hash + "&timestamp=" + time
        print(url)
        json = self.requestHttp(url)
        print (json)
        
        if json["status"] == 1:
            token = json["data"]["token"]
            print(token)
        
        
        
    def getInfo(self):
        global token  
        
        url =  ip + ":" + port + "/v1/printer/system?token=" + token
        print(url)
        json = self.requestHttp(url)
        print (json)
        
    def getPrinterStatus(self):
        global token  
        
        url =  ip + ":" + port + "/v1/printer/runningstatus?token=" + token
        print(url)
        json = self.requestHttp(url)
        print (json)

    def getCurrentJob(self):
        global token  
        
        url =  ip + ":" + port + "/v1/job/currentjob?token=" + token
        print(url)
        json = self.requestHttp(url)
        print (json)
        

        
#md5(sha1("password=123456xtamp=now"))
main = raise3d()

main.getLogin()
main.getInfo()
main.getPrinterStatus()
main.getCurrentJob()
