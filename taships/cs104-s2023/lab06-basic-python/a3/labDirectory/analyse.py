'''
    Function Call Analysis
'''

def analyser(func, *args):
    lut = {}
    calls = {}
    print(f'Function: {func.__name__}')
    print(f'Arguments: {args}')
    print(f'Answer: {func(lut,calls,*args)}')
    print(f'Lookups: {len(lut)}')
    print(f'Calls: {sum(calls.values())}')
    print('----------------------')
