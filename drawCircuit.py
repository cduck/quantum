'''
Class for drawing a Circuit in matplotlib or other output

matplotlib output is generated by the PlotQCircuit library:
https://github.com/rpmuller/PlotQCircuit

Multi-bit gates will be displayed on the last bit with the others drawn as
control bits.

Example:
```
    from circuit import QuantumCircuit
    from gate import *
    from util import pi
    from drawCircuit import DrawableCircuit

    circuit = QuantumCircuit()
    reg = circuit.newRegister(3, name='a')
    x, = circuit.borrowAncilla(1)

    H(reg)
    Rz(-3*pi/32)(reg[1])
    P(pi/2)(reg)
    SWAP(reg[1], x)
    CX(reg[0], x)
    CRz(pi/3)(reg[1], reg[2])

    drawable = DrawableCircuit(circuit, showArgs=True)
    drawable.plot(showLabels=True, scale=0.7)
```
'''

from circuit import QuantumCircuit
from displayUtil import angleToLatex


class DrawableCircuit:
    plotNameMap = {'CX':'CNOT', 'CCX':'TOFFOLI'}
    plotSpecial = {'M', 'CNOT', 'TOFFOLI', 'NOP', 'SWAP', 'CPHASE'}
    def __init__(self, circuit, showArgs=False):
        self.showArgs = showArgs
        self._buildFromCircuit(circuit)
    def _buildFromCircuit(self, circuit):
        self.history = list(circuit.history)  # Make a copy
        #self.labels = ['q{}'.format(i) for i in range(circuit.n)]
        self.labels = [None] * circuit.n
        for regName, bits in circuit.regNames.items():
            if regName == 'ancilla':
                for i, b in enumerate(bits):
                    self.labels[b] = '0'
            elif len(bits) == 1:
                self.labels[bits[0]] = regName
            else:
                for i, b in enumerate(bits):
                    self.labels[b] = '{}_{}'.format(regName, i)
    def _argToStr(self, arg):
        return angleToLatex(arg)
    def _gateNameStr(self, gate, nameMap={}, special=set()):
        name = nameMap.get(gate.name, gate.name)
        if self.showArgs and gate.args:
            return '${}({})$'.format(name, ','.join(
                                map(self._argToStr,gate.args)))
        elif name in special:
            return name
        else:
            return '${}$'.format(name)
    def plot(self, showLabels=True, scale=0.75):
        import PlotQCircuit.plot_quantum_circuit as pqc

        plotList = []
        for gate in self.history:
            name = self._gateNameStr(gate, self.plotNameMap, self.plotSpecial)
            if len(gate.bits) <= 0:
                bits = (0,)
            else:
                bits = gate.bits[::-1]
            entry = (name, *bits)
            plotList.append(entry)
        ids = range(len(self.labels))
        inits = {i:self.labels[i] for i in ids}
        pqc.plot_quantum_circuit(plotList, inits=inits, labels=ids,
                                 plot_labels=showLabels, scale=scale)

