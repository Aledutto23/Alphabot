import requests
import time as vremya
#/api/v1/motors/left?pwm=x&time=t
#/api/v1/motors/right?pwm=y&time=t
#/api/v1/motors/both?pwmL=x&pwmR=y&time=t
def main():
    try:
        while True:
            vremya.sleep(0.3)
            r = requests.get('http://192.168.0.129:5000/api/v1/sensors/obstacles')  
            r = r.json()
            destra = r["right"] #1 c'è 0 non c'è
            sinistra = r["left"]

            while int(destra) == 0 and int(sinistra) == 0:
                r = requests.get('http://192.168.0.129:5000/api/v1/sensors/obstacles')  
                r = r.json()
                destra = r["right"] #1 c'è 0 non c'è
                sinistra = r["left"]
                pwmL = 33
                pwmR = 35
                time = 0.3
                r = requests.get(f'http://192.168.0.129:5000/api/v1/motors/both?pwmL={pwmL}&time={time}&pwmR={pwmR}')

            while int(destra) == 0 and int(sinistra) == 1:  #ostacolo sulla sinistra
                r = requests.get('http://192.168.0.129:5000/api/v1/sensors/obstacles')  
                r = r.json()
                destra = r["right"] #1 c'è 0 non c'è
                sinistra = r["left"]
                pwmL = 33
                pwmR = 0
                time = 0.2
                r = requests.get(f'http://192.168.0.129:5000/api/v1/motors/both?pwmL={pwmL}&time={time}&pwmR={pwmR}')

            while int(destra) == 1 and int(sinistra) == 0: #ostacolo sulla destra
                r = requests.get('http://192.168.0.129:5000/api/v1/sensors/obstacles')  
                r = r.json()
                destra = r["right"] #1 c'è 0 non c'è
                sinistra = r["left"]
                pwmL = 0
                pwmR = 33
                time = 0.3
                r = requests.get(f'http://192.168.0.129:5000/api/v1/motors/both?pwmL={pwmL}&time={time}&pwmR={pwmR}')
            
            while int(destra) == 1 and int(sinistra) == 1:
                r = requests.get('http://192.168.0.129:5000/api/v1/sensors/obstacles')  
                r = r.json()
                destra = r["right"] #1 c'è 0 non c'è
                sinistra = r["left"]
                pwmL = 33
                pwmR = 0
                time = 0.3
                r = requests.get(f'http://192.168.0.129:5000/api/v1/motors/both?pwmL={pwmL}&time={time}&pwmR={pwmR}')
                time = 0.4
                pwm = 33
                r = requests.get(f'http://192.168.0.129:5000/api/v1/motors/back?pwm={pwm}&time={time}')
                r = requests.get('http://192.168.0.129:5000/api/v1/sensors/obstacles')  
                r = r.json()
                destra = r["right"] #1 c'è 0 non c'è
                sinistra = r["left"]
                if int(destra) == 0 and int(sinistra) == 0:
                    break;
                elif int(destra) == 1 and int(sinistra) == 1:
                    r = requests.get('http://192.168.0.129:5000/api/v1/sensors/obstacles')  
                    r = r.json()
                    destra = r["right"] #1 c'è 0 non c'è
                    sinistra = r["left"]
                    pwmL = 0
                    pwmR = 33
                    time = 0.8
                    r = requests.get(f'http://192.168.0.129:5000/api/v1/motors/both?pwmL={pwmL}&time={time}&pwmR={pwmR}')
            


            
    except KeyboardInterrupt:
        print("programma finito")


if __name__ == "__main__":
    main()