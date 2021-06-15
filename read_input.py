# this simply gets the input from the file
def read_input():
    with open('mempool.csv') as f:
        return process_input([line.strip().split(',') for line in f.readlines()])

# this takes the input recieved from the file and puts it in a format that we can use
def process_input(input_array):
    processed_array = []
    for inp in input_array:
        new_arr = []
        new_arr.append(inp[0])
        new_arr.append(inp[1])
        new_arr.append(inp[2])
        new_arr.append(inp[3].strip().split(';'))
        if('' in new_arr[3]):
            new_arr[3].remove('')
        processed_array.append(new_arr)
    return processed_array


