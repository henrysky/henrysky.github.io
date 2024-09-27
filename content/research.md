---
title: Research
longtitle: My Research
faIcon: "fa fa-flask"
type: page
layout: single
weight: 4
---

{{< centered_img source_path="assets/img/mw_nn_dr2.jpg" alttext="About Me" maxwidth="400" caption="Neural Network distance vs Gaia DR2">}}


My current research focuses on using new robust machine learning methodology to analyze big astronomical survey data-sets, such as spectroscopic data from the Sloan Apache Point Observatory Galaxy Evolution Experiment (APOGEE) and Gaia astrometric data to better understand the Milky Way Galaxy. I use new robust machine learning methodologies such as multi-layer ("deep") Bayesian artificial neural networks, which can learn complex mapping functions between inputs andoutputs while considering uncertainty in training data and also providing uncertainty estimates for predicted values. These new machine learning technologies provide data products withhigher precision than available from traditional analyses which helps further our understanding the formation and evolution of the Milky Way galaxy. I am currently applying these techniques tothe problems of determining stellar parameters and chemical abundances, spectro-photometric distances, and stellar ages without relying much on stellar evolutionary models, allowing almost completely data-driven studies of the structure and dynamics of the Milky Way. The elemental abundances I have determined for APOGEE stars are the best available of any method applied to APOGEE stars and the spectro-photometric distance method that I am currently writing up provides distances more precise than 10% for stars out to 10 kpc, much higher precision than Gaia itself provides. These distances are already being used by groups around the world.

{{< centered_img source_path="assets/img/example_plot_gaia.png" alttext="About Me" maxwidth="400" caption="Gaia DR1 with 20% parallax error cut">}}

To facilitate my projects in this new area of big data astronomy with deep learning, I am developing astroNN, an open source python package designed for fast deep learning in astronomy that is based on Tensorflow, a general deep learning framework. The goals of astroNN are:(a) to provide a code that focuses on deep learning in astronomy, (b) to develop tools and datasets that are relevant to astronomers, (c) to provide an easily accessible tool that is well tested against errors, and (d) to act as a platform to share astronomy-oriented neural networks.astroNN makes it easy for non-machine learning experts like typical astronomers to use advanced tools like Bayesian neural networks to analyze data

{{< centered_img source_path="assets/img/mw_vt.jpg" alttext="About Me" maxwidth="400" caption="This map is made with distances from neural network and Gaia DR2">}}

My research focused on application of neural network in astronomy. Current projects include
1. Stellar Spectra Analysis using Bayesian Neural Network with Dropout Variational Inference
1. Data-Driven stellar distance trained with Gaia with Neural Network
1. Asteroseismic ages with deep learning
1. Novel deep learning methods for astronomical time-series data
