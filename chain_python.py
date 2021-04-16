"""
Append only data type called "chain".
Inspired by bitcoin protocol.
"""
# to get current time
from time import time
# to compute hash
from hashlib import sha256
# to feed sha256 string from json dictionary
import json

class Chain:
    chain = {}
    id = 0

    def add_to_chain(self, data):
        temp_chain = {}
        if self.id == 0:
            temp_chain["prev_hash"] = "shyngys" # You can put 0 or empty string. I put shyngys (my name) for fun. 
        else:
            temp_chain["prev_hash"] = list(self.chain.keys())[-1]
        temp_chain["id"] = self.id
        temp_chain["time"] = time()
        temp_chain["data"] = data
        string_from_dictionary = json.dumps(temp_chain)
        hash = self.compute_hash(string_from_dictionary)
        self.chain[hash] = {
            "id":   temp_chain["id"],
            "time": temp_chain["time"],
            "data": temp_chain["data"],
        }
        self.id = self.id + 1

    def values(self):
        return self.chain

    def compute_hash(self, string_from_dictionary):
        return sha256(string_from_dictionary.encode()).hexdigest()

# usage example
chain = Chain()
chain.add_to_chain({
    "sent_from": "Abhi",
    "sent_to":   "Shyngys"
})
chain.add_to_chain(1)
print(chain.values())
