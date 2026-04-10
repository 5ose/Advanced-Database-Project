class ClockPolicy:
    def __init__(self, size):
        self.size = size
        self.clock = []          # circular list of pages
        self.ref_bits = {}       # page_id -> reference bit
        self.hand = 0            # pointer

    def record_access(self, page_id):
        # Set reference bit to 1 on access
        self.ref_bits[page_id] = 1

    def record_insert(self, page_id):
        # Insert page into clock
        if len(self.clock) < self.size:
            self.clock.append(page_id)
        else:
            # This case normally won't happen because eviction happens first
            pass

        self.ref_bits[page_id] = 1

    def record_removal(self, page_id):
        # Remove page from structures
        if page_id in self.clock:
            idx = self.clock.index(page_id)
            self.clock.remove(page_id)

            # Fix hand if needed
            if idx < self.hand:
                self.hand -= 1
            elif self.hand >= len(self.clock):
                self.hand = 0

        if page_id in self.ref_bits:
            del self.ref_bits[page_id]

    def choose_victim(self, frames):
        while True:
            if not self.clock:
                return None

            page_id = self.clock[self.hand]

            if self.ref_bits.get(page_id, 0) == 0:
                # Evict this page
                victim = page_id
                self.hand = (self.hand + 1) % len(self.clock)
                return victim
            else:
                # Give second chance
                self.ref_bits[page_id] = 0
                self.hand = (self.hand + 1) % len(self.clock)