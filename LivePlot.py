import time
import serial
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def animate(i, dataList, ser):
    ser.write(b'g')                                     # Transmit the char 'g' to receive the Arduino data point
    arduinoData_string = ser.readline().decode('ascii') # Decode received Arduino data as a formatted string
    #print(i)                                           # 'i' is a incrementing variable based upon frames = x argument

    try:
        arduinoData_float = float(arduinoData_string)   # Convert to float
        dataList.append(arduinoData_float)              # Add to the list holding the fixed number of points to animate

    except:                                             # Pass if data point is bad                               
        pass

    dataList = dataList[-50:]                           
    
    ax.clear()                                          
    ax.plot(dataList)                                   # Plot new data frame
    
    ax.set_ylim([0, 1200])                              # Set Y axis limit of plot
    ax.set_title("Arduino Data")                        # Set title of figure
    ax.set_ylabel("Value")                              # Set title of y axis 

dataList = []                                           # Create empty list variable for later use
                                                        
fig = plt.figure()                                      
ax = fig.add_subplot(111)                               # Add subplot to main fig window

ser = serial.Serial("COM7", 9600)                       # Establish Serial object with COM port and BAUD rate to match Arduino Port/rate
time.sleep(2)                                           

                                                        # Matplotlib Animation Fuction that takes takes care of real time plot.
                                                         
ani = animation.FuncAnimation(fig, animate, frames=100, fargs=(dataList, ser), interval=100) 

plt.show()                                              
ser.close()                                             # Close Serial connection when plot is closed
