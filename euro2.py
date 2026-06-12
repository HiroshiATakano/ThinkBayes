from __future__ import print_function
import thinkbayes
import thinkplot

class Euro(thinkbayes.Suite):
    """Represents hypotheses about the probability of heads."""

    def Likelihood(self, data, hypo):
        x = hypo/100.0
        if data == 'H':
            return x
        else:
            return 1-x
class Euro2(thinkbayes.Suite):

    def Likelihood(self, data, hypo):
        x = hypo/100.0
        heads, tails = data
        like = x**heads * (1-x)**tails
        return like
    
def Version1():
    suite = Euro(range(0,101))
    heads, tails = 140, 110
    dataset = 'H'*heads + 'T'*tails

    for data in dataset:
        suite.Update(data)

    return suite

def Version2():
    suite = Euro(range(0,101))
    heads, tails = 140, 110
    dataset = 'H'*heads + 'T'*tails

    suite.UpdateSet(dataset)
    return suite

def Version3():
    suite = Euro2(range(0,101))
    heads, tails = 140, 110

    suite.Update((heads, tails))
    return suite

def main():
    suite = Version1()
    print(suite.Mean())

    thinkplot.Pmf(suite)
    thinkplot.Show()


if __name__ == '__main__':
    main()
