import hashlib

class DLeftHashTable:
    def __init__(self, entries, buckets):
        self.entries = entries
        self.buckets = buckets
        self.left_table = {i: [] for i in range(buckets)}
        self.right_table = {i: [] for i in range(buckets)}

    def hash_functions(self, key):
        # Generate two different hash values
        hash1 = int(hashlib.sha256(key.encode('utf-8')).hexdigest(), 16) % self.buckets
        hash2 = int(hashlib.md5(key.encode('utf-8')).hexdigest(), 16) % self.buckets
        return hash1, hash2

    def insert(self, key, value):
        hash1, hash2 = self.hash_functions(key)
        # Choose the table with the lowest occupancy
        if len(self.left_table[hash1]) <= len(self.right_table[hash2]):
            self.left_table[hash1].append((key, value))
        else:
            self.right_table[hash2].append((key, value))

    def lookup(self, key):
        hash1, hash2 = self.hash_functions(key)
        # Search in both tables
        for k, v in self.left_table[hash1]:
            if k == key:
                return v
        for k, v in self.right_table[hash2]:
            if k == key:
                return v
        return None