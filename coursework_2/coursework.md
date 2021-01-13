---
title: Assignment 2 --- Volume visualization
credits: 20% of the module
hours: 20--25 hours
deadline: 31 March, 2020 11:00am
...

# Motivation

You are given a selection of three volume data sets. Two of the three are unknown and
mysterious. Your job is to explore, hypothesize, and discover what phenomena the data sets
depict through the use of volume rendering. Rather than producing a volume renderer from
scratch, you are to use an existing volume renderer such as:

* The Visualization Toolkit (<http://www.vtk.org/>)
* Voreen (<https://www.uni-muenster.de/Voreen/>)
* ParaView (<http://www.paraview.org>)
* Inviwo (<http://www.inviwo.org/>)

to help you with your exploration. Voreen is installed on the lab machines.
*You are not restricted to the above
software. You may use any volume rendering software but you need to clear it
with me first.* 

# Tasks

The tools above are advanced, state-of-the-art volume rendering tools freely
available for educational and research purposes. They are open source volume
rendering libraries which enable interactive visualization of volumetric data
sets with high flexibility. They are implemented as a multi-platform (Windows
and Linux) C++ libraries using OpenGL and GLSL for GPU-based rendering,
licensed under the terms of the GNU General Public License. In order to
accomplish this task, you are to explore the software's features (look for
"Features") with a special focus on their various volume rendering techniques
and transfer functions.

The aim of this assignment is to learn to use state-of-the-art volume
visualization tools. Select a tool and, for each dataset, indentify the
characteristics of the data and ultimately unravel what they are or what you
think they are.

- Can you use volume rendering to gain an overview of the data?
- Can you discover any patterns or trends in the data?
- Does the data have any features, at a large scale or a small scale?
- What do you think the data sets are?
- What phenomena do the data sets try to capture?
- Can you support your answers with visualizations that provide evidence?

You do not necessarily need to answer these questions directly. My hope is that
in the proces of doing the assignment you will discover some of the answers to
these questions.  You will do this for 3 different tasks listed below.

## Task 1: Getting started

Start off with rendering a known data set. We recommend you render a known data
set supplied by one of the renderers from the list first. For example with
Voreen, there is a standard Walnut data set. It can be downloaded from:
<http://www.voreen.org/108-Data-Sets.html>. Any sample data set provided by a
rendering package may be used to get started.

## Task 2: Mystery Data Sets

There are 2 mystery data sets listed with the assignment. Your job is to 
use one of the volume visualization software packages to produce 2 
visualizations for each of the 2 datasets (so 4 total).

Currently, there are two phenomena to discover, one is called data1 and the
other data2. They are not exciting names but part of your task is to discover
what these 2 objects are! These are both volume datasets that have appeared in
the scientific visualization literature many times already. 

## Task 3: The Visible Human Project

For the third part, include two different volume visualizations and a
description of each from the Visible Human Project:
<https://www.nlm.nih.gov/research/visible/visible_human.html>.  Instructions on
how to download the data for the Visible Human is available on their website.
You can make two different visualizations of the same dataset or use two
different datasets. Experiment!

# Guidance 

## Data Format Conversion

Since the field of data visualization has not yet evolved to the point of using
universal data format standards, the format of the data you have been given
will have to be converted to a format that your chosen program(s) can read.
The input data format for each tool is described on each tool's respective web
pages.

## Help and Hints

- Each tool's web sites have lots of helpful documentation on how to use them.
- YouTube features helpful introductory videos on how to use the ParaView, Voreen, and other
  volume rendering software.
- You can post any number of questions on VisGuides.org or the tool authors
  for help if you run into problems.
- The teaching assistant can also help you. But don't wait until the day before the deadline.

# Submission

Your task is to produce 7 different visualizations that convey some meaningful
and hopefully interesting insight about four data sets and support your
hypothesis as to what they may be.  The four data sets are 1) one of the sample
data sets provided by the software you choose, 2) data1, 3) data2, and 4) the 
Visible Human. 

## Description Template

For each of your 7 visualizations, use the following template.

Image: 
  : The visualization itself as an image

Tool:
  : The name of the tool used to generate the image

Visual Mappings: 
  : Each of the visual mappings, e.g., color is mapped to ..., opacity
    is mapped to..., this is where you describe your transfer function

Data conversion:
  : If you performed any data conversion/editing, then describe it here

Unique Observation: 
  : Things we can learn from the visualization, e.g., from this 
    visualization we can see this pattern...

## Submission

The report must be in a single pdf file! No other format is acceptable.
You are required to submit a report which contains:

1. Describe, briefly how you converted each data set such that it can be 
   rendered by the volume visualization software of your choice. If the data
   has been modified in order to create your images, please describe the
   changes that were made. Please also indicate the number of hours spent on
   this part of the assignment for help us to calibrate the difficulty levels
   in future assignments.
2. **Show 7 different images** 2 different images for data1, data2, and the
   Visible Human.  Only 1 sample image for the given data set accompanying your
   chosen software. For each data set, each of which is accompanied by a
   template description like in the example provided. Provide a template
   description for each of your images. For each data set, your volume
   visualization types are distinct, e.g., an isosurface and a direct volume
   rendering using MIP. In other words, two different isosurfaces
   visualizations are two instances of one type of visualization. You may
   submit additional visualizations, e.g., other volume visualization
   techniques are slicing or the various transfer functions covered in lecture.
3. **Demo video via Screen Capture** Use screen capturing software to
   demonstrate the interaction of your application. Show what your
   visualizations look like when you rotate them and modify parameters such as
   the cutting plane position, the iso-value, or the transfer function(s).
   The file(s) is named after the tool and feature(s) being
   demonstrated e.g., laramee16vtkSlicingAndIsosurface.mpg.  The movie files
   are saved in MPEG or MP4 format. You may only submit one movie file that
   captures all the visualizations is ideal.  Blackboard cannot store very
   large files.  Therefore, you are encouraged to upload any video demo files
   to YouTube or Vimeo. They do not have to be public. YouTube has a “Unlisted”
   option for videos making them only accessible to those with a direct link.

Submit both files: report in pdf + demo
video(s) to Blackboard as a .zip file or as a .tar.gz file. Note that these are
the only two platform independent file formats.

