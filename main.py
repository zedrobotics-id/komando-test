def hello(name: str = "World") -> str:
    """Sapa pengguna, menerima parameter name dengan default 'World'."""
    return f"Hello, {name}!"

if __name__ == "__main__":
    print(hello())
