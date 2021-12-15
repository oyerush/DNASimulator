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


def bin_sig(x, q, ind_dic):
    # x - st of DNA
    # q - size of DAN-chunk
    # return binary string
    #   i-th character is 1 if DNAbase(i) in x
    bs = [0] * len(ind_dic)
    for i in range(0, len(x) - q + 1):
        st = x[i:i + q]
        bs[ind_dic[st]] = 1
    bs_str = ''.join(str(e) for e in bs)
    return bs_str

def edit_dis(s1, s2):
    # edit distance between s1, s2
    m = len(s1) + 1
    n = len(s2) + 1

    tbl = {}
    for i in range(m):
        tbl[i, 0] = i
    for j in range(n):
        tbl[0, j] = j
    for i in range(1, m):
        for j in range(1, n):
            #cost = 0 if s1[i - 1] == s2[j - 1] else 1
            if s1[i - 1] == s2[j - 1]:
                tbl[i, j] = min(tbl[i, j - 1] + 1, tbl[i - 1,
                            j] + 1, tbl[i - 1, j - 1])
            else:
                tbl[i, j] = min(tbl[i, j - 1] + 1, tbl[i - 1,j] + 1)

    return tbl[i, j]
