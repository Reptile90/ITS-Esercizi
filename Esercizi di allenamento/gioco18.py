def compose(f,g):
    def compose(x):
        return f(g(x))
    return compose