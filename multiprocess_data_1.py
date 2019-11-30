from multiprocessing import Process

'''
Main process : define a list of some numbers
               Forking the user defined process
               Will wait for user defined process to finish the work
               Print the list of numbers
User defined process : squaring up all the numbers in that list
'''

numbers = [3, 4, 2, 1, 6, 7] # common data

class SquarerProcess(Process):
    def run(self):
        global numbers
        numbers = [n ** 2 for n in numbers]
        print('Numbers as seen by squarer process : {0}'.format(numbers)) # memory space of squarer process

udp = SquarerProcess()
udp.start()

# wait for the sqaurer process to get over
udp.join()

print('Numbers as seen by main process : {0}'.format(numbers)) # memory space of main process, which is not shared with
# squarer process

