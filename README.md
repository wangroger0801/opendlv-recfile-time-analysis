# opendlv-recfile-time-analysis

The python program can compute the latency and jitter by reading opendlv rec files.

latency is : time received - time send 

jitter is : sampleTimeStamp_t - sampleTimeStamp_t-1 


`latency and jitter analysis_1Rec.ipynb` is for analysing a single set of rec files.

`latency and jitter analysis_2Recs.ipynb` is for comparing between two sets of rec files.
