import tensorflow as tf
x=tf.ones([2,3],tf.int32)
sess=tf.Session()
output=sess.run(x)
print(x)
print(output)
sess.close()
                  
