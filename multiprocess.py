
from joblib import Parallel, delayed
import multiprocessing

inputs = range(10) 
def processInput(i):
    return i * i,i*i*i

num_cores = multiprocessing.cpu_count()
print(num_cores)
results = Parallel(n_jobs=num_cores)(delayed(processInput)(i) for i in inputs)

print(results)