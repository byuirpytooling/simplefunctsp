# %%
def divide(a: float, b: float) -> float:
    """Divide two numbers.

    This function is documented in a way that mkdocstrings can
    automatically extract and render.

    Args:
      a: float The first number to divide.
      b: float The second number to divide.

    Returns:
      float The sum of ``a`` and ``b``.

    Examples:
        >>> divide(10, 5)
        2
        >>> divide(20, 2)
        10
    """
    return a / b

# %%
