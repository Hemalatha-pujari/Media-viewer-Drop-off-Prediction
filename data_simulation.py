import numpy as np
import pandas as pd

def generate_data(n=1200):
    np.random.seed(42)

    watch_time = np.random.randint(5, 120, n)
    pause_count = np.random.randint(0, 10, n)
    rewind_count = np.random.randint(0, 6, n)
    content_length = np.random.randint(30, 150, n)

    engagement_score = (watch_time / content_length) - (pause_count * 0.05)

    drop_off = (engagement_score < 0.5).astype(int)

    return pd.DataFrame({
        "watch_time": watch_time,
        "pause_count": pause_count,
        "rewind_count": rewind_count,
        "content_length": content_length,
        "drop_off": drop_off
    })
