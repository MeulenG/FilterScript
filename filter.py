import time
import sys

# Usage of this code could look like: python filter.py * * *
# That example would output the following into the terminal:
#2021-08-08T09:28:59+02:00 INFO Application starting



#2021-08-08T09:29:20+02:00 ERROR Unable to load configuration



#2021-08-08T09:29:21+02:00 INFO Shutdown started



#2021-08-08T09:29:24+02:00 INFO Shutdown complete

# python filter.py log.txt 9 29 * would output the following into the terminal:

#2021-08-08T09:29:20+02:00 ERROR Unable to load configuration 

#2021-08-08T09:29:21+02:00 INFO Shutdown started

#2021-08-08T09:29:24+02:00 INFO Shutdown complete


def timelogfilter():
    filepath = sys.argv[1] #Our log.txt as a system argument
    hour = sys.argv[2] # the hour as a system argument
    minute = sys.argv[3] # the minute as a system argument
    sec = sys.argv[4] # the seconds as a system argument
    with open(filepath,'r') as f: #opens the file
        for line in f: #reads through the lines
            #hour is located at [11], [12]
            # minute is located at [14], [15]
            # sec is located at [17], [18]
            #this method works with this specific type of log file since we know the position, and therefore can utilise the slicing technique
            #strip the leading 0 to account for every case
            # you could use regular expressions, but I'm not familliar enough with that and therefore i chose not to. 
            hour_string = line[11:13].lstrip("0") 
            minute_string = line[14:16].lstrip("0")
            sec_string = line[17:19].lstrip("0")
            # # this if statement first and foremost checks whether its a star and therefore a valid argument or if the hour and the hour_string is the same and if it is then it prints the line
            if hour == "*" or hour == hour_string: 
                if minute == "*" or minute == minute_string:
                    if sec == "*" or sec == sec_string:
                        print(line)


if __name__=="__main__": #main function
    timelogfilter() #calls our function