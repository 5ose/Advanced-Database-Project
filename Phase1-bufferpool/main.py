from bufferpool import BufferPool
from LRU import LRUPolicy
from LRUK import LRUKPolicy
from two_queues import TwoQueuesPolicy   
from clock_policy import ClockPolicy


if __name__ == "__main__":
    print("=== Design 4: LRU ===")
    pool3 = BufferPool(3, LRUPolicy())
    for p in [1, 2, 3, 1, 4, 2]:
        pool3.fetch_page(p)
        pool3.display()

    print("\n=== Design 4: LRU-K (K=2) ===")
    pool4 = BufferPool(3, LRUKPolicy(k=2))
    for p in [1, 2, 3, 1, 2, 4, 5]:
        pool4.fetch_page(p)
        pool4.display()

    print("\n=== Design 4: 2Q ===")   
    pool5 = BufferPool(3, TwoQueuesPolicy(size=3))
    for p in [1, 2, 3, 1, 4, 5, 1]:
        pool5.fetch_page(p)
        pool5.display()
    print("\n=== Design 4: Clock ===")
    pool6 = BufferPool(3, ClockPolicy(size=3))
    for p in [1, 2, 3, 1, 4, 2, 5]:
        pool6.fetch_page(p)
        pool6.display()    