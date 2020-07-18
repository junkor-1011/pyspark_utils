"""GeoSparkDriver"""

from geospark.register import upload_jars
from geospark.register import GeoSparkRegistrator

from .SparkDriver import SparkDriver


class GeoSparkDriver(SparkDriver):
    """
    GeoSparkDriver
    """

    def __init__(self):
        self.createSession()
        spark = self._spark

        # for geospark
        upload_jars()
        GeoSparkRegistrator.registerAll(spark)
        self._spark = spark
