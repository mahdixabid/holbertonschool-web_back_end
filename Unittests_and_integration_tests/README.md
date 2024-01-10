# 0x09-Unittests_and_integration_tests

>>>  unittest and is based on the ‘action -> assertion’ pattern instead of ‘record -> replay’ used by many mocking frameworks.

- unit tests vs integration tests
- Use parametrization to generate dynamic tests
- learned about the subTest context manager in unittest


- learned about patch() method : [!https://docs.python.org/3/library/unittest.mock.html#unittest.mock.patch ]
- combining assertisEquel(fn(), None) with assertIsNone(fn())

> Mock an item where it is used, not where it came from.

> The Mock class of unittest.mock removes the need to create a host of stubs throughout your test suite

> 

assert Mock_obj is cls.fn()


Resources:
- https://daniel.perez.sh/blog/2017/unittest-assert-raises/
- https://medium.com/geekculture/right-way-to-test-mock-and-patch-in-python-b02138fc5040
- https://myadventuresincoding.wordpress.com/2011/02/26
- https://www.fugue.co/blog/2016-02-11-python-mocking-101#:~:text=How%20do%20we%20mock%20in,want%20or%20raise%20an%20Exception%20.
- https://gist.github.com/igniteflow/1be88c18185ffe42a66a46e48118f486