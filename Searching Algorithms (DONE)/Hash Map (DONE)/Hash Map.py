'''
Hash Maps are similar to dictionaries...
Use Python's hashing function
'''

class HashTable():
    def __init__(self, size_of_buckets):
        self.size = size_of_buckets
        self.hash_table = self.create_buckets()

    def create_buckets(self):
        return [[] for _ in range(self.size)]

    def setvalue(self, key, value):
        hashed_key = abs(hash(key)) % self.size # Get Hash (Used for Indexing)
        bucket = self.hash_table[hashed_key]
        if bucket:
            for i in bucket:
                if i[0] == key and i[1] == value:
                    pass
                else:
                    bucket.append((key, value))

        else:
            bucket.append((key, value))

    def getvalue(self, key):
        hashed_key = abs(hash(key)) % self.size # Get Same Hash Key
        bucket = self.hash_table[hashed_key]
        if bucket:
            for i in bucket:
                if i[0] == key:
                    return i[1]
                else:
                    return "Record does not exist!"
        else:
            return "Bucket does not exist!"

    def deletevalue(self, key):
        hashed_key = abs(hash(key)) % self.size
        bucket = self.hash_table[hashed_key]
        if bucket:
            for i in bucket:
                if i[0] == key:
                    bucket.remove(i)
                else:
                    return "Record does not exist!"
        else:
            return "Bucket does not exist!"



    def __str__(self):
        return ''.join(str(item) for item in self.hash_table)


ha = HashTable(100)
ha.setvalue('Darryl', 'Data Scientist')
ha.setvalue('Jia Hui', 'D1octor')
ha.setvalue('Jia Hui', 'D1octor')
print(ha)

print(ha.getvalue('Jia Hui'))

ha.deletevalue('Jia Hui')
print(ha)





