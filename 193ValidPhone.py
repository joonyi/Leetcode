"""
Given a text file file.txt that contains list of phone numbers (one per line), write a one liner
bash script to print all valid phone numbers.

You may assume that a valid phone number must appear in one of the following two formats:
(xxx) xxx-xxxx or xxx-xxx-xxxx. (x means a digit)

You may also assume each line in the text file must not contain leading or trailing white spaces.

987-123-4567
123 456 7890
(123) 456-7890
(001) 345-00001

grep -P '^(\d{3}-|\(\d{3}\) )\d{3}-\d{4}$' file.txt

GNU doesn't support \d in grep -e
egrep = grep -E
grep -E -e '^(\([0-9]{3}\) |[0-9]{3}-)[0-9]{3}-[0-9]{4}$' 193ValidPhone.py
equivalent to
egrep -e '^(\([0-9]{3}\) |[0-9]{3}-)[0-9]{3}-[0-9]{4}$' 193ValidPhone.py

egrep -e "[0-9]{3}-[0-9]{3}-[0-9]{4}" -e "\([0-9]{3}\) [0-9]{3}-[0-9]{4}" 193ValidPhone.py
"""

"""
String  starts with the prefix Mr., Mrs., Ms., Dr., or Er.
The remainder of string  (i.e., the rest of the string after the prefix) consists of one or 
more upper and/or lowercase English alphabetic letters (i.e., [a-z] and [A-Z]).

Mr.X
output: True
Mrs.Y
output: True
Dr#Joseph
output False
Er .Abc
output: False

re = ^(Mr|Mrs|Ms|Dr|Er)(\.)[a-zA-Z]*$
"""