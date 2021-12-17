from behave import given, when, then
from builder import *

@given('I have sum = {x:g}')
def step(context, x):
    context.x = x

@when('I sum the cost')
def step(context):
    context.x = sum_cost(context.x)

@then('I expect to get result = {result:g}')
def step(context, result):
    assert context.x == result
    
if __name__ == "__main__":
    given.main()