## Decouple

- Single responsibility Class
- Opening for expand and closing for modify
- Take advantage of inheritance and polymorphism
    - A variable declared in the form of a parent class, assigned to any child class that inherits from this parent class does not affect the execution of the program.
- Depends on abstruction not implementation
    - Abstruction shouldn't depends on details(implementation)
    - Details should depends on abstruction
- Use interfaces for describing relationship of classes
- Class should know as less as possible of the other classes it calls