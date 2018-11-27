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

## System Overview
<p align="center"> 
<img  src="https://github.com/ShuDiamonds/Security-camera/blob/master/image/Securitycamera_SystemOverview.svg.png"  title="system overview">
</p>

## Pump
<p align="center"> 
<img  src="https://github.com/ShuDiamonds/PUMP-Control/blob/master/pictures/keedox-dc30a-1230-12v-dc-2-phase-cpu-cooling-car-brushless-water-pump-waterproof-submersible_3224360.jpg"  title="pump pic">
</p>

## Moter driver circuit
### circuit diagram
<p align="center"> 
<img  src="https://github.com/ShuDiamonds/PUMP-Control/blob/master/pictures/%E3%83%A2%E3%83%BC%E3%82%BF%E5%88%B6%E5%BE%A1%E5%9B%9E%E8%B7%AF.png"  title="moter driver circuit">
</p>

### wiring to breadboard
<p align="center"> 
<img  src="https://github.com/ShuDiamonds/PUMP-Control/blob/master/pictures/bredboard2.jpg"  title="moter driver bredboard">
</p>

<p align="center"> 
<img  src="https://github.com/ShuDiamonds/PUMP-Control/blob/master/pictures/%E5%9B%9E%E8%B7%AF%E5%9B%B3%20-%20%E3%82%B3%E3%83%94%E3%83%BC.jpg"  title="Upgraded">
</p>


## Requirement  
* Raspberry pi 3  
* ubuntu16.04  
* Python 3.x  
* Opencv
* Web Camera x2
 <p align="center"> 
<img  src="https://github.com/ShuDiamonds/Security-camera/blob/master/image/IMG_20180927_215417.jpg"  title="setting" width="480">
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
* [Machine Learning data](https://github.com/topics/shu-machine-learning-data)

## Author
  [ShuDiamonds](https://github.com/ShuDiamonds)
