# Problem 19

days_30 = [4, 6, 9, 11]
days_31 = [1, 3, 5, 7, 8, 10, 12]
days_28 = [2]

cur_year = 1900
cur_day = 1
cur_month = 1
days_in_month = 31
day_of_month = 1

num_of_sundays = 0

while cur_year < 2001:
	
	while cur_month < 13:
		
		if cur_month in days_30:
			days_in_month = 30
		
		elif cur_month in days_31:
			days_in_month = 31
		
		elif cur_month in days_28:
			days_in_month = 28
			if (cur_year % 4) == 0:
				if (cur_year % 100) != 0 or (cur_year % 400) == 0:
					days_in_month += 1
		
		while day_of_month <= days_in_month:
			
			if day_of_month == 1 and (cur_day % 7) == 0 and cur_year > 1900:
				num_of_sundays += 1
			
			day_of_month += 1
			cur_day += 1
		
		cur_month += 1
		day_of_month = 1
	
	cur_month = 1
	cur_year += 1

print num_of_sundays
