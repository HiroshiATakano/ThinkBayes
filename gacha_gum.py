from thinkbayes import Suite

class Gacha_Gum(Suite):

    bag_2019 = {
        "red": 0.40,
        "blue": 0.30,
        "yellow": 0.20,
        "green": 0.10
    }

    bag_2021 = {
        "red": 0.20,
        "blue": 0.40,
        "yellow": 0.10,
        "green": 0.30
    }

    hypoA = dict(bag1=bag_2019, bag2=bag_2021)
    hypoB = dict(bag1=bag_2021, bag2=bag_2019)

    hypotheses = dict(A=hypoA, B=hypoB)

    def Likelihood(self, data, hypo):
        bag, color = data
        mix = self.hypotheses[hypo][bag]
        like = mix[color]
        return like
    

def main():
    suite = Gacha_Gum('AB')

    suite.Update(('bag1','red'))
    suite.Update(('bag2', 'green'))

    suite.Print()

if __name__ == '__main__':
    main()
