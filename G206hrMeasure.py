import serial
import csv
import time
from datetime import datetime
import pytz

# Open the serial port
ser = serial.Serial('COM3', 9600)  # Replace 'COM5' with the appropriate port and baud rate

# Create or open the CSV file
csv_file = open('final_readings2.csv', 'w', newline='')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Timestamp(HMS) '+'Light(analog) '+'CO2(analog) '+'Temp(C) '+'Humid(%) '+'Motion(01) ' ])
try:
    while True:
        # Read sensor values from Arduino
        data = ser.readline().decode("utf-8")
        sensor_values = data.split()

        # Get current timestamp in IST with only the time
        ist = pytz.timezone('Asia/Kolkata')
        ist_time = datetime.now(ist).strftime('%H:%M:%S')

        # Write timestamp and sensor values to the CSV file
        row = [ist_time + " "+sensor_values[0]+" "+sensor_values[1]+" "+sensor_values[2]+" "+sensor_values[3]+" "+sensor_values[4]+" "]
        csv_writer.writerow(row)
        csv_file.flush()  # Optional: Forcefully write to the file immediately

except KeyboardInterrupt:
    print("Stopping the program...")

finally:
    # Close the CSV file and serial port
    csv_file.close()
    ser.close()
 