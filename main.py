from machine import Pin, ADC
import time

# Define GPIO pins for the traffic lights
# Westbound
west_red = Pin(0, Pin.OUT)
west_amber = Pin(1, Pin.OUT)
west_green = Pin(2, Pin.OUT)

# Northbound
north_red = Pin(28, Pin.OUT)
north_amber = Pin(21, Pin.OUT)
north_green = Pin(26, Pin.OUT)

# Southbound
south_red = Pin(3, Pin.OUT)
south_amber = Pin(5, Pin.OUT)
south_green = Pin(15, Pin.OUT)

# Eastbound
east_red = Pin(22, Pin.OUT)
east_amber = Pin(20, Pin.OUT)
east_green = Pin(19, Pin.OUT)

# Define pin for LDR
ldr = ADC(Pin(27))  # LDR connected to GPIO 27

# Threshold for LDR 
LIGHT_THRESHOLD = 500

# Function to run the traffic light sequence
def traffic_light_sequence():
    while True:
        ldr_value = ldr.read_u16()  # Read LDR value
        
        if ldr_value < LIGHT_THRESHOLD: 
             # NIGHT TIME
            # Step 1: Westbound Green, Eastbound Red
            west_green.on()
            east_red.on()
            north_red.on()
            south_red.on()
            time.sleep(8)  # Longer green duration at night
            west_green.off()

            # Step 2: Westbound Amber
            west_amber.on()
            time.sleep(3)  # Longer amber duration at night
            west_amber.off()

            # Step 3: North/South Green, East/West Red
            north_green.on()
            south_green.on()
            west_red.on()
            east_red.on()
            time.sleep(8)  # Longer green duration at night
            north_green.off()
            south_green.off()

            # Step 4: North/South Amber
            north_amber.on()
            south_amber.on()
            time.sleep(3)  # Longer amber duration at night
            north_amber.off()
            south_amber.off()

            # Step 5: Eastbound Green, Westbound Red
            east_green.on()
            west_red.on()
            north_red.on()
            south_red.on()
            time.sleep(8)  # Longer green duration at night
            east_green.off()

            # Step 6: Eastbound Amber
            east_amber.on()
            time.sleep(3)  # Longer amber duration at night
            east_amber.off()

        else: 
             # DAY TIME
            # Step 1: Westbound Green, Eastbound Red
            west_green.on()
            east_red.on()
            north_red.on()
            south_red.on()
            time.sleep(5)  # Normal green duration
            west_green.off()

            # Step 2: Westbound Amber
            west_amber.on()
            time.sleep(2)  # Normal amber duration
            west_amber.off()

            # Step 3: North/South Green, East/West Red
            north_green.on()
            south_green.on()
            west_red.on()
            east_red.on()
            time.sleep(5)  # Normal green duration
            north_green.off()
            south_green.off()

            # Step 4: North/South Amber
            north_amber.on()
            south_amber.on()
            time.sleep(2)  # Normal amber duration
            north_amber.off()
            south_amber.off()

            # Step 5: Eastbound Green, Westbound Red
            east_green.on()
            west_red.on()
            north_red.on()
            south_red.on()
            time.sleep(5)  # Normal green duration
            east_green.off()

            # Step 6: Eastbound Amber
            east_amber.on()
            time.sleep(2)  # Normal amber duration
            east_amber.off()

# Start the traffic light sequence
traffic_light_sequence()