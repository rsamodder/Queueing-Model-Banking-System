from math import factorial

EPS = 1e-7


class MM1:

    def __init__(s, lamda, miu):
        
        s._lamda = eval(lamda)

        s.__miu = eval(miu)

        s.__rho = s._lamda / s.__miu

    @property
    def proP0(s):

        return 1 - s.__rho
        # else TODO: throw an exception

    def proP(s, n):
        return s.__rho ** n * s.proP0

    def customerl(s):
        return s._lamda * s.timeW()

    def customerlq(s):
        return s._lamda * s.timeWq()

    def timeW(s):
        return 1 / (s.__miu - s._lamda + EPS)

    def timeWq(s):
        return s.__rho * s.timeW()

    def setlamda(s, lamda):
        s._lamda = eval(lamda)
        s.__rho = s._lamda / s.__miu

    def set_miu(s, miu):
        s.__miu = eval(miu)
        s.__rho = s._lamda / s.__miu

    def getlamda(s):
        return s._lamda

    def get_miu(s):
        return s.__miu

    def get_rho(s):
        return s.__rho

class MM1N:

    def __init__(s, lamda, miu, k):
        s._lamda = eval(lamda)
        s.__miu = eval(miu)
        s.__k = eval(k)
        s.__rho = s._lamda / s.__miu

    def proP(s, n):
        if s.__rho == 1:
            return 1 / (s.__k + 1)
        else:
            return round(s.__rho ** n * ((1 - s.__rho + EPS) / (1 - s.__rho ** (s.__k + 1) + EPS)), 2)

    def customerl(s):
        if s.__rho == 1:
            return s.__k / 2
        else:
            num = 1 - (s.__k + 1) * s.__rho ** s.__k + s.__k * s.__rho ** (s.__k + 1) + EPS
            den = (1 - s.__rho + EPS) * (1 - s.__rho ** (s.__k + 1) + EPS)
        return round(s.__rho * num / den, 2)

    def customerlq(s):
        return round(s.timeWq() * s._lamda * (1 - s.proP(s.__k) + EPS), 2)

    def timeW(s):
        return round(s.customerl() / (s._lamda * (1 - s.proP(s.__k) + EPS)), 2)

    def timeWq(s):
        return round(s.timeW() - (1 / s.__miu) + EPS, 2)

    def setlamda(s, lamda):
        s._lamda = eval(lamda)
        s.__rho = s._lamda / s.__miu

    def set_miu(s, miu):
        s.__miu = eval(miu)
        s.__rho = s._lamda / s.__miu

    def set_k(s, k):
        s.__k = int(k)

    def getlamda(s):
        return s._lamda

    def get_miu(s):
        return s.__miu

    def get_rho(s):
        return s.__rho

    def get_k(s):
        return s.__k


class MMS:

    def __init__(s, lamda, miu, c):
        s._lamda = eval(lamda)
        s.__miu = eval(miu)
        s.__c = eval(c)
        s.__r = s._lamda / s.__miu
        s.__rho = s.__r / s.__c

    def proP0(s):
        acc = 0
        if s.__c > s.__r:
            for i in range(s.__c):
                acc += s.__r ** i / factorial(i)
            acc += s.__c * s.__r ** s.__c / (factorial(s.__c) * (s.__c - s.__r + EPS))
        else:
            for i in range(s.__c):
                acc += (1 // factorial(i)) * s.__r ** i
            acc += (1 // factorial(s.__c)) * s.__r ** s.__c * (
                        (s.__c * s.__miu) / (s.__c * s.__miu - s._lamda + EPS))
        return round(1 / acc, 6)

    def proP(s, n):
        num = s._lamda ** n
        if 0 <= n < s.__c:
            den = factorial(n) * s.__miu ** n
        else:
            den = s.__c ** (n - s.__c) * factorial(s.__c) * s.__miu ** n
        return (num / den) * s.proP0()

    def customerl(s):
        return round(s.customerlq() + s.__r, 3)

    def customerlq(s):
        num = s.__r ** (s.__c + 1) / s.__c
        den = factorial(s.__c) * (1 - s.__r / s.__c + EPS) ** 2
        return round(num * s.proP0() / den, 3)

    def timeW(s):
        return round(s.timeWq() + 1 / s.__miu, 3)

    def timeWq(s):
        return round(s.customerlq() / s._lamda, 3)

    def setlamda(s, lamda):
        s._lamda = eval(lamda)
        s.__r = s._lamda / s.__miu
        s.__rho = s.__r / s.__c

    def set_miu(s, miu):
        s.__miu = eval(miu)
        s.__r = s._lamda / s.__miu
        s.__rho = s.__r / s.__c

    def set_c(s, c):
        s.__c = int(c)
        s.__rho = s.__r / s.__c

    def get_miu(s):
        return s.__miu

    def getlamda(s):
        return s._lamda

    def get_c(s):
        return s.__c

    def get_rho(s):
        return s.__rho

    def get_r(s):
        return s.__r


class MMSN:

    def __init__(s, lamda, miu, c, k):
        s._lamda = eval(lamda)
        s.__miu = eval(miu)
        s.__c = eval(c)
        s.__k = eval(k)

        s.__r = s._lamda / s.__miu
        s.__rho = s.__r / s.__c

    def proP0(s):
        if s.__c != s.__r:
            acc = (1 - s.__rho ** (s.__k + 1 - s.__c)) * s.__r ** s.__c / (
                        factorial(s.__c) * (1 - s.__rho))
        else:
            acc = (s.__k + 1 - s.__c) * s.__r ** s.__c / factorial(s.__c)

        for i in range(s.__c):
            acc += (s.__r ** i / factorial(i))

        return round(1 / acc, 9)

    def proP(s, n):
        num = s._lamda ** n
        if n < s.__c:
            den = factorial(n) * s.__miu ** n
        else:
            den = s.__c ** (n - s.__c) * factorial(s.__c) * s.__miu ** n
        return round(num / den * s.proP0(), 9)

    def customerl(s):
        acc = 0.0
        for i in range(s.__c):
            acc += (s.__c - i) * s.__r ** i / factorial(i)
        return round(s.customerlq() + s.__c - s.proP0() * acc, 9)

    def customerlq(s):
        acc = 1 - (s.__rho ** (s.__k - s.__c) * (s.__k - s.__c + 1) * (
                    1.0 - s.__rho + EPS) + s.__rho ** (s.__k + 1 - s.__c))
        num = s.__rho * s.__r ** s.__c * s.proP0()
        den = factorial(s.__c) * (1.0 - s.__rho + EPS) ** 2
        return round(num / den * acc, 9)

    def timeW(s):
        return round(s.customerl() / (s._lamda * (1 - s.proP(s.__k))), 9)

    def timeWq(s):
        return round(s.customerlq() / (s._lamda * (1 - s.proP(s.__k))), 9)

    def setlamda(s, lamda):
        s._lamda = eval(lamda)
        s.__r = s._lamda / s.__miu
        s.__rho = s.__r / s.__c

    def set_miu(s, miu):
        s.__miu = eval(miu)
        s.__r = s._lamda / s.__miu
        s.__rho = s.__r / s.__c

    def set_k(s, k):
        s.__k = int(k)

    def set_c(s, c):
        s.__c = int(c)
        s.__rho = s.__r / s.__c

    def get_miu(s):
        return s.__miu

    def getlamda(s):
        return s._lamda

    def get_k(s):
        return s.__k

    def get_c(s):
        return s.__c

    def get_rho(s):
        return s.__rho

    def get_r(s):
        return s.__r
