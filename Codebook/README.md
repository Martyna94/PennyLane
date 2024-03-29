* https://codebook.xanadu.ai/

Useful resource:
* https://discuss.pennylane.ai/
* https://realpython.com/python-complex-numbers/
* https://www.markdownguide.org/basic-syntax/
* Latex mathematical symbols : https://www.cmor-faculty.rice.edu/~heinken/latex/symbols.pdf

* rendering greece letter in markdown - https://rpruim.github.io/s341/S19/from-class/MathinRmd.html

Codebook materials are split into two parts: challenge and textbook. Challenge part is included in this project.
Textbook is included in the written notes.

C. Albornoz, G. Alonso, M. Andrenkov, P. Angara, A. Asadi, A. Ballon, S. Bapat, I. De Vlugt, O. Di Matteo, P. Finlay, A. Fumagalli, A. Gardhouse, N. Girard, A. Hayes, J. Izaac, R. Janik, T. Kalajdzievski, N. Killoran, J. Soni, D. Wakeham. (2021) Xanadu Quantum Codebook.
Useful information:
* `qml.probs(wires=range(n_bits))` - array[float]: Probabilities for observing different outcomes.
* `qml.state()` - array[complex]: The state of the qubit after the operations.
* all_states = [np.binary_repr(n, n_bits-1) for n in range(2**(n_bits-1))]
* `qml.Hamiltonian(coeffs, obs)` - qml.Hamiltonian: The Hamiltonian of the system.
* `qml.draw(X_plus_Z)(), plt.show()`
* `for index in range(2**k_bits): ctrl_str =  np.binary_repr(index, k_bits) # Create binary representation`
* `qml.broadcast(qml.Hadamard, wires=[i for i in range(n_bits)], pattern="single")`
* `zero_vec = np.array([1] + [0]*(2**k_bits - 1))`