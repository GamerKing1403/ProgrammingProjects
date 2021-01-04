from scipy import misc
import matplotlib.pyplot as plt
if __name__ == '__main__':
    face = misc.face()
    plt.imshow(face)
    plt.show()
