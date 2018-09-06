import csv
import datetime
now = datetime.datetime.now()

def PrintVertical(input_list):
    for counter in range(0,len(input_list)):
        print(input_list[counter])

calendar_text = open("Calendar.txt", "r")
read_file = calendar_text.readlines()

cleaned_up = []

month = []
day = []
start_time = []
start_ampm = []
end_time = []
end_ampm = []
room_num = []

for counter in range(0,len(read_file)):
    cleaned_up.append(read_file[counter].replace("\t", ""))
    cleaned_up[counter] = cleaned_up[counter].replace("\n", "")
    cleaned_up[counter] = cleaned_up[counter].replace("Curry Student Center", "")
    cleaned_up[counter] = cleaned_up[counter].replace("reserved", "")
    cleaned_up[counter] = cleaned_up[counter].replace("Mon", "")
    cleaned_up[counter] = cleaned_up[counter].replace("Tue", "")
    cleaned_up[counter] = cleaned_up[counter].replace("Wed", "")
    cleaned_up[counter] = cleaned_up[counter].replace("Thu", "")
    cleaned_up[counter] = cleaned_up[counter].replace("Fri", "")
    cleaned_up[counter] = cleaned_up[counter].replace("/2018", "")



for counter in range(0,len(cleaned_up)):
    current_line = cleaned_up[counter]
    month_end = current_line.find("/", 0)
    month.append(current_line[0:month_end])

    day_end = current_line.find(" ", month_end)
    day.append(current_line[month_end+1:day_end])

    time_start = day_end+1
    time_end = current_line.find(":",time_start)
    start_time.append(current_line[time_start:time_end])

    ampm_start = time_end+4
    ampm_end = ampm_start+2
    start_ampm.append(current_line[ampm_start:ampm_end])

    end_time_start = ampm_end
    end_time_end = current_line.find(":", end_time_start)
    end_time.append(current_line[end_time_start:end_time_end])

    ampm_start = current_line.find(" ", end_time_end) + 1
    ampm_end = ampm_start+2
    end_ampm.append(current_line[ampm_start:ampm_end])

    num_start = ampm_end+1
    num_end = num_start+3
    room_num.append(current_line[num_start:num_end])

last_month = month[0]
last_day = day[0]
last_start = str(start_time[0]) + str(start_ampm[0])
last_end = str(end_time[0]) + str(end_ampm[0])
print_month = True
print_day = True
for i in range(1,len(month)):
    last_month = month[i-1]
    last_day = day[i-1]

    last_start = str(start_time[i-1]) + str(start_ampm[i-1])
    last_end = str(end_time[i-1]) + str(end_ampm[i-1])

    cur_start = str(start_time[i]) + str(start_ampm[i])
    cur_end = str(end_time[i]) + str(end_ampm[i])

    if (last_day == day[i]):
        print_day = False
    else:
        print_day = True
    if(i == 1):
        print_day = True

    if(print_day):
        print(str(month[i]) + "/" + str(day[i]))

    print("Room #" + str(room_num[i]) + " - From: " + str(cur_start) + " To " + str(cur_end))

file_out = "/home/hirshjack/Calendar_Events.csv"

with open(file_out, 'w') as csv_file:
    fieldnames = ['Subject', 'Start Date', 'Start Time', 'End Time', 'Location']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    for i in range(0, len(month)):
        start_date = str(month[i]) + "/" + str(day[i]) + "/" + str(now.year)
        start = str(start_time[i]) + ":00 " + str(start_ampm[i])
        end = str(end_time[i]) + ":00 " + str(end_ampm[i])
        location = "Room #" + str(room_num[i]) + " Curry Student Center"
        writer.writerow({'Subject' : "Study Room", 'Start Date' : start_date, 'Start Time' : start, 'End Time' : end, 'Location' : location})


