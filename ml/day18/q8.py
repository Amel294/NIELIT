import tensorflow as tf
x=tf.linspace(5.0,10.0,50, name="linspace")
sess=tf.Session()
out=sess.run(x)
print(out)
sess.close()
