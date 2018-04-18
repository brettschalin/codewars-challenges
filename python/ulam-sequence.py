def ulam_sequence(u0, u1, n):
    '''
https://www.codewars.com/kata/5995ff073acba5fa3a00011d
The Ulam sequence is defined as follows:
u(0) and u(1) are given. u(2) and later are the smallest integers
which can be expressed as the unique sum of two previous terms.

input args: u0, u1 are the first two terms, n is the number of terms to evaluate.
    '''
    seq = [u0,u1,u0+u1]
    while len(seq) < n:
        seq.append(find_next(seq))
    return seq

def find_next(seq):
    seen = []
    candidates = set()
    for i,x in enumerate(seq):
        for y in seq[i+1:]:
            c = x+y
            if c <= seq[-1]: continue
            if c in seen:
                candidates.discard(c)
                continue
            seen.append(c)
            candidates.add(c)
    return min(candidates)