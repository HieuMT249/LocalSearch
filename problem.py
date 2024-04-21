import numpy as np
import matplotlib.pyplot as plt
import cv2
import random

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
        return self.X, self.Y, self.Z
        
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

    def generate_start_state(self):
        X = random.choice(self.X)
        Y = random.choice(self.Y)
        return [X, Y,random.randint(0,255)]
    
    def get_evaluation(self, state):
        return state[2]
    
    def get_neighbors(self, state):
        x, y, z = state
        neighbors = []
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                new_x = x + dx
                new_y = y + dy
                # Check if the new position is within bounds
                if 0 <= new_x < self.w and 0 <= new_y < self.h:
                    neighbors.append((new_x, new_y, self.Z[new_y, new_x]))
        return neighbors
    