# -*- coding: utf-8 -*-
"""2-qubit-quantum-circuit.py

"""

!pip install qiskit
!pip install pylatexenc

# Commented out IPython magic to ensure Python compatibility.
from qiskit import *
from qiskit.tools.visualization import plot_histogram
from qiskit import IBMQ
from qiskit.tools.monitor import job_monitor

qr = QuantumRegister(2)
cr = ClassicalRegister(2)
circuit = QuantumCircuit(qr, cr)
# %matplotlib inline
circuit.h(qr[0])
#circuit.draw(output='mpl')

circuit.cx(qr[0], qr[1])

circuit.measure(qr, cr)
circuit.draw()

simulator = Aer.get_backend('qasm_simulator')

result = execute(circuit, backend=simulator).result()

plot_histogram(result.get_counts(circuit))

provider = IBMQ.load_account()
#IBMQ account key
#IBMQ.save_account('')

provider = IBMQ.get_provider(hub='ibm-q')
provider = IBMQ.get_provider(group='open')


#There are a limited number of backends check the list before starting your calculations.
backend = provider.get_backend('ibmq_bogota')

job = execute(circuit, backend)
job_monitor(job)

result = job.result()

plot_histogram(result.get_counts(circuit))
