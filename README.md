# PUMP-Control
This is a project to control a DC pump with PWM on Raspberry pi.
The repositroy includes a design about a moter driver curcuit, control programs, pump.
<div style="; position: relative;top:0; left: 100px;"></div>
<img src="https://github.com/ShuDiamonds/PUMP-Control/blob/master/pictures/pumpaction.gif"  width="320">

## Main Features
* Strong Reduction of its SD memory occupation with `difference extraction` Technology.
* Reporting a daily bulletin through on Gmail.
* Supervise the [main program](https://github.com/ShuDiamonds/Security-camera/blob/master/demo/demo2.py) by [reporting.py](https://github.com/ShuDiamonds/Security-camera/blob/master/demo/reporting.py).
* Delete one week ago camera data automatically.

## Requirement  
* Raspberry pi 3  
* ubuntu Mate16.04  
* Python 3.x  
* wiringpi
* [DC pump](https://www.amazon.co.jp/dc12v-%E6%B0%B4%E4%B8%AD%E3%83%9D%E3%83%B3%E3%83%97-DC30A-1230-%E3%83%8F%E3%82%A4%E3%83%91%E3%83%AF%E3%83%BC-%E7%9B%B4%E6%B5%81DC5V%EF%BD%9EDC12V/dp/B07BGHC6YR/ref=sr_1_1_sspa?s=diy&ie=UTF8&qid=1543290060&sr=1-1-spons&keywords=dc30a1230&psc=1)


## System Overview
<p align="center"> 
<img  src="https://github.com/ShuDiamonds/Security-camera/blob/master/image/Securitycamera_SystemOverview.svg.png"  title="system overview">
</p>

## Pump
<p align="center"> 
<img  src="https://github.com/ShuDiamonds/PUMP-Control/blob/master/pictures/keedox-dc30a-1230-12v-dc-2-phase-cpu-cooling-car-brushless-water-pump-waterproof-submersible_3224360.jpg"  title="pump pic">
</p>
### datasheet 
We used this [DC pump](https://www.amazon.co.jp/dc12v-%E6%B0%B4%E4%B8%AD%E3%83%9D%E3%83%B3%E3%83%97-DC30A-1230-%E3%83%8F%E3%82%A4%E3%83%91%E3%83%AF%E3%83%BC-%E7%9B%B4%E6%B5%81DC5V%EF%BD%9EDC12V/dp/B07BGHC6YR/ref=sr_1_1_sspa?s=diy&ie=UTF8&qid=1543290060&sr=1-1-spons&keywords=dc30a1230&psc=1)
### features
* Model number:DC30A-1230
* Voltage:DC5V-12V
* Rated current:0.35A
* Max Volumetric flow rate:4L/min
* Rated power consumption:4.2W




## Moter driver circuit
### circuit diagram
<p align="center"> 
<img  src="https://github.com/ShuDiamonds/PUMP-Control/blob/master/pictures/%E3%83%A2%E3%83%BC%E3%82%BF%E5%88%B6%E5%BE%A1%E5%9B%9E%E8%B7%AF.png"  title="moter driver circuit">
</p>
### electronic component

### wiring to breadboard
<p align="center"> 
<img  src="https://github.com/ShuDiamonds/PUMP-Control/blob/master/pictures/bredboard2.jpg"  title="moter driver bredboard">
</p>

<p align="center"> 
<img  src="https://github.com/ShuDiamonds/PUMP-Control/blob/master/pictures/%E5%9B%9E%E8%B7%AF%E5%9B%B3%20-%20%E3%82%B3%E3%83%94%E3%83%BC.jpg"  title="Upgraded">
</p>



 
## Setting
###  demo2.py property
* image size
 adjust heght and width variables.

### reporting.py property
Set the email infomation to send a daily report through on gmail.
```
from_email = "senderhogehoge@gmail.com" # 送信元のアドレス
to_email = "receiverhogehoge@gmail.com" # 送りたい先のアドレス
username = "sender@gmail.com"           # Gmailのアドレス
password = "mygmailpassword"            # Gmailのパスワード
```
and you have to lower its Google Security level (if not doing that, you can't send email from gmail and recieve the security alart mail from google).

## Usage
### Basic Example
```bash
$ python3 demo2.py
```
### report program example
This program provides three function,Reporting on gmail,deleting one week ago camera data, program activity check (every one hour).

```bash
$ python3 reporting.py
```


## Licence

  [MIT](https://github.com/tcnksm/tool/blob/master/LICENCE)

## Related Articles
* [embedded](https://github.com/topics/shu-embedded-systems)

## Author
  [ShuDiamonds](https://github.com/ShuDiamonds)
