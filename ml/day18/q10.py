import tensorflow as tf
x=tf.random_uniform([3,2],minval=0,maxval=2)
sess=tf.Session()
out=sess.run(x)
print(out)
sess.close()
