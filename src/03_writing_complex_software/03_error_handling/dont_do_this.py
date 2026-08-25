try:
    something  # type: ignore[name-defined]  # noqa: F821  # bare except below hides even this
except:  # noqa: E722
    pass
