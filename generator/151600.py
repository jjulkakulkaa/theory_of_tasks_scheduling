import random
tasks = {}



for n in range(50, 501, 50):
    
    tasks = {}
    
    for j in range(n):
        p = random.randint(1, 1000)
        d = 0
        while d < p:
            d = random.randint(1, 1000)
                            # czas przezbrojenia z j do każdego taska 1 ... n
        tasks[j] = [p, d, [random.randint(1, 1000) for _ in range (n)]]
        
    with open(f'151600_{n}.in', 'w') as file:
            file.write(f"{n}\n")
            for j in range(n):
                file.write(f"{tasks[j][0]} {tasks[j][1]}\n")  #  p  d
                
            # czasy przezbrojen
            for j in range(n):
                file.write(" ".join(map(str, tasks[j][2])) + "\n")
            
            
            