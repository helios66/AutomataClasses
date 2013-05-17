
# -*- coding: utf-8 -*-
#!/usr/bin/env python

class DFA:
	'''
	This class represents the DFA
	'''
	def __init__(self):
		'''
		This creates a new DFA with the following elements

		Inputs
		--------------------------------------------------
		states => A non-empty set of states

		'''
		self.states = []
		self.alphabet = []
		self.delta = {}
		self.q0 =''
		self.qf = []
		self.text = ''
		self.name = ''

	def addArc(self,q1,s,q2):
		'''
		Adds an arc to a DFA
		'''
		if (q1,s) not in self.delta:
			self.delta[(q1,s)] = q2
		elif self.delta[(q1,s)] != q2:
			self.delta[(q1,s)] = q2

	def rmArc(self,q1,s,q2):
		'''
		Removes an Arc
		'''
		if (q1,s) in self.delta and self.delta[(q1,s)] == q2:
			self.delta.pop((q1,s))

	def transitionTable(self):
		'''
		Prints out the transition table of a DFA
		'''
		delta2 = {}
		print '\nTransition Table for DFA'
		print '-------------------------------'
		r = ''
		for s in sorted(self.states):
			r += ' |'+s+'\t'
		print r
		print '-------------------------------'
		for (q1,sym),q2 in self.delta.iteritems():
			if (q1,q2) not in delta2:
				delta2[(q1,q2)] = [sym] 
			else:
				delta2[(q1,q2)].append(sym)

		for si in sorted(self.states):
			a = si
			for sj in sorted(self.states):
				a += '|'+self.str2(delta2[(si,sj)])+'\t ' if (si,sj) in delta2 else '|\t '				
			print a
		print '-------------------------------'

	def str2(self,l):
		out =''
		for i in l:
			out += i
		return out

	def parse(self, input):
		'''
		Takes an input string and checks if it is accepted or rejected by the DFA
		'''
		sym =  []
		p = []
		for cursym in input:
			sym.append(cursym)
		current = self.q0
		for j in range(0,len(sym)):
			next = self.transit(current, sym[j])
			if next == None:
				break
			else:
				p.append([current, sym[j], next])
			current = next
		print p		
		print 'String Accepted' if next in self.qf else 'String Rejected'

	def transit(self,current,j):
		'''
		Gets the next state given the current state and current symbols

		input
		-----------
		current - Current state
		j - Current symbols

		Returns the next states
		'''
		return self.delta[((current,j))] if (current,j) in self.delta else None

	def definition(self):
		'''
		Prints out the formal definition of a DFA
		'''
		print '\nThe DFA', self.name,'is defined as:'
		print self.name,'= <Q, Σ, qo, qf, δ>\n\nWhere:'
		print '\tQ is a finite set of states\n\tQ = {',self.states,'}'
		# ØδΣ
		print '\tΣ is a finite set of input symbols\n\tΣ = {',self.alphabet,'}'
		print '\tq0 = an initial state\n\tq0 = ',self.q0
		print '\tqf is a finite set of final states\n\tqf = {',self.qf,'}'
		print '\tδ is a set of mapping function given as Q x Σ → Q: \n\t', self.transitionTable()

	# def verify(self):
	# 	'''

	# 	'''
	# 	if self.q0 = 