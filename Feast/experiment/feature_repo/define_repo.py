from datetime import timedelta

import pandas as pd

from feast import (
    Entity,
    FeatureService,
    FeatureView,
    Field,
    FileSource,
    PushSource,
    RequestSource,
)
from feast.on_demand_feature_view import on_demand_feature_view
from feast.types import Int64, String

channel = Entity(name="channel", join_keys=["channel_id"])

channel_stats_source = FileSource(
    name="channel_daily_stats_source",
    path="C:/Users/felip/OneDrive/Documentos/GitHub/MLOps/Feast/experiment/feature_repo/data/channels.parquet",
    timestamp_field="date",
    created_timestamp_column="created",
)

# Here we define a Feature View that will allow us to serve the
# channel data to our model online.
channel_stats_fv = FeatureView(
    name="channel_daily_stats",
    entities=[channel],
    ttl=timedelta(days=1),
    # The list of features defined below act as a schema to both define features
    # for both materialization of features into a store, and are used as references
    # during retrieval for building a training dataset or serving features
    schema=[
        Field(name="channel_name", dtype=String),
        Field(name="k_subscribers", dtype=Int64),
        Field(name="30_days_k_views", dtype=Int64, description="Average daily channel stats"),
    ],
    online=True,
    source=channel_stats_source,
    # Tags are user defined key/value pairs that are attached to each
    # feature view
    tags={"team": "youtube_analytics"},
)