from pymavlink import mavutil

# Create a connection to the Pixhawk
master = mavutil.mavlink_connection('/dev/ttyACM0', baud=921600)

while True:
    msg = master.recv_match(type='GPS_RAW_INT', blocking=True)
    print(f"GPS Data: {msg}")
