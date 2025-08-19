flightA= ('Amsterdam', 'Dublin', 100)
flightB = ('Amsterdam', 'Rome', 140)
flightC = ('Rome', 'Warsaw', 130)
flightD = ('Minsk', 'Prague', 95)
flightE = ('Stockholm', 'Rome', 190)
flightF = ('Copenhagen', 'Paris', 120)
flightG = ('Madrid', 'Rome', 135)
flightH = ('Lisbon', 'Rome', 170)
flightI = ('Dublin', 'Rome', 170)
flights = [flightA, flightB, flightC, flightD, flightE, flightF, flightG, flightH, flightI]
 
if 'Rome' in [time[1] for time in flights]:
    print('There are flights to Rome!!!')
    connections = [time for time in flights if time[1] == 'Rome']
    average_flight_time = sum(time[2] for time in connections) / len(connections)
    print(f"{len(connections)} connections lead to Rome with an average flight time of {average_flight_time} minutes")