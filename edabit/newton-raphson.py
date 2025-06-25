def cubic_pol_value(coefs, x):

    '''returns value of a cubic polynomial given coefficients
    and input value'''

    return (coefs[0]* x ** 3 +
            coefs[1]* x ** 2 +
            coefs[2]* x +
            coefs[3])

def cubic_pol_deriv (coefs, x):

    '''returns value for derivative of cubic polynomial given coefficients
    and input value'''


    return (coefs[0]* 3 * x ** 2 +
            coefs[1]* 2 * x +
            coefs[2])
    
def newton_raphson(coefs, max_iter=20):

    '''given a set of coefficients for a cubic polynomial,
    applies the Newton-Raphson method for finding polynomial roots'''
    
    x = 0
    for _ in range(max_iter):
        fx = cubic_pol_value(coefs, x)
        f_dash_x = cubic_pol_deriv (coefs, x)
        x = x - fx / f_dash_x
        
    return round(x, 3)
