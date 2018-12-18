import tensorflow as tf
x=tf.constant([[1, 2], [3, 4], [5, 6]],tf.int32)
y=tf.random_shuffle(x)
sess=tf.Session()
output=sess.run(x)
output1=sess.run(y)
print(output)
print(output1)
sess.close()
