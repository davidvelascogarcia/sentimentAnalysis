[![sentimentAnalysis Homepage](https://img.shields.io/badge/sentimentAnalysis-develop-orange.svg)](https://github.com/davidvelascogarcia/sentimentAnalysis/tree/develop/programs) [![Latest Release](https://img.shields.io/github/tag/davidvelascogarcia/sentimentAnalysis.svg?label=Latest%20Release)](https://github.com/davidvelascogarcia/sentimentAnalysis/tags) [![Build Status](https://travis-ci.org/davidvelascogarcia/sentimentAnalysis.svg?branch=develop)](https://travis-ci.org/davidvelascogarcia/sentimentAnalysis)

# Sentiment Analysis: sentimentAnalysis (Python API)

- [Introduction](#introduction)
- [Use](#use)
- [Requirements](#requirements)
- [Status](#status)
- [Related projects](#related-projects)


## Introduction

`sentimentAnalysis` module use `TextBlob` in `python`. This module receive text to be analyze with `YARP` port. `sentimentAnalysis` publish the results of the anslysis by `YARP` ports.


## Use

`sentimentAnalysis` requires text like input.
The process to running the program:

1. Execute [programs/sentimentAnalysis.py](./programs), to start de program.
```python
python sentimentAnalysis.py
```
2. Connect data source.
```bash
yarp connect /yourport/data:o /sentimentAnalysis/data:i
```

NOTE:

- Data results are published on `/sentimentAnalysis/data:o`

## Requirements

`gpsTracker` requires:

* [Install YARP 2.3.XX+](https://github.com/roboticslab-uc3m/installation-guides/blob/master/install-yarp.md)
* [Install pip](https://github.com/roboticslab-uc3m/installation-guides/blob/master/install-pip.md)
* Install TextBlob:

(Using YARP with Python 2.7 bindings)
```bash
pip2 install textblob
```

(Using YARP with Python 3 bindings)
```bash
pip3 install textblob
```

Tested on: `windows 10`, `ubuntu 14.04`, `ubuntu 16.04`, `ubuntu 18.04`, `lubuntu 18.04` and `raspbian`.


## Status

[![Build Status](https://travis-ci.org/davidvelascogarcia/sentimentAnalysis.svg?branch=develop)](https://travis-ci.org/davidvelascogarcia/sentimentAnalysis)

[![Issues](https://img.shields.io/github/issues/davidvelascogarcia/sentimentAnalysis.svg?label=Issues)](https://github.com/davidvelascogarcia/sentimentAnalysis/issues)

## Related projects

* [TextBlob: docs](https://textblob.readthedocs.io/en/dev/quickstart.html)

