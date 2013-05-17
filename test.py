# -*- coding: utf-8 -*-
#!/usr/bin/env python

from automata import DFA


Q = ['A', 'B', 'C']
E = ['0','1']
q0 = 'A'
qf = ['C']

d = DFA()
d.states = Q
d.alphabet = E
d.q0 = q0
d.qf = qf
d.name = 'VM'
d.text = 'A DFA to model a vending machine'

d.addArc('A','1','B')
d.addArc('B','0','B')
d.addArc('B','1','C')
d.addArc('C','1','C')
d.addArc('C','0','C')

print d.delta
d.parse('11001')
d.transitionTable()

d.definition()