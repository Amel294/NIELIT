import tensorflow as tf
x=tf.fill([3,2],5)
sess=tf.Session()
out=sess.run(x)
print(out)
print(x)
sess.close()
