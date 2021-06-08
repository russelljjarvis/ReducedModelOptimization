import setuptools; setuptools.setup()
extras_require={'BluePyOpt': ['BluePyOpt @ git+git+https://github.com/russelljjarvis/BluePyOpt.git@neuronunit_reduced_cells']}
extras_require1={'neuronunit': ['neuronunit @ git+https://github.com/russelljjarvis/neuronunit.git@optimization']}
extras_require.update(extras_require1)
