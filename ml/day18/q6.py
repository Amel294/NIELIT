import tensorflow as tf
x=tf.constant([[1,3,5],[4,6,8]],tf.float32)
sess=tf.Session()
out=sess.run(x)
print(out)
sess.close()
