from fractions import Fraction

def solution(pegs):

    # radius of [0] must be double of radius[max]
    # radius of [0] and [1] ... must add to [1]-[0]

    """
    P0 = pegs[0]
    P1 = pegs[1]
    ...

    r0 * w0 = rn * wn
    where 'w' denotes angular velocity

    therefore

    r0 = (wn/w0) * rn = 2 * rn (wn/w0 must = 2/1 -> radius of [0] must be double of radius[max])
    """

    # building the equation:

    """
    Case when n = 3:
    r0 + r1 = P1 - P0
    r1 + r2 = P2 - P1
    """

    # early return for if the pegs list is not eligible (failstate)
    max_len = len(pegs)
    if not pegs or max_len == 1:
        return [-1,-1]

    # determine if the number of pegs is odd or even
    odd = False if (max_len % 2 == 0) else True
    sum = ( -pegs[0] - pegs[ max_len-1 ] ) if odd else ( -pegs[0] + pegs[ max_len-1 ] )

    if (max_len > 2):
        pos_neg = 1
        for peg in pegs[1:max_len-1]:
            sum += 2 * peg * pos_neg
            pos_neg *= -1
 
    gear1_radius = Fraction(2 * (sum if odd else float(sum)/3)).limit_denominator()

    # early return for efficiency if gear1 radius < 1 (failstate)
    if gear1_radius < 1:
        return [-1, -1]

    curr_radius = gear1_radius
    for curr_peg, next_peg in zip(pegs[0:max_len-2], pegs[1:max_len-1]):

        # next_peg - curr_peg = total distance between pegs, removing the curr_radius from this gives us the next_radius
        next_rad = next_peg - curr_peg - curr_radius

        # return for if the next radius < 1 (failstate)
        if (next_rad < 1):
            return [-1,-1]

        curr_radius = next_rad

    # if we never run into a failstate in the code, we can safely return the gear1 radius
    return [gear1_radius.numerator, gear1_radius.denominator]