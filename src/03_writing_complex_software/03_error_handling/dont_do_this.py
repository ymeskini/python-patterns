try:
    something  # type: ignore[name-defined]  # bare except below hides even this
except:
    pass
