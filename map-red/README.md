Instructions
You can use any language of choice, but Scala/Python/Java would be preferred. The exercise has no time limit. Please submit the solution to exercise@nyansa.com via Google Drive/Dropbox(preferred) or as attachment.


You are given a collection of N data points corresponding to the application performance of a bunch of users over a certain time period. Each data point has the following fields, X = {id, device_type, score}
 

X.id is an "id" of the device (e.g., an IP address of a device)

X.device_type is the device type  (e.g., Android or IPhone)

X.score is an application performance score between 0 and 100 (e.g., Facebook app performance at a certain time)

 

Example input:

X1 = {"1.1.1.1", "android", 20}

X2 = {"1.1.1.1", "android", 100}

X3 = {"2.2.2.2", "iphone", 10}

X4 = {"2.2.2.2", "iphone", 20}

X5 = {"3.3.3.3", "android", 10}

X6 = {"3.3.3.3", "android", 40}

X7 = {"3.3.3.3", "android", 10}

X8 = {"4.4.4.4", "iphone", 10}

 

A device is considered to have “poor” performance if the average value of its scores is less than or equal to 50. For example, in the above input, "1.1.1.1" has two data points X1 and X2. The average value of the score is 60 (which is > 50). "1.1.1.1" is NOT poor. "2.2.2.2" instead has average value 15 and is poor. Similarly, "3.3.3.3" and "4.4.4.4" are poor.

 

A device type's “poor-ratio” is the ratio of the number of devices that are poor to the total number of devices of that device_type. For example, in the above input, poor-ratio of "android" is 0.5 and the poor-ratio of "iphone" is 1.0.

 

QUESTION: Write a "map-reduce / functional style" code to compute the device type with the highest poor-ratio. For the example input above, the output should be "iphone". You can either read input from a text file, or you can assume that the input is given to you as a list, or any other input source that you prefer. 



Note: A fully working code would be a plus, but at the very least please provide a pseudo-code that outlines clearly the key-value transformations.  An executable code that can run on a Spark or Hadoop cluster would also be a plus.