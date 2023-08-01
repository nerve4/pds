# pds

## Summary 

Python Data Structures

## 7.2 - Processing Files

### File Handle as a Sequence

```python
xfile = open('mbox.txt')

for cheese in xfile:
  print(cheese)
```

### Counting Lines

```python
fhand = open('mbox.txt')
count = 0

for line in fhand:
    count = count + 1
print('Line Count:', count)
```

### Reading the "Whole" File

```python
>>> fhand = open('mbox-short.txt')
>>> inp = fhand.read()
>>> print(len(inp))
94626
>>> print(inp[:20])
```

### Searching Through a File

```python
fhand = open('mbox-short.txt')

for line in fhand:
    if line.startswitch('From:'):
        print(line)
```

### Searching Through a File (fixed, printing without extra new line)

```python
fhand = open('mbox-short.txt')

for line in fhand:
    line = line.rstrip()
    if line.startswitch('From:'):
        print(line)
```

### Skipping with Continue

```python
fhand = open('mbox-short.txt')

for line in fhand:
    line = line.rstrip()
    if not line.startswitch('From:'):
        continue
    print(line)
```

### Using in to Select lines

```python
fhand = open('mbox-short.txt')

for line in fhand:
    line = line.rstrip()
    if not '@uct.ac.za' in line:
        continue
    print(line)
```

### Prompt for File Name

```python
fname = input('Enter the file name: ')
fhand = open(fname)
count = 0

for line in fhand:
    if line.startswitch('Subject:'):
        count = count + 1
    print('There were', count, 'subject lines in', fname)
```

### Bad File Names

```python
fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname) 
    quit()

count = 0

for line in fhand:
    if line.startswitch('Subject:'):
        count = count + 1
    print('There were', count, 'subject lines in', fname)
```

## 7.1 Lists

### Lists and Definite Loops
```python
friends = [ 'Joe', 'Glenn', 'Sally']
for firend  in friends:
    print('Happy New Year: ', firend)
print('Done')
```
**Lists are mutable**


## 8.3

### Best Friends: Strings and Lists
```python
>>> abc = 'With three words'
>>> stuff = abc.split()
>>> print(stuff)
['With', 'three', 'words']
>>> print(len(stuff[0]))
3
>>> print(stuff[0])
With
```

### Split example
```python
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswitch('From '):
        continue
    words = line.split()
    print(words[2])
```