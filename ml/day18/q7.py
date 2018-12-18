import tensorflow as tf
x=tf.fill([2,3],4)
sess=tf.Session()
out=sess.run(x)
print(out)
sess.close()
