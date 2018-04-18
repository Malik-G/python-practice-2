from timeit import timeit

def test_modulo():
    'Don\'t %s, I\'m the %s.' % ('worry', 'Doctor')

def test_format():
    'Don\'t {0}, I\'m the {1}.'.format('worry', 'Doctor')

bam = timeit(stmt=test_modulo, number=1000000)
print(bam)
# 0.31221508979797363

bam2 = timeit(stmt=test_format, number=1000000)
print(bam2)
# 0.5489029884338379