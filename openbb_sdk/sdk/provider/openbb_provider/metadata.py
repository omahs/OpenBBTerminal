"""Metadata for the parameters of the Pydantic models."""

QUERY_DESCRIPTIONS = {
    "symbol": "Symbol to get data for.",
    "start_date": "Start date of the data, in YYYY-MM-DD format.",
    "end_date": "End date of the data, in YYYY-MM-DD format.",
    "weekly": "Whether to return weekly data.",
    "monthly": "Whether to return monthly data.",
    "period": "Period of the data to return (quarterly or annually).",
    "date": "A specific date to get data for.",
    "limit": "The number of data entries to return.",
    "countries": "The country or countries you want to get data.",
    "units": "The units you want to see.",
    "frequency": "The frequency you want to see.",
}

DATA_DESCRIPTIONS = {
    "date": "The date of the data.",
}
