# References : 

# Weight Optimisation of Neural Network using Genetic Algorithm

Weight optimization of a neural network using a genetic algorithm involves using the principles of evolution to find the optimal set of weights that minimizes the network's loss function. The genetic algorithm starts by generating a population of potential solutions, where each solution represents a set of weights for the neural network. The fitness of each solution is then evaluated by calculating the loss function for the corresponding network. The fittest individuals are selected to "breed" the next generation of solutions.

The breeding process involves crossover and mutation. Crossover involves selecting two parent solutions and combining their weights to create a new child solution. Mutation involves randomly modifying the weights of a solution to introduce new variations.

The newly generated population is then evaluated for fitness, and the process repeats until a satisfactory solution is found, or a maximum number of iterations is reached.

The genetic algorithm provides a powerful optimization technique that can be used to improve the accuracy and performance of neural networks.


## References

#### Research paper: 
* [Training Feedforward Neural Networks Using Genetic Algorithms](https://github.com/SG-Akshay10/Dynamic_Programming/blob/main/CIA2/Reference/Training%20Feedforward%20Neural%20Networks%20Using%20Genetic%20Algorithms%5B2155%5D.pdf)

#### Website: 
* [Towardsdatascience](https://towardsdatascience.com/introduction-to-genetic-algorithms-including-example-code-e396e98d8bf3)

# Weight Optimisation of Neural Network using Particle Swarm Optimization

Particle Swarm Optimization (PSO) is a popular metaheuristic optimization algorithm that can be used to optimize the weights of a neural network. PSO is based on the behavior of swarms in nature, where each individual particle adjusts its position based on its own experience and the experience of the best particle in the swarm.

Weight optimization of neural networks using Particle Swarm Optimization involves initializing a swarm of particles, where each particle represents a candidate solution for the weights of the neural network. The particles adjust their positions and velocities based on their current position, their previous best position, and the best position found by any particle in the swarm. The fitness function is evaluated for each particle's position, and the weights are updated based on the position of the particle with the best fitness value. This process is repeated for a number of iterations until a satisfactory solution is found. PSO has been shown to be an effective method for optimizing the weights of neural networks and can be used for a wide range of applications.

## References

#### Research paper: 
* [Particle Swarm Optimization](https://github.com/SG-Akshay10/Dynamic_Programming/blob/main/CIA2/Reference/Particle_swarm_optimization.pdf)

#### Website: 
* [Particle Swarm Optimization from Scratch with Python](https://nathanrooy.github.io/posts/2016-08-17/simple-particle-swarm-optimization-with-python/)

* [Swarm Intelligence: Coding and Visualising Particle Swarm Optimisation in Python](https://towardsdatascience.com/swarm-intelligence-coding-and-visualising-particle-swarm-optimisation-in-python-253e1bd00772)

# Weight Optimisation of Neural Network using Ant Colony Optimization

Ant Colony Optimization (ACO) is a metaheuristic optimization algorithm inspired by the behavior of ants searching for food. The idea of using ACO for weight optimization in neural networks is to treat the weights of the neural network as pheromones, which ants deposit and follow to find the shortest path to food.

The ACO algorithm can be used to optimize the weights of a neural network by treating them as pheromones that ants follow to find the shortest path to food. This approach involves initializing a pheromone matrix, generating an ant population to explore the weight space, constructing a neural network with random weights, and training the network. The pheromone matrix is updated based on the performance of the ants, and this process is repeated until the optimal weights are found. The use of ACO for weight optimization in neural networks can lead to improved accuracy and performance compared to other optimization algorithms.

## References

#### Research paper: 
* [Training feed-forward neural networks with ant colony optimization: An application to pattern classification](https://github.com/SG-Akshay10/Dynamic_Programming/blob/main/CIA2/Reference/ReferencePaperForACO.pdf)


# Comparision of Genetic Algorithm and Particle Swarm Optimization

Particle Swarm Optimization (PSO), Genetic Algorithm (GA), and Ant Colony Optimization (ACO) are examples of metaheuristic optimisation techniques used to solve challenging issues. Yet how they approach optimisation and how they apply it varies.

Natural selection and evolution are the sources of GA's inspiration. New generations of solutions are produced by applying selection, crossover, and mutation procedures on an initial population of solutions. The best solutions are chosen to build the following generation once each solution's fitness has been assessed. GA is frequently utilised in a variety of industries, including biology, banking, and engineering.

The behaviour of ants looking for food served as the basis for ACO. It entails developing answers by tracing pheromone trails left by earlier ants. The pheromone trail is updated based on how the ants perform, and the algorithm eventually finds the optimal answer. Routing and scheduling issues like the travelling salesman dilemma are frequently addressed with ACO.

PSO draws inspiration from both the schooling behaviour of fish and the flocking behaviour of birds. It involves moving particles that each have a position and velocity inside a search space. Based on the particle's best position and the swarm's best position, the velocity is updated. PSO is utilised in numerous applications, such as data mining, control systems, and image processing.

GA typically performs better when used to issues that have a big search space and few variables. PSO is more suited for continuous optimisation issues, while ACO is more successful for discrete optimisation issues with plenty of variables.

To sum up, GA, ACO, and PSO are strong optimisation algorithms that may be used to a variety of issues. The kind of problem at hand and the properties of the search space influence the method of choice.


#### Particle Swarm Optimization : 
![image](https://user-images.githubusercontent.com/83088512/230156228-0aa57cab-4ba2-450b-9f02-54d06d364d16.png)

#### Genetic Algorithm:
![image](https://user-images.githubusercontent.com/83088512/230156629-2190d699-48a1-4db5-9658-22ebc5afad56.png)

#### Ant Colony Optimization:
![image](https://user-images.githubusercontent.com/83088512/230175815-dcd43ff1-24e6-4793-a19a-c26ca0fac7bd.png)



