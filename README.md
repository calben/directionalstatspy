directionalstatspy
===========

Circular/Directional statistics for Python!
The usual thing to do is to use the pretty amazing `circular` package in R, but R has messy syntax and I've found it to be much slower than solutions built on Numpy.
So here is a Python solution!


### Status
![Build Status](https://travis-ci.org/calben/directionalstatspy.svg?branch=master)

![Coverage Status](https://img.shields.io/coveralls/calben/directionalstatspy.svg)


## Usage

You probably saw that title above and thought I'd give you usage notes.
Well I can't right now because I have limited free time and would rather go to the movies to unwind now and then than give you beautiful documentation.
Here's some mediocre documentation instead!

Everything is a Pandas dataframe or series.
Pass a pandas dataframe of degrees or radians or sin-cos matrix to the appropriate function and the function will return a pd.DataFrame or a pd.Series with the appropriate values.
Simple as that!
Ain't that beautiful?

As the library becomes more complicated (which is to say, as I encounter more problem I need to solve of this variety), it may become more complicated.
But really, DataFrames and Series are beautiful and dandy for now :-)
