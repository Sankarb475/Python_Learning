import org.apache.spark.SparkConf
import org.apache.spark.sql.SparkSession
import org.apache.spark.streaming.{Seconds, StreamingContext}
import org.apache.kafka.common.serialization.StringDeserializer
import org.apache.spark.streaming.kafka010._


object KafkaSpark extends App{
  System.setProperty("hadoop.home.dir", "D:\\App\\hadoop_2.7.1")

  val conf = new SparkConf().setMaster("local[*]").setAppName("KafkaSparkStreaming")
  val spark = SparkSession.builder().config(conf).getOrCreate()

  val sc = spark.sparkContext

  val ssc = new StreamingContext(sc, Seconds(10))

  val topicsSet = Set("test-log")


  val kafkaParams = Map[String, Object](
    "bootstrap.servers" -> "localhost:9092",
    "key.deserializer" -> classOf[StringDeserializer],
    "value.deserializer" -> classOf[StringDeserializer],
    "group.id" -> "kafka_spark",
    "auto.offset.reset" -> "latest"
  )

  //consume the messages from Kafka topic and create DStream
  val LogsStream = KafkaUtils
    .createDirectStream[String, String](ssc, LocationStrategies.PreferConsistent, ConsumerStrategies.Subscribe[String, String]
      (topicsSet,kafkaParams))


  val messages=LogsStream.map(_.value())
  case class schema(ID: Int, First: String, Last: String, Salary: Int, Currency: String)

  import spark.implicits._
  val df = messages.map(x => x.split(',')).map(field => schema(field(0).toInt, field(1), field(2), field(3).toInt, field(4)))
    .toDF("ID", "First", "Last", "Salary", "Currency")

  val words=messages.flatMap(x=>x.split(','))
  val counts=words.map(x=>(x,1)).reduceByKey(_+_)
  counts.print()


  ssc.start()
  ssc.awaitTermination()
}
