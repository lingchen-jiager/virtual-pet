from machine import Pin,SPI
import ssd1306a  #其实就是官方的ssd1306，这里ssd1306a是因为我对这个文件做了简单的改动来让其支持中文，加个a以示区分。
import font,framebuf,utime
hspi = SPI(1,baudrate=80000000,polarity=0,phase=0)
display = ssd1306a.SSD1306_SPI(128,64,hspi,Pin(5),Pin(4),Pin(16))
display.init_display()
#display.text('Hello,World',1,1)  #显示字
#display.draw_chinese_fast('天气',2,0)
#display.draw_chinese('天气多云',6,0)

with open("./28.pbm", 'rb') as f:  #将此pbm图像上传到esp8266上
    data = bytearray(f.read().split(b"\r")[-1])   #这里本来可以用readline三次，然后再read，但是\r没被readline识别到，所以第一次readline就把整个数据全部读取了，所以采用这种方法。
    print(data)


    
fbuf = framebuf.FrameBuffer(data, 128, 64, framebuf.MONO_HLSB)      

display.invert(0)
display.blit(fbuf, 0, 0)
display.show()
