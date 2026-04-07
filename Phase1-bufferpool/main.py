from bufferpool import BufferPool
from LRU import LRUPolicy
from LRUK import LRUKPolicy

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