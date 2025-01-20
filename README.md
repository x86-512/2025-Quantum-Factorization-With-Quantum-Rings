# Challenge: Crack the Code with Quantum Factorization

Sponsored by Quantum Rings

## Overview

Shor's algorithm revolutionized our understanding of computational power, proving that quantum computers could solve problems far beyond the reach of classical systems. Now, in a space where innovation meets legacy—the halls of MIT, where Professor Shor himself still walks—we invite you to push the boundaries of quantum computing.

Welcome to the **Quantum Factorization Challenge**, where your mission is to factor increasingly larger semiprime integers using pure quantum algorithms. With access to the **Quantum Rings Simulator**, capable of simulating circuits with hundreds of qubits and millions of gate operations, all running on the qBraid platform, or on your local developer environment-- this is your chance to demonstrate mastery, ingenuity, and the future of quantum computation.


## Why Does This Matter?

At the heart of this challenge lies one of the most critical problems in modern cryptography: the difficulty of factoring large integers. Semiprime numbers, the product of two prime numbers, form the foundation of encryption methods like RSA. The security of these systems relies on the near impossibility of factoring large semiprimes using classical computers.

Quantum algorithms like Shor’s show that this problem can be solved efficiently in a quantum world, posing both opportunities and challenges for the future of cryptography. By participating in this challenge, you’re not just solving a problem—you’re contributing to advancements that could reshape cybersecurity, data privacy, and computational theory.

---

## What You’ll Be Doing

1. **Factor Large Semiprime Integers**  
   Use quantum algorithms to tackle a prepared list of semiprime integers, from approachable 14-bit numbers to a formidable 200-bit challenge.

2. **Leverage the Quantum Rings Simulator**  
   Use any quantum framework, but run all simulations on the Quantum Rings Simulator, delivering unmatched precision and scalability. (We recommend qiskit)

3. **Focus on Pure Quantum Solutions**  
  Classical optimizations are off the table—this challenge is about harnessing the full power of quantum algorithms.

---

## Scoring Breakdown

Submissions will be evaluated on:

- **Performance (80%)**: Size of the largest integer successfully factored from the provided list.
- **Universality (10%)**: Adaptability to any integer, but must work on the semi0primes provided of varying sizes.
- **Documentation (10%)**: Clear, concise, and insightful explanations of your approach.

---

## The Numbers You’ll Face

A sample from the semiprime integer list (full list in [semiprimes.py](./semiprimes.py)):

### Beginner Level
- **14 bits**: 11009  
- **16 bits**: 47053  
- **18 bits**: 167659  

### Intermediate Level
- **20 bits**: 744647  
- **24 bits**: 11426971  
- **30 bits**: 857830637  

### Advanced Level
- **36 bits**: 52734393667  
- **40 bits**: 862463409547  
- **50 bits**: 696252032788709  

### Insane Level
- **60 bits**: 827414216976034907  
- **80 bits**: 839063370715343025081359  
- **100 bits**: 793334180624272295351382130129  
- **120 bits**: 1153151809972770124185028131269906357  
- **200 bits**: 1292650905825941096257239453478790385594125558306176183893071  

As you go, you may want to start small, and scale up.  Keep in mind that simulation time may be a bottle neck, so getting a working implementation quickly for smaller numbers is key, so you can estimate the time it will take to run your algorithm on larger numbers.  Keep in mind that 80% of your score is going to be based on the largest integer you are able to factorize from the list.

---

## Submission Guidelines

Submit the following:

1. **Code**: Provide your quantum implementation, ensuring compatibility with Quantum Rings' backend simulator via Git Hub. 
2. **Results**: Include the integers factored, their prime factors, the number of qubits used, the number of gate operations, and the execution times.
3. **Documentation**: Explain your algorithm, scalability, and insights into any learnings or novelty in your approach.

---

## What You’ll Get

In addition to a chance to compete for the challenge prize, all participants will get:

- Access to the Quantum Rings Simulator with 200 qubits for one year after the hackathon (non-commercial use).
- Support from the Quantum Rings community and staff to assist with simulator-related questions during the event.
- Hands-on experience with cutting-edge quantum computing challenges.

---

Good luck-- let's see what you can achieve!