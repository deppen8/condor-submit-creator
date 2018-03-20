# HTCondor Submission Creator
A Python script and UI designed to create submission files for HTCondor

## Description
The purpose of this project was to create a user interface that would allow the user to quickly create a submission file of the format needed to submit jobs to an instance of [HTCondor](https://research.cs.wisc.edu/htcondor/). High throughput computing systems like HTCondor can allow individuals (in our case, archaeologists) to ask questions of large datasets that are impractical (or impossible) on a single laptop or desktop computer. This is especially true of computationally intensive analyses involving large geographic datasets. The user can break a big job into chunks and use a system like HTCondor to distribute the work across many different machines. In order to do this, however, HTCondor requires a specially-formatted text file (the submission file) that contains system parameters and the details of each small job that it will distribute to the various machines.

This submission creator is a simple Python script that initializes a tkinter user interface to help the user create a simple submission file. It was designed for a very basic implementation of HTCondor and thus won’t suit all purposes, but it can definitely eliminate wasted time in just setting up the jobs. It is often the case that submission files will contain hundreds or even thousands of separate jobs, so entering each one manually is out of the question and often requires writing a separate script just to create the submission file. This submission creator simply generalizes that process so that it can be used with many different projects.

This project was created as part of a project in the [Digital Archaeology Research (DigAR) Lab](https://www.digarlab.uw.edu/) at the University of Washington.

## Dependencies
The script only requires the `tkinter` and `os` packages, which are both included in the standard Python 3 library.
