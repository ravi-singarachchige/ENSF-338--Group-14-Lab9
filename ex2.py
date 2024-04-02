import random
import string
import hashlib
import matplotlib.pyplot as plt

# Step 1: Generate 1,000,000 random strings
random_strings = [''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(1, 10))) for _ in range(1_000_000)]

class DLeftHashTable:
    def __init__(self, buckets):
        self.buckets = buckets

    def hash_functions(self, key):
        hash1 = int(hashlib.sha256(key.encode('utf-8')).hexdigest(), 16) % self.buckets
        hash2 = int(hashlib.md5(key.encode('utf-8')).hexdigest(), 16) % self.buckets
        return hash1, hash2

# Step 2: Initialize hash table and distributions
hash_table = DLeftHashTable(1000)
hash1_distribution = [0] * 1000
hash2_distribution = [0] * 1000

for string in random_strings:
    hash1, hash2 = hash_table.hash_functions(string)
    hash1_distribution[hash1] += 1
    hash2_distribution[hash2] += 1

# Step 3: Plot the distributions
plt.figure(figsize=(20, 8))

plt.subplot(1, 2, 1)
plt.bar(range(1000), hash1_distribution, color='blue')
plt.title('SHA256 Hash Function Distribution')
plt.xlabel('Index Value')
plt.ylabel('#Collisions')

plt.subplot(1, 2, 2)
plt.bar(range(1000), hash2_distribution, color='green')
plt.title('MD5 Hash Function Distribution')
plt.xlabel('Index Value')

plt.tight_layout()
plt.show()

#The plots do not show significant "hot spots," indicating both hash functions 
# distribute the hash values quite evenly across all buckets. There are no
# obvious peaks or valleys that would suggest a concentration of hash values 
# (collisions) in specific buckets, which is desirable for achieving a uniform distribution in a hash table.