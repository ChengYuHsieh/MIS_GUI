import sys
import SmallSchedule_generator_demo
import time
import dailySchedule

worker_scale = 300
duty_scale = 500
skill_scale = 10
demand_scale = 1

def main():
	start_time = time.time()
	Data = SmallSchedule_generator_demo.main(worker_scale, duty_scale, skill_scale, demand_scale)
	end_time = time.time()
	time1 = end_time - start_time
	print("generate time: " + str(time1))
	dname1 = "inputForGreedy.txt"

	#algo1
	start_time = time.time()
	#Need rewrite
	output1 = dailySchedule.Greedy(Data["dutyList"], Data["empList"])
	#Need rewrite
	end_time = time.time()
	time1 = end_time - start_time
	print(time1)

	return output1


if __name__ == "__main__":
	main()