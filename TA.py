#Teaching Assistant
import threading
import time
import random

NUM_SEAT = 3
SLEEP_MAX = 5

# Semaphores
sem_stu = threading.Semaphore(0)
sem_ta = threading.Semaphore(1)

# Mutex
mutex = threading.Lock()

chair = [0] * NUM_SEAT
count = 0
next_seat = 0
next_teach = 0

def rand_sleep():
    time.sleep(random.randint(1, SLEEP_MAX))

def stu_programming(stu_id):
    global count, next_seat
    print(f"[stu] student {stu_id} is leaving for TA office")

    while True:
        rand_sleep()

        with mutex:
            if count < NUM_SEAT:
                chair[next_seat] = stu_id
                count += 1

                print(f"    [stu] student {stu_id} is waiting seated at hallway")
                print(f"waiting students: [1] {chair[0]} [2] {chair[1]} [3] {chair[2]}")

                next_seat = (next_seat + 1) % NUM_SEAT

                sem_stu.release()
                sem_ta.acquire()
            else:
                print(f"[stu] no more chairs. student {stu_id} is outside hallway and will be back later")

def ta_teaching():
    global count, next_teach
    while True:
        sem_stu.acquire()

        with mutex:
            print(f"        [ta] TA is teaching student {chair[next_teach]}")
            chair[next_teach] = 0
            count -= 1

            print(f"waiting students: [1] {chair[0]} [2] {chair[1]} [3] {chair[2]}")

            next_teach = (next_teach + 1) % NUM_SEAT

            rand_sleep()

            print("        [ta] teaching finish.")

        sem_ta.release()

# Get number of students from user
student_num = int(input("How many students? "))

if student_num == 0:
    print("TA sleeping, no students!")
    exit(-1)

# Create threads
students = []
for i in range(student_num):
    students.append(threading.Thread(target=stu_programming, args=(i + 1,)))

ta = threading.Thread(target=ta_teaching)

# Start threads
ta.start()
for student in students:
    student.start()

# Join threads
ta.join()
for student in students:
    student.join()
