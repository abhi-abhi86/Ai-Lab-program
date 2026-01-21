import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def generate_dataset(n=200):
    x = []
    y = []
    
    # Generate random data
    random_x1 = np.random.rand(n)
    random_x2 = np.random.rand(n)
    
    for i in range(n):
        x1 = random_x1[i]
        x2 = random_x2[i]
        
        # y = ax1 + bx2 + c + noise
        term = 2 * x1 + 3 * x2 + np.random.rand()
        x.append([x1, x2])
        y.append(term)
        
    return np.array(x), np.array(y)

def main():
    # 1. Generate Data
    X, Y = generate_dataset(200)
    
    # 2. Visualize
    mpl_params = {'legend.fontsize': 12}
    plt.rcParams.update(mpl_params)
    
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    # Plot the points
    ax.scatter(X[:,0], X[:,1], Y, c='r', marker='o', label='Data Points')
    
    ax.set_xlabel('X1')
    ax.set_ylabel('X2')
    ax.set_zlabel('Y')
    ax.legend()
    
    print("Displaying 3D plot of dataset for Multiple Linear Regression...")
    plt.savefig('lab-10-output.png')
    print("Saved 3D plot to lab-10-output.png")
    # plt.show()

if __name__ == "__main__":
    main()