from qiskit.circuit import QuantumCircuit

#from quantumrings.toolkit.qiskit import QrSamplerV1 as Sampler

import QuantumRingsLib 
from QuantumRingsLib import QuantumRegister, AncillaRegister, ClassicalRegister, QuantumCircuit
from QuantumRingsLib import QuantumRingsProvider
from QuantumRingsLib import job_monitor
from QuantumRingsLib import JobStatus

provider = QuantumRingsProvider(
    token='QRING Token Here',
    name='QRING EMail Here'
)
backend = provider.get_backend("scarlet_quantum_rings")
shots = 1024

provider.active_account()

def main():
    q = QuantumRegister(8, 'q')
    c = ClassicalRegister(8, 'c')
    qc = QuantumCircuit(q,c)
    qc.h([i for i in range(8)])
    qc.measure_all()
  
    job = backend.run(qc, shots=shots)
    job_monitor(job)
    result = job.result()
    counts = result.get_counts()
    print(counts)



if __name__=="__main__":
    main()
