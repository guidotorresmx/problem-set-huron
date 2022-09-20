# Proposed changes to the second algorithm described in this [article](https://www.sciencedirect.com/science/article/pii/S1361841520301213) 

## First Approach 

Using the median value of the minimum hamming distances vector doesn’t seem to be justified, it could be affected by outliers in the minimum hamming distances, as well as the median. A softer technique could be better for this case. For instance, a histogram-like aggregation of the hamming distances, followed by a low-pass filter of the occurrences, followed by the selection of the lower local maximums of the histogram can be a good start; and does not add a lot of processing time.

## Second Approach 
On the other hand, (out of the question scope) matching the high-level vectors of features prior to the BoB creation could be an option, although, a pre-processing step could be needed, a filtering stage could work well
