# form hash_base to get the binary signature
DNA = {
    0: 'A',
    1: 'C',
    2: 'G',
    3: 'T'
}


def numberToBase(n, b, size):
    if n == 0:
        return [0]*(size - 1)+[0]
    digits = []
    while n:
        digits.append(int(n % b))
        n //= b
    return [0]*(size-len(digits[::-1])) + digits[::-1]


def toDNA(x):
    dna_str = ""
    for n in x:
        dna_str += DNA[n]
    return dna_str


def create_ind(m, size):
    for x in [toDNA(numberToBase(x, 4, size)) for x in range(4**size)]:
        m[x] = []
    return m


def ham_dis(x, y):
    # hamming distance between x, y
    dis = 0
    for i in range(0, len(x)):
        if x[i] != y[i]:
            dis += 1
    return dis


def ind_st(st):
    # convert form DNA-base to decimal-base
    # All 3-grams: AAA,AAG,AAC,AAT,AGA,AGC,...,TTA,TTG,TTC,TTT
    # A-0, G-1, C-2, T-3
    # index of CAT = Decimal representaion of (203)
    N_q = {"A": 0, "C": 1, "G": 2, "T": 3}
    dec = 0
    for i in range(0, len(st)):
        dec += N_q[st[i]] * (4 ** (len(st) - i - 1))
    return dec


def bin_sig(x, q):
    # x - st of DNA
    # q - size of DAN-chunk
    # return binary string
    #   i-th character is 1 if DNAbase(i) in x
    bs = [0] * (4 ** q)
    for i in range(0, len(x) - q + 1):
        st = x[i:i + q]
        bs[ind_st(st)] = 1
    bs_str = ''.join(str(e) for e in bs)
    return bs_str
