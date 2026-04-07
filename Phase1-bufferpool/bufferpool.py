class BufferPool:
    def __init__(self, size, policy):
        self.size = size
        self.frames = []
        self.page_table = {}
        self.policy = policy

    def fetch_page(self, page_id):
        if page_id in self.page_table:
            print(f"HIT: {page_id}")
            self.policy.record_access(page_id)
        else:
            print(f"MISS: {page_id}")

            if len(self.frames) == self.size:
                print("Buffer is Full. Evicting a page...")
                victim = self.policy.choose_victim(self.frames)
                self.remove_page(victim)

            self.frames.append(page_id)
            self.page_table[page_id] = True
            self.policy.record_insert(page_id)

    def remove_page(self, page_id):
        self.frames.remove(page_id)
        del self.page_table[page_id]
        self.policy.record_removal(page_id)

    def display(self):
        print("Frames:", self.frames)