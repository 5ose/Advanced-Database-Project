from collections import defaultdict

class LRUKPolicy:
    def __init__(self, k=2):
        self.k = k
        self.time = 0
        self.history = defaultdict(list)

    def record_access(self, page_id):
        self.time += 1
        self.history[page_id].append(self.time)

    def record_insert(self, page_id):
        self.time += 1
        self.history[page_id].append(self.time)

    def choose_victim(self, current_frames):
        victim = None
        best_score = None

        for page in current_frames:
            accesses = self.history[page]

            if len(accesses) < self.k:
                kth_recent = float("-inf")
            else:
                kth_recent = accesses[-self.k]

            if best_score is None or kth_recent < best_score:
                best_score = kth_recent
                victim = page

        return victim

    def record_removal(self, page_id):
        # optional:
        # del self.history[page_id]
        pass