import sys  
import re  # regular expression module


def log_parsing():
    """gets infomation from logs"""
    codes = [200, 301, 400, 401, 403, 404, 405, 500] # possible status codes to be present in logs
    
    # created a dictionary to count the noof occurrence of each status code
    status_count = {status: 0 for status in codes}
    
    # stores the file size of each log
    file_size = []
    
    # count will be used to count the no of lines
    count = 0
    status = None
    try:
        # loop through the standard input
        for line in sys.stdin:
            count += 1
            search = re.search('GET .* (.*) (.*)', line) # capture the status code and file size of a log with regex
            
            status = int(search.group(1))  # assign the status code
            
            if status in status_count.keys(): # check if the status code is in the allowed status codes
            
                status_count[status] += 1    # if yes, increase the count of the status code
                
                file_size.append(int(search.group(2)))   # append the file size of that log to file_size list
                
            if count == 10:   # check if the no lines == 10
                count = 0     # set count back to zero
                
                print("File size: {}".format(sum(file_size))) # if yes, print the file size and the no of occurrence of each \n
                for key, val in status_count.items():         # status code so far
                    if val != 0:
                        print("{}: {}".format(key, val))
        print("File size: {}".format(sum(file_size)))   # same as the print statement above but caters for when the loop and ended 
        for key, val in status_count.items():           # example: lets say the no of logs is 31, this would cater for the last log
            if val != 0:                                # since "if count == 10:" would have happend to be true 3 times
                print("{}: {}".format(key, val))
    except KeyboardInterrupt:
        print("File size: {}".format(sum(file_size)))  # same as above but for if KeyboardInterrupt is encountered
        for key, val in status_count.items():
            if val != 0:
                print("{}: {}".format(key, val))
        raise


if __name__ == "__main__":
    log_parsing()
