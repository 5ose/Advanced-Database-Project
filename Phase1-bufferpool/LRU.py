from collections import OrderedDict

class LRUPolicy:
    def __init__(self):
        self.order = OrderedDict()

    def record_access(self, page_id):
        if page_id in self.order:
            self.order.move_to_end(page_id)
        else:
            self.order[page_id] = True

    def record_insert(self, page_id):
        self.order[page_id] = True
        self.order.move_to_end(page_id)

    def choose_victim(self, current_frames):
        # first key = least recently used
        return next(iter(self.order))

    def record_removal(self, page_id):
        if page_id in self.order:
            del self.order[page_id]