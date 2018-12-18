import tensorflow as tf
x=tf.random_normal([3,2],stddev=2)
sess=tf.Session()
out=sess.run(x)
print(out)
sess.close()
