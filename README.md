# Testing
## Discussion Questions
1. Say I give you a spec to implement, how will you check that what you built works?
2. What if I hand the code to Henry and give him a new spec. How will he check his work? How will he make sure he didn't break all of your functionality?
3. What if we have to make a sweeping change to a part of the API but we don't want it to affect the other parts. How can we be confident that we haven't broken anything?
4. When should we not write tests? When is manual QA good enough?

## Types of tests
## Unit tests
Example: We have a function `uppercase_if_longer_than_8_characters` that should take a string and return it uppercased only if it's longer than 8 characters, otherwise it does nothing.

```python
def uppercase_if_longer_than_8_characters(value):
    if len(value) > 8:
        return value.upper()
    return value

def test_longer_than_8():
    assert uppercase_if_longer_than_8_characters("suneelius") == "SUNEELIUS"

def test_NOT_longer_than_8():
    assert uppercase_if_longer_than_8_characters("daniel") == "daniel"
```

## Functional tests
We have a function that takes a `username` and `id` and finds the `User` with that `id` in the DB and updates its username to be the username passed in.

Write a test that calls that function and then checks that the User record in the db is updated.

## Integration tests
We have a function that takes a Stripe token and hits the Stripe API to return a list o their most recent transactions.

Write a test that creates a Stripe token and a list of transactions associated with this token using the Stripe API. Then call this function with the Stripe token and then check that the returned transaction list matches the one we created.

## Inductive Learning
Let's see how we can use testing to make a complex problem simpler.

Suppose we are building a financial transaction cleaning algorithm. Our job is to take raw financial transaction data, hit our NameCleaningAPI, our CategorizationAPI and our GeolocationAPI.

The NameCleaningAPI will return (clean_name, confidence value)
The CategorizationAPI will return (category, confidence value)
The GeolocationAPI will return (city, state, confidence value)

Implement a combiner that will take an incoming transaction string and return a nice dictionary of cleaned data according to the following rules:

1. If the categorization confidence is greater than .7 include it
2. If the geolocation confidence is greater than .8 include it
3. If the name confidence is greater than .65 include it
4. If the name confidence is lower than .65, no matter what return None.



