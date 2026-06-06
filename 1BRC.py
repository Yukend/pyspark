import time

city_temp = {}

start = time.time()

count = 1
for i in open("temperatures.txt", "r").readlines():
    city, temp = i.replace("\n", "").split(";")
    temp = float(temp)
    if city in city_temp:
        city_temp[city] = {
            "average":  (city_temp[city]["average"] + temp)/2,
            "max": city_temp[city]["max"] if city_temp[city]["max"] > temp else temp,
            "min": city_temp[city]["min"] if city_temp[city]["min"] < temp else temp}
    else:
        city_temp[city] = {
            "average": temp,
            "max": temp,
            "min": temp}
    count += 1
    if count%1000000 == 0:
        print(count)
        print(time.time() - start)
print(city_temp)

# import time
# import random
# import threading
# import multiprocessing

# data = [
#     "Hamburg;12.0",
#     "Bulawayo;8.9",
#     "Palembang;38.8",
#     "St. John's;15.2",
#     "Cracow;12.6",
#     "Bridgetown;26.9",
#     "Istanbul;6.2",
#     "Roseau;34.4",
#     "Conakry;31.2",
#     "Istanbul;23.0",
#     "Hamburg;12.5",
#     "Bulawayo;8.5",
#     "Palembang;38.5",
#     "St. John's;15.5",
#     "Cracow;12.5",
#     "Bridgetown;26.5",
#     "Istanbul;6.5",
#     "Roseau;34.5",
#     "Conakry;31.5",
#     "Istanbul;23.5",
#     "Hamburg;12.5",
#     "Bulawayo;8.5",
#     "Palembang;38.5",
#     "St. John's;15.5",
#     "Cracow;12.5",
#     "Bridgetown;26.5",
#     "Istanbul;6.5",
#     "Roseau;34.5",
#     "Conakry;31.5",
#     "Istanbul;23.5"
# ]

# # Repeat the data to generate a billion rows
# total_rows = 1000000
# rows_per_thread = total_rows // multiprocessing.cpu_count()
# threads = []
# file_lock = threading.Lock()

# def generate_data(thread_id):
#     start_index = thread_id * rows_per_thread
#     end_index = (thread_id + 1) * rows_per_thread
#     thread_data = [random.choice(data) for _ in range(start_index, end_index)]

#     with file_lock:
#         with open("temperatures.txt", "a") as file:
#             for row in thread_data:
#                 file.write(row + "\n")

#     print(f"Thread {thread_id} completed.")

# start = time.time()
# # Create and start threads
# for i in range(multiprocessing.cpu_count()):
#     thread = threading.Thread(target=generate_data, args=(i,))
#     threads.append(thread)
#     thread.start()

# # Wait for all threads to finish
# for thread in threads:
#     thread.join()

# print(time.time() - start)
# print("Data generation complete.")

