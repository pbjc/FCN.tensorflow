import matplotlib.cm as cm
import matplotlib.pyplot as plt
from PIL import Image

def main():
    for i in range(8):
        plt.subplot(1, 3, 1)
        plt.imshow(Image.open('logs/inp_{}.png'.format(i + 5)))
        plt.subplot(1, 3, 2)
        plt.imshow(Image.open('logs/gt_{}.png'.format(i + 5)), cmap=cm.Paired, vmin=0, vmax=151)
        plt.subplot(1, 3, 3)
        plt.imshow(Image.open('logs/pred_{}.png'.format(i + 5)), cmap=cm.Paired, vmin=0, vmax=151)
        plt.colorbar()
        plt.savefig('logs/compare_{}.png'.format(i+5))
        plt.show()

if __name__ == '__main__':
    main()
