class Node:
    def __init__(self, key, value):
        self.key   = key
        self.value = value
        self.prev  = None   # pointer to less-recently-used neighbor
        self.next  = None   # pointer to more-recently-used neighbor


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache    = {}   # key → Node (for O(1) lookup)

        # Two dummy boundary nodes — they never hold real data.
        # Everything between them is real cache, ordered LRU → MRU.
        self.lru_end = Node(0, 0)   # left  sentinel — LRU side
        self.mru_end = Node(0, 0)   # right sentinel — MRU side
        self.lru_end.next = self.mru_end
        self.mru_end.prev = self.lru_end

    # ── Private helpers ──────────────────────────────────────────

    def _remove_from_list(self, node):
        """Snip a node out of the doubly linked list."""
        node.prev.next = node.next
        node.next.prev = node.prev

    def _insert_at_mru(self, node):
        """Put a node just before the MRU sentinel (= most recently used)."""
        neighbor          = self.mru_end.prev
        neighbor.next     = node
        node.prev         = neighbor
        node.next         = self.mru_end
        self.mru_end.prev = node

    # ── Public API ───────────────────────────────────────────────

    def get(self, key):
        if key not in self.cache:
            return -1

        # Move to MRU position (it was just used)
        node = self.cache[key]
        self._remove_from_list(node)
        self._insert_at_mru(node)
        return node.value

    def put(self, key, value):
        # If key already exists, remove the old node first
        if key in self.cache:
            self._remove_from_list(self.cache[key])

        # Create and insert the new/updated node at MRU end
        new_node        = Node(key, value)
        self.cache[key] = new_node
        self._insert_at_mru(new_node)

        # Evict if over capacity
        if len(self.cache) > self.capacity:
            lru_node = self.lru_end.next   # oldest node is right after the LRU sentinel
            self._remove_from_list(lru_node)
            del self.cache[lru_node.key]   # ← this is why the Node stores its own key