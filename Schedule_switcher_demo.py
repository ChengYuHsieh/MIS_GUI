import sys
import Schedule_generator_demo
import sub1
import time

skill_scale = 10 #10
multiskill_scale = 20 #100
demand_scale = 50 #300

def main():
	start_time = time.time()
	Schedule_generator_demo.main(skill_scale, multiskill_scale, demand_scale)
	end_time = time.time()
	time1 = end_time - start_time
	print("generate time: " + str(time1))
	dname = "inputForLag.txt"


	#Lagrangian algo
	start_time = time.time()
	output = sub1.solve(dname)
	end_time = time.time()
	time1 = end_time - start_time
	print(time1)
	
	return output


if __name__ == "__main__":
	main()
