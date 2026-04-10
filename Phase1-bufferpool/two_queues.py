from collections import deque

class TwoQueuesPolicy:
    def __init__(self, size):
        self.size = size

        # Queues
        self.A1 = deque()      # FIFO (recent pages)
        self.Am = deque()      # LRU (frequent pages)
        self.A1out = deque()   # Ghost queue

        # Sizes (tunable)
        self.k_in = max(1, size // 4)   # avoid 0
        self.k_out = max(1, size // 2)

    def record_access(self, page_id):
        # If page is in Am → move to MRU
        if page_id in self.Am:
            self.Am.remove(page_id)
            self.Am.append(page_id)

        # If page is in A1 → promote to Am
        elif page_id in self.A1:
            self.A1.remove(page_id)
            self.Am.append(page_id)

        # If page was in A1out → bring to Am
        elif page_id in self.A1out:
            self.A1out.remove(page_id)
            self.Am.append(page_id)

    def record_insert(self, page_id):
        # Insert into A1
        self.A1.append(page_id)

        # Maintain A1 size
        if len(self.A1) > self.k_in:
            old = self.A1.popleft()
            self.A1out.append(old)

            # Maintain ghost size
            if len(self.A1out) > self.k_out:
                self.A1out.popleft()

    def record_removal(self, page_id):
        if page_id in self.A1:
            self.A1.remove(page_id)
        elif page_id in self.Am:
            self.Am.remove(page_id)

        # Add to ghost queue
        self.A1out.append(page_id)

        if len(self.A1out) > self.k_out:
            self.A1out.popleft()

    def choose_victim(self, frames):
        # Try A1 first (FIFO behavior)
        for page in self.A1:
            if page in frames:
                return page

        # Then try Am (LRU behavior)
        for page in self.Am:
            if page in frames:
                return page

        # Fallback (safety)
        return frames[0]