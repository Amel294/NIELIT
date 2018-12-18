import tensorflow as tf
x=tf.zeros([2,3],tf.int32)
sess=tf.Session()
output=sess.run(x)
print(output)
sess.close()
