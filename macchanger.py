import subprocess
import argparse
process=argparse.ArgumentParser()
result=subprocess.run(["ls","/sys/class/net/"],capture_output=True,text=True)
if 'eth0' in result.stdout:
        print("eth0 interface found")
if 'wlan0' in result.stdout:
        print("wlan0 interface found")
process.add_argument("-i","--interface",dest="interface",help="choose an interface")
process.add_argument("-m","--mac",dest="mac",help="enter a mac address")
userinput=process.parse_args()
interface=userinput.interface
mac=userinput.mac
try:
        subprocess.call(["ifconfig",interface,"down"])
        subprocess.call(["ifconfig",interface,"hw","ether",mac])
        subprocess.call(["ifconfig",interface,"up"])
except:
        if interface=='eth0' or interface=='wlan0':
                print("enter a valid interface")
        print("An error occured ")
