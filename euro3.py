from __future__ import print_function


import thinkbayes

class Euro(thinkbayes.Suite):
    def Likelihood(self, data, hypo):
        """The likelihood of the data under the hypothesis.

        hypo: integer value of x, the probability of heads (0-100)
        data: tuple of (number of heads, number of fails)
        """
        x = hypo / 100.0
        heads, tails = data
        like = x**heads * (1-x)**tails
        return like
    
def TrianglePrior():
    suite = Euro()
    for x in range(0, 51):
        suite.Set(x,x)
    for x in range(51,101):
        suite.Set(x, 100-x)
    suite.Normalize()
    return suite

def SuiteLikelihood(suite, data):
    total = 0
    for hypo, prob in suite.Items():
        like = suite.Likelihood(data, hypo)
        total += like * prob
    return total

def main():
    data = (140, 110)
    data = 8,12

    suite = Euro()
    like_f = suite.Likelihood(data,50)
    print('p(D|F) =', like_f)

    actual_percent = 100*140/250
    likelihood = suite.Likelihood(data, actual_percent)
    print('p(D|B_cheat)', likelihood)
    print('p(D|B_cheat) p(D|F)', likelihood/like_f)

    like40 = suite.Likelihood(data, 40)
    like60 = suite.Likelihood(data, 60)
    likelihood = 0.5*like40 + 0.5*like60
    print('p(D|B_two)', likelihood)
    print('p(D|B_two) / p(D|F)', likelihood/like_f)

    b_uniform = Euro(range(0,101))
    b_uniform.Remove(50)
    b_uniform.Normalize()
    likelihood = SuiteLikelihood(b_uniform, data)
    print('p(D|B_uniform)', likelihood)
    print('p(D|B_uniform) / p(D|F)', likelihood/like_f)

    b_tri = TrianglePrior()
    b_tri.Remove(50)
    b_tri.Normalize()
    likelihood = b_tri.Update(data)
    print('p(D|B_tri)',likelihood)
    print('p(D|B_tri) / p(D|F)', likelihood/like_f)

if __name__ == '__main__':
    main()