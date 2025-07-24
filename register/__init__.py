from .reg_telegram import register_telegram
# from .reg_slack import register_slack (future)

__all__ = ["register_telegram"]

def register(platform: str, **kwargs):
    if platform == "telegram":
        return register_telegram(**kwargs)
    # elif platform == "slack":
    #     return register_slack(**kwargs)
    else:
        raise ValueError(f"Unknown platform: {platform}")
