from multiprocessing import Process, Array

'''
Main process : define a list of some numbers
               Forking the user defined process
               Will wait for user defined process to finish the work
               Print the list of numbers
User defined process : squaring up all the numbers in that list
'''

numbers = Array('i', [3, 4, 2, 1, 6, 7]) # shared data in the memory
# can be shared by multiple processes

class SquarerProcess(Process):
    def run(self):
        global numbers
        i = 0
        for n in numbers:
            numbers[i] = n ** 2 # modifies the data in the common memory space
            i += 1
        print('Numbers as seen by squarer process')
        for n in numbers:
            print(n, end=',')

udp = SquarerProcess()
udp.start()

# wait for the sqaurer process to get over
udp.join()

print('Numbers as seen by main process')
for n in numbers:
    print(n, end=',') # accesses the data from the common memory space


