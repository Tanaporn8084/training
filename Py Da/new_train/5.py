income = 250_000
lowtaxland_rate = 0.05
ripoffland_rate = 0.43
#print((income * lowtaxland_rate) ,(income * ripoffland_rate))

print('Your income is',(income),'and you would pay', (lowtaxland_rate),'income in Lowtaxland or', (ripoffland_rate), 'income tax in Ripoffland.','You could save',(income * ripoffland_rate - income * lowtaxland_rate),'by paying taxes in Lowtaxland!')