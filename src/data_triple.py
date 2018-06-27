class DataTriple:
    def __init__(self, count, address, data):
        assert 1 <= count <= 0xff
        assert 0 <= address < 8192
        assert count == len(data)

        self.count = count
        self.address = address
        self.data = data

    def __eq__(self, other):
        return tuple([self.count, self.address, self.data]) \
               == tuple([other.count, other.address, other.data])

    def __str__(self):
        data_str = ''.join(f"{a:02x}" for a in self.data)
        return f"{self.count:01x}{self.address:04x}{data_str}"
