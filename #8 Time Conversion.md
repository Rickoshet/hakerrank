## Time Conversion

### Problem:
Given a time in [12-hour AM/PM format](https://en.wikipedia.org/wiki/12-hour_clock "12-hour clock"), 
convert it to military (24-hour) time.

Note: Midnight is 12:00:00AM on a 12-hour clock, and 00:00:00 on a 24-hour clock. 
Noon is 12:00:00PM on a 12-hour clock, and 12:00:00 on a 24-hour clock.
#### Function Description
Complete the timeConversion function. It should return a new string representing the input time in 24 hour format.

timeConversion has the following parameter(s):
  * s: a string representing time in 12-hour format
#### Input Format
A single string *s* containing a time in 12-hour clock format (i.e.: hh:mm:ssAM or hh:mm:ssPM), where 
01 ≤ *hh* ≤ 12 and 00 ≤ *mm*, *ss* ≤ 59
#### Constraints 
  * All input times are valid
#### Output Format
Convert and print the given time in 24-hour format, where 00 ≤ *hh* ≤ 23.
#### Sample Input
```json
07:05:45PM
```
#### Sample Output
```json
19:05:45
```
### Solution 
```json
from datetime import datetime
t = input()

dt=datetime.strptime(t, '%I:%M:%S%p')
print(dt.strftime('%H:%M:%S'))

```