title: 'Data Driven Optimization of Reduced Neuronal Models'

tags:
  - data driven optimization
  - reduced neuronal models
  - applied genetic algorithms
  - numba jit LLVM

authors:
  - name: Russell Jarvis
    affiliation: Previous PhD Neuroscience, Arizona State University
  - name: Rick Gerkin

date: June 2021

The quadratic non-linearity behavior of the Izhikevich model and the exponential non-linearity of the Adaptive Exponential (AdExp) 
models make them challenging to optimize, despite the fact that conductance based models are intinsically very non-linear too. 

For some choices of error functions the AdExp model, and the Izhikevich models give rise to highly corrogated and undulating error surfaces.
Although genetic algorithms are robust against local optima, in high dimensional problems (11 model parameters), corrogated patterns dominate each dimension in the 
error hyper-volume, and this greatly degrades the learnability of error surfaces, and so it also descreases the efficiency of the genetic algorithm.

In this tool/work-flow I present a workflow for optimizing reduced Neuron models, by choosing a small number of reliable feature sets that have been shown to work.


In contrast to very custom in-house solutions (Allen Brain, BluePyOpt). I present optimization based on a novel combination of tools and data sources. 

*numba jit code accelerated models (made by me).
*NeuronUnit for scaling/normalizing error functions in proportion to data observations.
*BluePyOpt Genetic Algorithm (a community standard optimizer).
*neo (for a community standard voltage container)

The workflow is generalizable for optimizing other models (GLIF, conductance based), and optimizing using multiple types of error functions (EFEL, neuronUnit) and data-sources Ephysiology, Spike train statistics.

Finally I present the tool in GUI form and I actively validate the tool with an app.


#, 10 multi-objective error functions) 

corrogations are occuring

infact have more cubic non-linearities.

In this work

Neuron models that behave like their biological counterparts are essential for computational neuroscience.
Reduced neuron models which abstract away biological mechanisms in the interest of speed and interpretability, 
have received much attention due to their utility in large scale simulations of the brain, but little care has been taken to ensure that these models
 exhibit behaviors that closely resemble real neurons.

In order to improve the verisimilitude of these reduced neuron models, I developed an optimizer that uses genetic algorithms to align model 
behaviors with those observed in experiments.
I verified that this optimizer was able to recover model parameters given only observed physiological data; however, I also found that reduced models nonetheless had 
limited ability to reproduce all observed behaviors, and that this varied by cell type and desired behavior.
These challenges can partly be surmounted by carefully designing the set of physiological features that guide the optimization. 


In summary, we found evidence that reduced neuron model optimization had the potential to produce reduced neuron models for only a limited range of neuron types.


[@Van Geit:2016]. While popular magazines, newspapers, and other outlets purposefully cater language #[1] @article{bluepyopt,
 AUTHOR={Van Geit, Werner  and  Gevaert, Michael  and  Chindemi, Giuseppe  and  Rössert, Christian  and  Courcol, Jean-Denis  and  Muller, Eilif Benjamin  and  Schürmann, Felix  and  Segev, Idan  and  Markram, Henry},
TITLE={BluePyOpt: Leveraging open source software and cloud infrastructure to optimise model parameters in neuroscience},
JOURNAL={Frontiers in Neuroinformatics},
VOLUME={10},
YEAR={2016},
NUMBER={17},
URL={http://www.frontiersin.org/neuroinformatics/10.3389/fninf.2016.00017/abstract},
DOI={10.3389/fninf.2016.00017},
ISSN={1662-5196}
}
