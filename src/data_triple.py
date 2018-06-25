class DataTriple:
    def __init__(self, count, address, data):
        assert 1 <= count <= 0xff
        assert 0 <= address < 8192

        self.count = count
        self.address = address
        self.data = data

    def __eq__(self, other):
        return tuple([self.count, self.address, self.data]) \
               == tuple([other.count, other.address, other.data])

    def __str__(self):
        return f"{self.count:01x}{self.address:04x}{self.data:02x}"
