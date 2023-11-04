# Es crucial manejar mismas versiones entre ambos ya que en el futuro esto nos causara errores

# Creamos un env para manejar versiones

# conda create --name ecomspy python=3.9
# conda activate ecomspy


# para ejecutar main.py es necesario especificar el master.

./spark-submit --master spark://MBPdeLucas880.fibertel.com.ar:7077 (config de memoria de ser necesario) main.py

luego del archivo agregar los parametros (rutas) de entrada y salida. 

Ej :
~/documents/projectos_data/ecommerce-cosmetic-shop  */documents/projectos_data/resultados-pyspark



Scrip final: 

./spark-submit --master spark://MBPdeLucas880.fibertel.com.ar:7077 --conf spark.executor.memory=4g main.py "~/documents/projectos_data/ecommerce-cosmetic-shop/*.csv"  "/documents/projectos_data/resultados-pyspark/ecommerce-cosmetic-shop"
