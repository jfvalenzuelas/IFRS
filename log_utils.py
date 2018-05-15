import time

LOG_FILE_PATH = 'log.txt'

def write(text):
    with open(LOG_FILE_PATH, 'w') as log_file:
        log_file.write('-----------------------------------------\n')
        log_file.write(time.strftime("%c"))
        log_file.write('\n')
        log_file.write(text)
        log_file.write('\n')

    log_file.close()