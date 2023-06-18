Temperature sensors:(SENSOR DONE) measure temp of surrunding enviornment and rooms

Light sensors:(SENSOR DONE) Measere the light in room and change the light based on occupancy and surroungidng light.

Motion sensors:(SENSOR DONE) detect occupancies and movements

Humidity sensors:(SENSOR DONE) monitor moisture in the air and rooms

Carbon dioxide/other gases sensors(SENSOR DONE): measure teh harmulf gass level to make more or less ventilation accordingly.

some type of elctric parameters measure and storing device:  to measeure the electric usage and t change it. Can be done by-
     1- hack multimeter(hard,cheap)
     2- buy a multimeter with this function(expensive,easy)
     3- get another deivce to do this thing(no clue about it)

1stWeek vyom- Prepare adivice to display values on lcd of sensors.
1-2 week vignesh- Prepaer a modle code with model data on how it will work.
NEXT- INTERGRATE THEM.
how we can integrete - we can use something with bluetooth or any other transmittion  that goes to an android phone then maybey we can  use android development to add python with it or somehting to process or we coude transmitt to a laptop or pc acitng as a server with pyhton code in it
Temperature and humidity-DHT11 SENSOR
Light -LDR sensor
Motion- PIR sensor
carbon DIOXIDE- MQ-135
SERACH FOR 2 WAY COMMUNICATION BETWEEN PYTHON AND ARDUINO
Fan ON/OFF if co2 and temp.
Light On/off- LDR and motion sensor.
Widnow open witservo - if co2
AC- if temp
Communication for python and arduino- 1. making a simple encryption with eirther python or arduino so that it does not interfere with sensor values.(BETTER)
                                      2. If bluetooth then we need to connec to bluetooth through python thhen process the data.
Giving data for 6 hours-
Motion sensor- How many times motion sensed in 1 hour
Humidity- AVG value in 1 hour
Temp- Avg in 1 hour
CO2 -  avg AnlgoValue  in hour, Min and max value (ANALOG) to set percentage for the whole 6 hours
Light level- avg every 1 hour(analog), Min-cover sensor, Max- bright flashlight
Measure electricity consumption-  measureing current with arduino with ACS712 hall effect current sensor and then mesuring voltage with a voltage divider circuit with a 20k and a 100k resitor to get the power. Then making a clock in python to obtain energy=P*T   P=I*V.


General Intro
//vig
Today we are with our project G20 EnergySathi.//vig It is a new way of empowering energy effiency by collecting, analyzing and optimising data related to energy. This project aims to minimise the energy consumptions of a building to conserve our resources and promote sustainable development.
//vig But what is the problem?? -//vig 
Acording to a study conducted by the berau of energy efficiency (BEE) in India , it is estimated that aroud 19 % of toatal energy consumption is wasted in the industrial sector and around 20% to 30% in residential araes.//vig this is due to inefficent use of HVAC nad lighting systems.This path of enviornmental degradation is taking us towards a climate crisis. Some other problems are also listed on the slide.//vig
Model showcasing --> Power (I, V), Photoresister, Motion, CO2, Humidity, Temperaeture
By measuring all these parameters that co relate with energy consumptions, we can improve automation of HCAV systems and empower energy efficiency to minimise energy consumption.
//vig Not only this, we are integarating this with a python scipt to make it smarter and more efficient with AI and ML. 
// softaware
Take a look at how AI and machine learning part works through python integration.
The sensor reading are taken as data in an excel sheet for forcasting and analysing patterns with the machine learning model displayed here. On the code shown here, the model is trained and tested. The results of prediction are shown here on the graph. As we see, the predictions and actual reading are pretty close at their timestamps. When we want to forecast power consumptions and other readings later, the data and timestamps can be put in the model and it would predict them for us.
//software
//vig
our project g20 energy sathi abides by many g20 and fln principles as listed on the slide. //vig We want to use sustainable development ,energy efficiency and collaboration  toweards a common gooal of minimizing energy consumtion in buildings.//vig
by implementation of g20 energy sathi we will be excpectuon a 15% to 30% reduction in energy wastage. This is a statistical evidence from a case study condected by american counci for energy efficient economy. Now with our own G20 energy sathin inida will too see result like or better than this
Even thogh this sathi covers a vast number of paprameters it can still be imporved. Like it can have more parameters with water consumptiono, equipment efficiency and solare readiation. //vig Or we can improve our softare procesing by inculduing fators like rcommended energy consumtion from g20 and fln or improving our ml and ai algorithms.//vig
This was our world changing project g20 energy sathi - //both empowering energy efiiciency.//both
