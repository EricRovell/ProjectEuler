# 022: Names scores

Using ('_files/022.txt'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order.

Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?

---

## The Solution

The approach to crack this problem is to split it into three parts:

1. Reading the data and turn the information into the manageable data structure.
2. Sorting the data we have got.
3. Make calculations the problem asks for (getting scores).

Data file has unnecessary quotes around names that should be get ridden off. This can be done in two different ways:
- replace quotes with empty strings while parsing the data;
- quickly delete quotes using text editor ('find all' option).

After that we break up the data by comma delimeter and put all names into the array or the list, because we need ordered data structure to solve this problem. 

Sorting the names can be done with build-in functions depending the language being used.

After getting manageable and sorted data the only step left is calculations to be done. Every name should get the score depending on it's letters places in the alphabet. This can be easily done converting each character to the ASCII value, which for A is 65, B is 66 and so on. So by subtracting 64, we map this numbers to the positions in the alphabet. (65 - 90 => 1 - 26).

The last step is to multiply each name's score and it's position in the list. Do not forget that lists and arrays are 0-indexed.

Finding the biggest score we solve the problem.