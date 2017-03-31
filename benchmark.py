from time import process_time as pc

class Benchmark(object):
    def __init__(self, name:str = ''):
        self.start_time = None
        self.end_time = None
        self.name = name
    
    def __enter__(self):
        self.start_time = pc()

    def __exit__(self, *args):
        self.end_time = pc()
        print(f'Benchmark "{self.name}" took: {self.end_time - self.start_time} seconds')