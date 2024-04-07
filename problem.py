import numpy as np
import matplotlib.pyplot as plt
import cv2

class Problem:
    def __init__(self, filename):
        self.img_path = filename
        self.load_state_space()
        
    def load_state_space(self):
        img = cv2.imread(self.img_path, cv2.IMREAD_GRAYSCALE)
        img = cv2.resize(img, (0, 0), fx=0.25, fy=0.25)
        img = cv2.GaussianBlur(img, (5, 5), 0)
        self.h, self.w = img.shape
        self.X = np.arange(self.w)
        self.Y = np.arange(self.h)
        self.Z = img 
        
    def show(self):
        X, Y = np.meshgrid(self.X, self.Y)
        fig = plt.figure(figsize=(8,6))
        self.ax = plt.axes(projection='3d')
        # draw state space (surface)
        self.ax.plot_surface(X, Y, self.Z, rstride=1, cstride=1, cmap='viridis', edgecolor='none')
        
    def draw_path(self, path):
        ae = self.show()
        xs = [point[0] for point in path]
        ys = [point[1] for point in path]
        zs = [self.Z[point[1], point[0]] for point in path]
        self.ax.plot(xs, ys, zs, 'r-', zorder=3, linewidth=0.5)
        plt.show()

            
    
    