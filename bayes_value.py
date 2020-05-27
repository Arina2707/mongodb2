# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 10:15:39 2020

@author: Arina27
"""

import math
from pomegranate import *

# factor group - 1
innovation = DiscreteDistribution({'yes': 0.80, 'no': 0.2})
design = DiscreteDistribution({'yes': 1, 'no': 0.0})
technical_strength = DiscreteDistribution({'yes': 0.11, 'no': 0.89})

# factor group - 2
lead_time = DiscreteDistribution({'yes': 0.2, 'no': 0.8})
volume_flexibility = DiscreteDistribution({'yes': 0.1, 'no': 0.9})
mix_flexibility = DiscreteDistribution({'yes': 0.4, 'no': 0.6})

# factor group - 3
continous_improvment = DiscreteDistribution({'yes': 0.3, 'no': 0.7})
quality_system = DiscreteDistribution({'yes': 0.15, 'no': 0.85})

# factor group - 4
delivery_reliability = DiscreteDistribution({'yes': 0.9, 'no': 0.1})
on_time_delivery = DiscreteDistribution({'yes': 0.45, 'no': 0.55})
geographical_location = DiscreteDistribution({'yes': 0.45, 'no': 0.55})

# factor group - 5
managment_vision = DiscreteDistribution({'yes': 0.9, 'no': 0.1})
strategic_fit = DiscreteDistribution({'yes': 0.45, 'no': 0.55})
university_affiliation = DiscreteDistribution({'yes': 0.45, 'no': 0.55})

# factor 1
technological_capability = ConditionalProbabilityTable(
    [['yes', 'no', 'yes', 'yes', 0.65],
     ['no', 'yes', 'yes', 'yes', 0.75],
     ['yes', 'yes', 'yes', 'yes', 0.95],
     ['no', 'no', 'yes', 'yes', 0.35],
     ['yes', 'no', 'no', 'yes', 0.35],
     ['no', 'yes', 'no', 'yes', 0.25],
     ['yes', 'yes', 'no', 'yes', 0.6],
     ['no', 'no', 'no', 'yes', 0.05],
     ['yes', 'no', 'yes', 'no', 0.35],
     ['no', 'yes', 'yes', 'no', 0.25],
     ['yes', 'yes', 'yes', 'no', 0.05],
     ['no', 'no', 'yes', 'no', 0.65],
     ['yes', 'no', 'no', 'no', 0.65],
     ['no', 'yes', 'no', 'no', 0.75],
     ['yes', 'yes', 'no', 'no', 0.4],
     ['no', 'no', 'no', 'no', 0.95]], [innovation, design, technical_strength])

# factor 2
flexibility = ConditionalProbabilityTable(
    [['yes', 'no', 'yes', 'yes', 0.65],
     ['no', 'yes', 'yes', 'yes', 0.75],
     ['yes', 'yes', 'yes', 'yes', 0.95],
     ['no', 'no', 'yes', 'yes', 0.35],
     ['yes', 'no', 'no', 'yes', 0.35],
     ['no', 'yes', 'no', 'yes', 0.25],
     ['yes', 'yes', 'no', 'yes', 0.6],
     ['no', 'no', 'no', 'yes', 0.05],
     ['yes', 'no', 'yes', 'no', 0.35],
     ['no', 'yes', 'yes', 'no', 0.25],
     ['yes', 'yes', 'yes', 'no', 0.05],
     ['no', 'no', 'yes', 'no', 0.65],
     ['yes', 'no', 'no', 'no', 0.65],
     ['no', 'yes', 'no', 'no', 0.75],
     ['yes', 'yes', 'no', 'no', 0.4],
     ['no', 'no', 'no', 'no', 0.95]], [lead_time, volume_flexibility, mix_flexibility])

# factor - 3
quality = ConditionalProbabilityTable(
    [['yes', 'no', 'yes', 0.65],
     ['no', 'yes', 'yes', 0.75],
     ['yes', 'yes', 'yes', 0.95],
     ['no', 'no', 'yes', 0.35],
     ['yes', 'no', 'no', 0.35],
     ['no', 'yes', 'no', 0.25],
     ['yes', 'yes', 'no', 0.05],
     ['no', 'no', 'no', 0.65],
     ['yes', 'no', 'yes', 0.65]], [continous_improvment, quality_system])

# factor 4
delivery = ConditionalProbabilityTable(
    [['yes', 'no', 'yes', 'yes', 0.65],
     ['no', 'yes', 'yes', 'yes', 0.75],
     ['yes', 'yes', 'yes', 'yes', 0.95],
     ['no', 'no', 'yes', 'yes', 0.35],
     ['yes', 'no', 'no', 'yes', 0.35],
     ['no', 'yes', 'no', 'yes', 0.25],
     ['yes', 'yes', 'no', 'yes', 0.6],
     ['no', 'no', 'no', 'yes', 0.05],
     ['yes', 'no', 'yes', 'no', 0.35],
     ['no', 'yes', 'yes', 'no', 0.25],
     ['yes', 'yes', 'yes', 'no', 0.05],
     ['no', 'no', 'yes', 'no', 0.65],
     ['yes', 'no', 'no', 'no', 0.65],
     ['no', 'yes', 'no', 'no', 0.75],
     ['yes', 'yes', 'no', 'no', 0.4],
     ['no', 'no', 'no', 'no', 0.95]], [delivery_reliability, on_time_delivery, geographical_location])

# factor 5
org_culture_strategy = ConditionalProbabilityTable(
    [['yes', 'no', 'yes', 'yes', 0.65],
     ['no', 'yes', 'yes', 'yes', 0.75],
     ['yes', 'yes', 'yes', 'yes', 0.95],
     ['no', 'no', 'yes', 'yes', 0.35],
     ['yes', 'no', 'no', 'yes', 0.35],
     ['no', 'yes', 'no', 'yes', 0.25],
     ['yes', 'yes', 'no', 'yes', 0.6],
     ['no', 'no', 'no', 'yes', 0.05],
     ['yes', 'no', 'yes', 'no', 0.35],
     ['no', 'yes', 'yes', 'no', 0.25],
     ['yes', 'yes', 'yes', 'no', 0.05],
     ['no', 'no', 'yes', 'no', 0.65],
     ['yes', 'no', 'no', 'no', 0.65],
     ['no', 'yes', 'no', 'no', 0.75],
     ['yes', 'yes', 'no', 'no', 0.4],
     ['no', 'no', 'no', 'no', 0.95]], [managment_vision, strategic_fit, university_affiliation])

# value 1
material_value = ConditionalProbabilityTable(
    [['yes', 'no', 'yes', 'yes', 0.65],
     ['no', 'yes', 'yes', 'yes', 0.75],
     ['yes', 'yes', 'yes', 'yes', 0.95],
     ['no', 'no', 'yes', 'yes', 0.35],
     ['yes', 'no', 'no', 'yes', 0.35],
     ['no', 'yes', 'no', 'yes', 0.25],
     ['yes', 'yes', 'no', 'yes', 0.6],
     ['no', 'no', 'no', 'yes', 0.05],
     ['yes', 'no', 'yes', 'no', 0.35],
     ['no', 'yes', 'yes', 'no', 0.25],
     ['yes', 'yes', 'yes', 'no', 0.05],
     ['no', 'no', 'yes', 'no', 0.65],
     ['yes', 'no', 'no', 'no', 0.65],
     ['no', 'yes', 'no', 'no', 0.75],
     ['yes', 'yes', 'no', 'no', 0.4],
     ['no', 'no', 'no', 'no', 0.95]], [technological_capability, delivery, quality])

# value 2
spiritual_value = ConditionalProbabilityTable(
    [['yes', 'no', 'yes', 0.65],
     ['no', 'yes', 'yes', 0.75],
     ['yes', 'yes', 'yes', 0.95],
     ['no', 'no', 'yes', 0.35],
     ['yes', 'no', 'no', 0.35],
     ['no', 'yes', 'no', 0.25],
     ['yes', 'yes', 'no', 0.05],
     ['no', 'no', 'no', 0.65],
     ['yes', 'no', 'yes', 0.65]], [flexibility, org_culture_strategy])

# value 3
cost_value = DiscreteDistribution({'overpriced': 0.4, 'adequate': 0.6})

# overall_value
overall_value = ConditionalProbabilityTable(
    [['yes', 'no', 'adequate', 'yes', 0.65],
     ['no', 'yes', 'adequate', 'yes', 0.75],
     ['yes', 'yes', 'adequate', 'yes', 0.95],
     ['no', 'no', 'adequate', 'yes', 0.35],
     ['yes', 'no', 'overpriced', 'yes', 0.35],
     ['no', 'yes', 'overpriced', 'yes', 0.25],
     ['yes', 'yes', 'overpriced', 'yes', 0.6],
     ['no', 'no', 'overpriced', 'yes', 0.05],
     ['yes', 'no', 'adequate', 'no', 0.35],
     ['no', 'yes', 'adequate', 'no', 0.25],
     ['yes', 'yes', 'adequate', 'no', 0.05],
     ['no', 'no', 'adequate', 'no', 0.65],
     ['yes', 'no', 'overpriced', 'no', 0.65],
     ['no', 'yes', 'overpriced', 'no', 0.75],
     ['yes', 'yes', 'overpriced', 'no', 0.4],
     ['no', 'no', 'overpriced', 'no', 0.95]], [material_value, spiritual_value, cost_value])

# criterion
s1 = State(innovation, name="Innovation")
s2 = State(design, name="Design")
s3 = State(technical_strength, name="Technical strength")
s4 = State(lead_time, name="Lead time")
s5 = State(volume_flexibility, name="Volume flexibility")
s6 = State(mix_flexibility, name="Mix flexibility")
s7 = State(continous_improvment, name="Continuous improvment")
s8 = State(quality_system, name="Quality system")
s9 = State(delivery_reliability, name="Delivery reliability")
s10 = State(on_time_delivery, name="On time delivery")
s11 = State(geographical_location, name="Geographical location")
s12 = State(managment_vision, name="Managment vision")
s13 = State(strategic_fit, name="Strategic fit")
s14 = State(university_affiliation, name="University affiliation")

# factor
s15 = State(technological_capability, name="Technological capability")
s16 = State(flexibility, name="Flexibility")
s17 = State(quality, name="Quality")
s18 = State(delivery, name="Delivery")
s19 = State(org_culture_strategy, name="Org culture and strategy")

# value
s20 = State(material_value, name="Material value")
s21 = State(spiritual_value, name="Spiritual value")
s22 = State(cost_value, name="Cost value")
s23 = State(overall_value, name="Overall value")

network = BayesianNetwork("Supplier impact on risk:")
network.add_states(s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12, s13, s14, s15, s16, s17, s18, s19, s20, s21, s22,
                   s23)

network.add_edge(s1, s15)
network.add_edge(s2, s15)
network.add_edge(s3, s15)

network.add_edge(s4, s16)
network.add_edge(s5, s16)
network.add_edge(s6, s16)

network.add_edge(s7, s17)
network.add_edge(s8, s17)

network.add_edge(s9, s18)
network.add_edge(s10, s18)
network.add_edge(s11, s18)

network.add_edge(s12, s19)
network.add_edge(s13, s19)
network.add_edge(s14, s19)

network.add_edge(s15, s20)
network.add_edge(s17, s20)
network.add_edge(s18, s20)

network.add_edge(s16, s21)
network.add_edge(s19, s21)

network.add_edge(s20, s23)
network.add_edge(s21, s23)
network.add_edge(s22, s23)

network.bake()

beliefs = network.predict_proba(
    {'innovation': 'yes', 'design': 'yes', 'technical_strength': 'yes', 'lead_time': 'yes', 'volume_flexibility': 'yes',
     'mix_flexibility': 'yes', 'continous_improvment': 'yes', 'quality_system': 'yes', 'delivery_reliability': 'yes',
     'on_time_delivery': 'yes', 'geographical_location': 'yes', 'managment_vision': 'yes', 'strategic_fit': 'yes',
     'university_affiliation': 'yes'})

beliefs1 = network.predict_proba()

beliefs1 = map(str, beliefs1)
print("\n".join("{}{}".format(state.name, belief) for state, belief in zip(network.states, beliefs1) if
                state.name == "Overall value"))

network.plot()
