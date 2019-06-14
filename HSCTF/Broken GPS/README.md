# BrokenGPS
## Problem Statement
Written by: Disha and Shray
Points: 257

Ella is following a broken GPS. The GPS tells her to move in the opposite direction than the one she should be travelling in to get to her destination, and she follows her GPS exactly. For instance, every time she is supposed to move west, the GPS tells her to move east and she does so. Eventually she ends up in a totally different place than her intended location. What is the shortest distance between these two points? Assume that she moves one unit every time a direction is specified. For instance, if the GPS tells her to move "north," she moves one unit north. If the GPS tells her to move "northwest," then she moves one unit north and one unit west.

Input Format:
You will receive a text file with N directions provided to her by the GPS (the ones that she will be following) (1<=N<=1000). The first line in the file will be N, and each consequent line will contain a single direction: “north,” “south,” “east,” “west,” “northwest,” “northeast,” “southwest,” or “southeast.”
Output Format:

Round your answer to the nearest whole number and then divide by 26. Discard the quotient (mod 26). Each possible remainder corresponds to a letter in the alphabet. (0=a, 1=b… 25=z).

Find the letter for each test case and string them together. The result is the flag. (For instance, a, b, c becomes “abc”). Remember to use the flag format and keep all letters lowercase!

## Solution
This is a simple scripting problem.

Opening the input files with a python script is simple. Then, storing the actual position in an array and the position you should be in another array is what I did. Looping through each line and adding the respective amounts to the x and y coordinates of the variables result and actual then finding the distance between them using Pythagoras' theorem gives us a number you can round and turn into a letter resulting in the output:
```
garminesuckz
```
