# Test

Test private variables/methods
- Not need test
    - If the variables or methods are not publicly available in any way at all, then it makes no sense to test it, because obviously it doesn't matter to any client code.
    - Unit testing is about testing behavior of your classes; not implementation details.
    - You don't test if private fields do have this or that content. The only thing you test is that methods do what they are supposed to do.
- Test anyway
    - Java reflections to access the private fields/methods
    - Test private variables in public method, or `getters()`
    - If we create a package in the test directory with the same name of the package of the class, and if we put the field in protected we will be able to access the field directly.
