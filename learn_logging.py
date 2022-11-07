import logging
logging.basicConfig(filename='firstlogfile.log',level= logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')
# logging level allow us to specify exactly what we want to log by seperating them into categories

# 1) DEBUG:-> detail info, typicaly of interest only when diagnosing problem

# 2) INFO:-> Confirmation that things are working as expected

# 3) WARNING:-> An Indication something unexpected happend or indicative of some problem in the near future (e.g 'disk space low'). The software is still working as expected

# 4) CRITICAL:-> A serious error, indication that the program itself may be unable to continue running

# 5) ERROR:-> Due to more serious problem, the software has not been able to perform some function  


def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    if y == 0:
        raise ZeroDivisionError("Sorry can't divide by zero")
    else:
        return x / y

num_1 = 10
num_2 = 5



add_result = add(num_1, num_2)
logging.info('Add: {} + {} = {}'.format(num_1, num_2, add_result))
# =======================================
sub_result = sub(num_1, num_2)
logging.info('Sub: {} - {} = {}'.format(num_1, num_2, sub_result))
# =======================================
mul_result = mul(num_1, num_2)
logging.info('Mul: {} * {} = {}'.format(num_1, num_2, mul_result))
# =======================================
div_result = div(num_1, num_2)
logging.info('Div: {} / {} = {}'.format(num_1, num_2, div_result))






# add_result = add(num_1, num_2)
# print('Add: {} + {} = {}'.format(num_1, num_2, add_result))
# # =======================================
# sub_result = sub(num_1, num_2)
# print('Sub: {} - {} = {}'.format(num_1, num_2, sub_result))
# # =======================================
# mul_result = mul(num_1, num_2)
# print('Mul: {} * {} = {}'.format(num_1, num_2, mul_result))
# # =======================================
# div_result = div(num_1, num_2)
# print('Div: {} / {} = {}'.format(num_1, num_2, div_result))