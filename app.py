import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(context="paper", font="monospace")
#%matplotlib inline
SILENT = True
import warnings
if SILENT:
	warnings.filterwarnings("ignore")
import os
on_heroku = False
if 'YOUR_ENV_VAR' in os.environ:
  on_heroku = True
if not on_heroku:
	import sys
	sys.path.insert(0,'/home/user/git/revitalize/neuronunit')
	if str("neuronunit") in sys.path[-5]:#
		del sys.path[-5]
from neuronunit.plotting.plot_utils import check_bin_vm_soma
from neuronunit.allenapi.allen_data_driven import opt_setup
from app_utils import optimize_job
from sciunit.scores import RelativeDifferenceScore
import pandas as pd
import pickle
import quantities as pq
import os

specimen_id = 325479788
def test_opt_relative_diff(specimen_id,model_type = "ADEXP",efel_filter_iterable=None,MU=10,NGEN=10):
	fitnesses,scores,obs_preds,opt,target,hall_of_fame,cell_evaluator = optimize_job(specimen_id,
												 model_type,
												 score_type=RelativeDifferenceScore,
												 efel_filter_iterable=efel_filter_iterable,MU=MU,NGEN=NGEN)
	#print(fitnesses)
	return obs_preds,opt,target,hall_of_fame,cell_evaluator
def main():
	#port = os.getenv('PORT', default=8000)
	#print(port)

	st.markdown("""
	#  BluePyOpt/NeuronUnit Optimization Application
	For Example You Can Use:
	* Allen Brain Experimental data (`specimen_id=325479788`, sweep number `64`) to derive features from.
	* EFEL feature extraction
	* BluePyOpt Optimization.
	* Numba JIT simple cell models (Izhikevich, Adaptive Exponential).
	* Neuronunit model scoring
	""")

	st.markdown("""
	# Below is a plot of vm trace for fitting the simple model to with neuron unit.
	* It is from Allen Specimen id `325479788`, sweep number `64`.
	* sweep number
	""")

	with open('325479788later_allen_NU_tests.p', "rb") as f:
		suite = pickle.load(f)

	plt.plot(suite.traces["vm_soma"].times,suite.traces["vm_soma"])
	plt.xlabel(pq.s)
	plt.ylabel(suite.traces["vm_soma"].dimensionality)
	plt.title("$V_{M}$ Allen Specimen id 325479788, sweep number 64")
	st.pyplot(plt)

	st.markdown("""
	* Izhikevich model
	* Allen specimen 325479788
	You will notice that all the features are timinig related, and some would seem redudandant. This is because one must use brute force to get a good fit, for this particular problem.
	Next can use sensativity analysis on the genes to find out which genes needed varying.Next can use sensativity analysis on the genes to find out which genes needed varying.
	""")
	efel_filter_iterable = [
		"ISI_log_slope",
		"mean_frequency",
		"adaptation_index2",
		"first_isi",
		"ISI_CV",
		"Spikecount",
		"all_ISI_values",
		"time_to_first_spike",
		"time_to_last_spike",
		"time_to_second_spike",
		"AHP1_depth_from_peak",
		"AHP2_depth_from_peak",
		"AHP_depth",
		"AHP_depth_abs",
		"AHP_depth_abs_slow",
		"AHP_depth_diff",
		"AHP_depth_from_peak",
		"AHP_slow_time",
		"AHP_time_from_peak"
		]
	#options = tuple(["ADEXP","IZHI"])
	efel_filter_iterable = st.sidebar.radio("Which features do you want to fit to?", efel_filter_iterable)
	MU_options = tuple((20,30,40,50,100,150))
	MU = st.sidebar.radio("Which MU Do you want to use?", MU_options)
	NGEN_options = tuple((100,150,200,300,400))
	NGEN = st.sidebar.radio("Which NGEN Do you want to use?", NGEN_options)

	options = tuple(["ADEXP","IZHI"])
	model_type = st.sidebar.radio("Which model Do you want to use?", options)
	options = (
		325479788,
		324257146,
		476053392,
		623893177,
		623960880,
		482493761,
		471819401,
	)
	#options = tuple(["325479788","325479788"])
	specimen_id = st.sidebar.radio("Which Allen Experiment Do you want to use?", options)

	obs_preds,opt,target,hall_of_fame,cell_evaluator = test_opt_relative_diff(specimen_id = specimen_id,
														model_type=model_type,
														efel_filter_iterable=efel_filter_iterable,
														NGEN=NGEN,MU=MU)

	st.set_option('deprecation.showPyplotGlobalUse', False)
	st.pyplot(check_bin_vm_soma(target,opt))


	params = opt.attrs_to_params()
	params = pd.DataFrame([params])
	st.dataframe(params)


	df = pd.DataFrame(obs_preds)
	df.rename(columns={0:'EFEL_feature_NU_test_Name',1:'prediction',2:'observation',3:'neuronunit_score'},inplace=True)
	st.dataframe(df)

if __name__ == "__main__":
	main()
