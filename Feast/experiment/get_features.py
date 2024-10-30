from pprint import pprint
from feast import FeatureStore
from datetime import datetime
import pandas as pd

store = FeatureStore(repo_path="feature_repo")

# The keys and filters for the information we want to obtain.
entity_df = pd.DataFrame.from_dict(
    {
        "channel_id": [1, 1, 5],
        "date": [
            datetime(2023, 11, 7),
            datetime(2023, 11, 6),
            datetime(2023, 11, 7),
        ],
    }
)

# The features we want to obtain.
feature_vector = store.get_historical_features(
    entity_df=entity_df,
    features=[
        "channel_daily_stats:channel_name",
        "channel_daily_stats:k_subscribers",
        "channel_daily_stats:30_days_k_views"
    ],
).to_df()

pprint(feature_vector)