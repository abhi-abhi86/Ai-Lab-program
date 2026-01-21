# AI Lab Program

This repository contains various AI and Computer Vision lab programs implemented in Python.

## Requirements

To run these programs, you will need Python installed along with the following libraries:

- `numpy`
- `matplotlib`
- `opencv-python`

You can install the required dependencies using pip:

```bash
pip install numpy matplotlib opencv-python
```

## Lab List and Outputs

### lab-1.py: Traveling Salesman Problem (TSP) using Hill Climbing
**Description**: Solves the TSP for a 4-city problem using a stochastic hill climbing approach.
**Output**:
```
Optimal Path: [3, 1, 0, 2]
Total Distance: 80
```
*(Note: Output path may vary due to randomization)*

### lab-2.py: Iterative Deepening Depth First Search (IDDFS) & DLS
**Description**: Performs graph reachability checks using IDDFS and DLS.
**Output**:
```
Target is reachable from source within max depth 3
```

### lab-3.py: Depth Limited Search (DLS)
**Description**: Traverses a nested list structure up to a specified depth limit.
**Output**:
```
Starting Depth Limited Search with limit 2:
At depth 1: processing element: 1
At depth 1: encountered nested list, diving deeper...
At depth 2: processing element: 2
At depth 2: processing element: 3
At depth 1: encountered nested list, diving deeper...
At depth 2: processing element: 4
At depth 2: encountered nested list, diving deeper...
At depth 1: processing element: 7
At depth 1: encountered nested list, diving deeper...
At depth 2: processing element: 8
At depth 2: processing element: 9
```

### lab-4.py: Find-S Algorithm
**Description**: Implements the Find-S algorithm to learn the maximally specific hypothesis from positive training examples.
**Output**:
```
Training Examples:
(['Sunny', 'Warm', 'Normal', 'Strong', 'Warm', 'Same'], 'Yes')
(['Sunny', 'Warm', 'High', 'Strong', 'Warm', 'Same'], 'Yes')
(['Rainy', 'Cold', 'High', 'Strong', 'Warm', 'Change'], 'No')
(['Sunny', 'Warm', 'High', 'Strong', 'Cool', 'Change'], 'Yes')

The Maximally Specific Hypothesis is: ['Sunny', 'Warm', '?', 'Strong', '?', '?']
```

### lab-5.py: Forward Chaining
**Description**: A rule-based system employing forward chaining to infer a query conclusion from known facts.
**Output**:
```
Known Facts: ['A', 'B', 'E']
Query: F
Inferring C from ['A', 'B']
Inferring D from ['C']
Inferring F from ['D', 'E']
Success: F can be inferred.
```

### lab-6.py: Backward Chaining
**Description**: Simple backward chaining algorithm to prove a goal by working, working backwards to known facts.
**Output**:
```
Facts: ['A', 'D'], Query: E
Success: Can prove E
```

### lab-7.py: Simple Chatbot
**Description**: A command-line based interaction loop.
**Sample Output**:
```
Chatbot: Hello! Type 'bye' to exit.
You: hi
Chatbot: Hello! How can I help you?
You: what is your name
Chatbot: I am a simple Python Chatbot.
You: bye
Chatbot: Goodbye! Have a nice day.
```

### lab-8.py: Hough Circle Transform
**Description**: Detects circles in an image (`smarties.png` by default) using OpenCV.
**Output**: 
![Lab 8 Output](lab-8-output.png)
*(Result of detecting circles on synthetic input)*

### lab-9.py: Template Matching
**Description**: Finds a template image within a larger main image using various matching methods.
**Output**:
![Lab 9 Output](lab-9-output.png)
*(Template matching result using cv2.TM_CCOEFF)*

### lab-10.py: Multiple Linear Regression (Visualization)
**Description**: Generates a dummy 3D dataset and visualizes it.
**Output**:
![Lab 10 Output](lab-10-output.png)