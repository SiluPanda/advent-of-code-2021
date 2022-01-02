
        
class PacketDecoder:
    def __init__(self) -> None:
        self.version = 0
        self.pos = 0
        self.binary = self.hex_to_bin(input())



    def hex_to_bin(self, hex):
        mapping = {}
        for i in range(0, 10):
            b = bin(i).replace('0b', '')
            b = '0' * (4 - len(b)) + b
            mapping[str(i)] = b

        mapping['A'] = '1010'
        mapping['B'] = '1011'
        mapping['C'] = '1100'
        mapping['D'] = '1101'
        mapping['E'] = '1110'
        mapping['F'] = '1111'

        binary = ''
        for c in hex:
            binary += mapping[c]

        return binary

    
    def get_decimal(self, num_bits):
        binary = self.binary[self.pos:self.pos + num_bits]
        self.pos += num_bits
        print(binary)
        return int(binary, 2)


    def get_binary(self, num_bits):
        binary = self.binary[self.pos:self.pos + num_bits]
        self.pos += num_bits
        return binary

    def parse(self):
        version = self.get_decimal(3)
        print(version)
        type = self.get_decimal(3)

        self.version += version
        if type == 4:
            return self.parse_literal()
        else:
            return self.parse_operator(type)


    def parse_literal(self):
        binary = ''
        while True:
            buffer = self.get_binary(5)
            binary += buffer[1:]
            if buffer[0] == '0':
                break

        return int(binary, 2)


    def parse_operator(self, type):
        len_id = self.get_binary(1)
        values = []
        if len_id == '0':
            content_length = self.get_decimal(15)
            starting_bit = self.pos
            while self.pos - starting_bit < content_length:
                value = self.parse()
                values.append(value)

        else:
            num_packets = self.get_decimal(11)
            for _ in range(num_packets):
                value = self.parse()
                values.append(value)

        if type == 0:
            return sum(values)

        if type == 1:
            mul = 1
            for num in values:
                mul *= num
            return mul

        if type == 2:
            return min(values)

        if type == 3:
            return max(values)

        if type == 5:
            return 1 if values[0] > values[1] else 0

        if type == 6:
            return 1 if values[0] < values[1] else 0

        if type == 7:
            return 1 if values[0] == values[1] else 0

        







packet = PacketDecoder()
ans  = packet.parse()

print(ans)



    


            
            




