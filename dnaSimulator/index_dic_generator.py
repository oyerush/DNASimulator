



class generate_indx_dic:
    def numberToBase(self, n, b, size):
        if n == 0:
            return [0] * (size - 1) + [0]
        digits = []
        while n:
            digits.append(int(n % b))
            n //= b
        return [0] * (size - len(digits[::-1])) + digits[::-1]

    def toDNA(self, x):
        dna_str = ""
        for n in x:
            dna_str += self.DNA[n]
        return dna_str

    def create_ind(self, size):
        return [self.toDNA(self.numberToBase(x, 4, size)) for x in range(4 ** size)]

    def is_legal(self, x):
        last_char = 0
        for c in x:
            if c == last_char:
                return False
            last_char = c
        return True

    def create_ind_dic(self):
        d = {}
        i = 0
        for x in self.create_ind(self.q):
            if self.is_legal(x):
                d[x] = i
                i += 1
        return d

    def __init__(self, q):

        self.q = q
        self.DNA ={
            0: 'A',
            1: 'C',
            2: 'G',
            3: 'T'
        }
        self.ind_dic = self.create_ind_dic()

    def get_ind_dic(self):
        return self.ind_dic



