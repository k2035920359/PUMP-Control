# PUMP-Control
This is a project to control a DC pump with PWM on Raspberry pi.
The repositroy includes a design about a motor driver curcuit, control programs, pump.
<div style="; position: relative;top:0; left: 100px;"></div>
<img src="https://github.com/ShuDiamonds/PUMP-Control/blob/master/pictures/pumpaction.gif"  width="320">

## Requirement  
* Raspberry pi 3  
* ubuntu Mate16.04  
* Python 3.x  
* wiringpi
* [DC pump](https://www.amazon.co.jp/dc12v-%E6%B0%B4%E4%B8%AD%E3%83%9D%E3%83%B3%E3%83%97-DC30A-1230-%E3%83%8F%E3%82%A4%E3%83%91%E3%83%AF%E3%83%BC-%E7%9B%B4%E6%B5%81DC5V%EF%BD%9EDC12V/dp/B07BGHC6YR/ref=sr_1_1_sspa?s=diy&ie=UTF8&qid=1543290060&sr=1-1-spons&keywords=dc30a1230&psc=1)


## System Overview
<p align="center"> 
<img  src="https://github.com/ShuDiamonds/PUMP-Control/blob/master/pictures/%E3%82%B7%E3%82%B9%E3%83%86%E3%83%A0%E6%A6%82%E8%A6%81%E5%9B%B3.jpg"  title="system overview" width="640">
</p>

## Pump
<p align="center"> 
<img  src="https://github.com/ShuDiamonds/PUMP-Control/blob/master/pictures/keedox-dc30a-1230-12v-dc-2-phase-cpu-cooling-car-brushless-water-pump-waterproof-submersible_3224360.jpg"  title="pump pic" width="320">
</p>

### datasheet 
We used this [DC pump](https://www.amazon.co.jp/dc12v-%E6%B0%B4%E4%B8%AD%E3%83%9D%E3%83%B3%E3%83%97-DC30A-1230-%E3%83%8F%E3%82%A4%E3%83%91%E3%83%AF%E3%83%BC-%E7%9B%B4%E6%B5%81DC5V%EF%BD%9EDC12V/dp/B07BGHC6YR/ref=sr_1_1_sspa?s=diy&ie=UTF8&qid=1543290060&sr=1-1-spons&keywords=dc30a1230&psc=1).
### features

* Model number:DC30A-1230
* Voltage:DC5V-12V
* Rated current:0.35A
* Max Volumetric flow rate:4L/min
* Rated power consumption:4.2W


<p align="center"> 
<img  src="https://github.com/ShuDiamonds/PUMP-Control/blob/master/pictures/cad.jpg"  title="pump design">
<img  src="https://github.com/ShuDiamonds/PUMP-Control/blob/master/pictures/t7kKsYOFSISV._UX300_TTW_.jpg"  title="datasheet">
</p>



## Motor driver circuit
### circuit diagram
<p align="center"> 
<img  src="https://github.com/ShuDiamonds/PUMP-Control/blob/master/pictures/%E3%83%A2%E3%83%BC%E3%82%BF%E5%88%B6%E5%BE%A1%E5%9B%9E%E8%B7%AF.png"  title="Motor driver circuit">
</p>

### electronic component
* Breadboard
* Photo coupler:EL817
* N-channel MOSFET:IRF840
* Resistors:150 ohm, 1k ohm, 1k ohm
* wire

### wiring to breadboard
<p align="center"> 
<img  src="https://github.com/ShuDiamonds/PUMP-Control/blob/master/pictures/bredboard2.jpg"  title="Motor driver bredboard" width="320">
</p>

<p align="center"> 
<img  src="https://github.com/ShuDiamonds/PUMP-Control/blob/master/pictures/%E5%9B%9E%E8%B7%AF%E5%9B%B3%20-%20%E3%82%B3%E3%83%94%E3%83%BC.jpg"  title="Upgraded" width="320">
</p>


## Input Volume
See [here](https://github.com/ShuDiamonds/PCF8591) written about PCF8591.
And do not forget to enable i2c of raspi


## Usage
### Basic Example
```bash
$ python3 flowdemo.py
```

### memo
we didn't use PWM of wiringpi, because it conflict the program using PCF8591. so that we made cheap software PWM program.


## Licence

  [MIT](https://github.com/tcnksm/tool/blob/master/LICENCE)

## Related Articles
* [embedded](https://github.com/topics/shu-embedded-systems)

## Author
  [ShuDiamonds](https://github.com/ShuDiamonds)
