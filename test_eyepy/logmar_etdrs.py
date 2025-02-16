def logmar_to_etdrs(logmar: float) -> int:
    """
    Convert LogMAR to ETDRS

    Args:
        logmar (float): Visual acuity in **LogMAR** notation

    Returns:
        int: The corresponding ETDRS score
        
    Examples:
        >>> logmar = 0.3
        >>> etdrs = logmar_to_etdrs(logmar)
        >>> print(etdrs)
        70
    """
    etdrs = 85 - (50 * logmar)
    # print("Why hello you thingy bob")
    return int(round(etdrs))