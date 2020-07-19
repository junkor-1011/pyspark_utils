"""GeoSparkDriver"""

from pyspark import SparkConf
from pyspark.sql import SparkSession
from geospark.register import upload_jars
from geospark.register import GeoSparkRegistrator
from geospark.utils import GeoSparkKryoRegistrator, KryoSerializer

# conf
from .config import spark_session as conf_spark_session

from .SparkDriver import SparkDriver


class GeoSparkDriver(SparkDriver):
    """
    GeoSparkDriver

    Note:
        - for Spark2.x
            - not work well in Spark3.0.0
    """

    # OVERWRITE SparkSession's method
    def createSession(self):
        """
        create GeoSpark Session
        """
        if self.spark is None:
            appName = conf_spark_session.appName
            master = conf_spark_session.master
            conf_list = self.make_conf()
            spark = SparkSession\
                .builder\
                .appName(appName)\
                .master(master)\
                .enableHiveSupport()\
                .config("spark.serializer", KryoSerializer.getName) \
                .config("spark.kryo.registrator", GeoSparkKryoRegistrator.getName) \
                .config(conf=SparkConf().setAll(conf_list))\
                .getOrCreate()

            # for GeoSpark
            upload_jars()
            GeoSparkRegistrator.registerAll(spark)

            self.spark = spark

        else:
            logging.warning("WARNING: SparkSession is already created.")
