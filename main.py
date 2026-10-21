def hello(name: str = "World") -> str:
    """Sapa pengguna."""
    return f"Hello, {name}!"

if __name__ == "__main__":
    print(hello())
