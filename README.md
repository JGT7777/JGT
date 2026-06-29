# JGT
MollyKao Centinel

Description: 

I’m building a quadruped robot, with two motors on each leg that allow it to move in all directions and do movements that normally wouldn’t be possible. It’s controlled via WiFi through an ESP32. Since I don’t have any ESP32 yet, I haven’t been able to make the robot’s control page, but I do have the interface done in Python. My plan is that once everything is finished, I’ll convert the Python program to an Exe, and when I open it, it will emulate a Google to to open the web I created for control panel to move the robot. I’m doing this because it’s my first complete robot. Until now, I had made some very simple ones, and I focused more on programming, so I wanted to create my first large and well‑designed robot. The first thing I want to finish is the robot’s control panel, since I already printed the parts. I used the burned ESP32 I had as a model, and everything fits. The battery, from what I’ve seen, fits the dimensions, so from a design perspective, I don’t think I’ll need to touch it for now. Once I finished the basics, I had ambitious plans to add a camera and replace the ESP with a Raspberry, since I think the ESP32 can't handle an image recognition model. My intention would be that, besides being able to control it myself, it could act as a home sentry, move on its own, entertain my two cats, and monitor its surroundings, as well as have its own charging port. The most important thing is that creating this robot will give me knowledge I didn't have before, since I'll have to dive into the world of ESP and how to control it, AI, and even design. I know the final model sounds pretty ambitious, but now that the school year is over, I have the whole summer ahead of me.
Just finished and added the Wiring Diagram, also updated the CSV BOM.

----> I'm Spanish so maybe this text has little errors....         

Bill Of Materials ---------------------------------------------------------------------------                                                

| OLED 0.96" SSD1306 | Tiny 128x64 OLED for my robot (I2C, ESP32) | 1 | $6.00 | Amazon |                                                           
| Tattu 450mAh 2S XT30 LiPo | Small 2S LiPo (7.4V) for the robot | 1 | $16.50 | Amazon |                                                           
| Buck converter LM2596 | Steps battery voltage down to 5V | 1 | $1.10 | Amazon |                                                                  
| Electro DH Single-Pole Switch | Main power switch | 1 | $1.10 | Amazon |                                                                         
| WeMos ESP32-S2 Mini | Main controller, WiFi movement | 1 | $7.60 | Amazon |                                                                      

-----------------------------------------------Stasis BOM-------------------------------------                                                        
<img width="807" height="1051" alt="image" src="https://github.com/user-attachments/assets/ade7a9f7-0789-40cc-b7e1-a786114251d7" />


Coding/Project images ------------------------------------------------------------------------

<img width="1919" height="1077" alt="Captura de pantalla 2026-05-23 163557" src="https://github.com/user-attachments/assets/f96e5a2c-436c-4f21-9cb4-4a103e660ec5" />
<img width="1919" height="1078" alt="Captura de pantalla 2026-05-23 163545" src="https://github.com/user-attachments/assets/ac1f81d5-03fc-4d54-8242-272a8067cb01" />
<img width="1919" height="984" alt="Captura de pantalla 2026-05-21 213530" src="https://github.com/user-attachments/assets/27e980d7-2e11-4369-9b43-fad4f4c6bda4" />
<img width="1919" height="1075" alt="Captura de pantalla 2026-05-19 223320" src="https://github.com/user-attachments/assets/29820c3c-f315-40f8-9002-c30e92ef23ce" />
<img width="3000" height="4000" alt="IMG_20260315_221404" src="https://github.com/user-attachments/assets/199e5782-d03a-4599-8425-b50ce175e075" />




