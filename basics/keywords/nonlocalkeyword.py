def outer():
    x = "outer value"
    
    def inner():
        nonlocal x
        x = "changed by inner func"
    
    inner()
    print(x)

outer()  # Output: changed by inner func
