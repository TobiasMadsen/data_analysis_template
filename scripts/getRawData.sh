#!/usr/bin/env bash

# Use wget, curl or something to download raw data into data directory
mkdir -p data
wget https://archive.ics.uci.edu/ml/machine-learning-databases/housing/housing.data -P data
