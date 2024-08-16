import threading
import time

N = 5  # Número de filósofos

# Semáforo para limitar o número de filósofos tentando pegar hashis
mutex = threading.Semaphore(N - 1)
# Semáforos para os hashis
hashis = [threading.Semaphore(1) for _ in range(N)]

def filosofo(i):
    while True:
        print(f"Filósofo {i + 1} está pensando.")
        time.sleep(5)

        # Tenta pegar os hashis
        mutex.acquire()
        hashis[i].acquire()
        hashis[(i + 1) % N].acquire()

        # Come
        print(f"Filósofo {i + 1} pegou os hashis {i + 1} e {(i + 1) % N + 1}. Comendo...")
        time.sleep(5)

        # Devolve os hashis
        hashis[i].release()
        hashis[(i + 1) % N].release()
        mutex.release()

        print(f"Filósofo {i + 1} devolveu os hashis {i + 1} e {(i + 1) % N + 1}. Voltando a pensar.")
        time.sleep(1)

threads = []

    # Cria as threads para os filósofos
for i in range(N):
   t = threading.Thread(target=filosofo, args=(i,))
   threads.append(t)
   t.start()
