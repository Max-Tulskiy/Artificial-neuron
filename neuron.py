import math


class Neuron:
    def __init__(self, w1, w2, coefficient, theta, typeActivation):
        self.w1 = float(w1)
        self.w2 = float(w2)
        self.theta = float(theta)
        self.typeActivation = typeActivation

        if typeActivation == 'Биполярная пороговая':
            self.k = None
        elif not coefficient:
            return 1 
        else:    
            self.k = float(coefficient)

        self.epochs = []

    def learn_neuron(self, coordinates):
        for p in (coordinates):
            x1 = p[0]
            x2 = p[1]
            d = p[2]

            result = self.find_output_signal(x1, x2)
            self.functional_value(result, d, x1, x2)

        return self.epochs

    # поиск ответа Y по активационной функции
    def functional_value(self, result, d, x1, x2):
        Y = 0
        if self.typeActivation == 'Линейная':
            
            Y = self.k * result
            if Y != d:
                self.find_delta_w(d, x1, x2)

        elif self.typeActivation == 'Биполярная пороговая':

            if result > 0:
                Y = 1
            else:
                Y = -1

            if Y != d:
                self.find_delta_w(d, x1, x2)

        else:
            Y = 1 / (1 + math.pow(math.e, self.k * result))       
            if Y != d:
                self.find_delta_w(d, x1, x2)


    def find_output_signal(self, x1, x2):
        x = self.w1 * x1 + self.w2 * x2 + self.theta
        return self.sign(x)


    def find_delta_w(self, d, x1, x2):
        self.w1 += d * x1
        self.w2 += d * x2
        self.theta += d 

        self.epochs.append([self.w1, self.w2, self.theta])


    def sign(self, x):
        if x > 0:
            return 1
        elif x < 0:
            return -1
        else:
            return 0