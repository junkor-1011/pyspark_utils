"""
manage

- Under Construction
"""
import pyspark

from .SparkDriver import SparkDriver, GeoSparkDriver


def get_or_create_spark_session():
    """
    get or create sparkSession

    - enable setting configuration dynamically

    Note:
        - using construtor of SparkDriver TEMPORARY.
            - to do improve in future.
    """
    sd = SparkDriver()
    spark = sd.spark
    return spark


def get_or_create_geospark_session():
    """
    get or create sparkSession for geospark

    Note:
        - only work at spark2.x
            - error will occur in spark3.x
        - implementation is TEMPORARY.
    """
    gsd = GeoSparkDriver()
    spark = gsd.spark
    return spark
