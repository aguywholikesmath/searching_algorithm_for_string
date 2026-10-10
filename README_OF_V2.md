# searching_algor V2
This program searches through a charset (set of defined characters) and finds the correct characters in the target string.
made in october tenth, 2026.
last modified: october tenth, 2026.

# EXPLANATION

1. The function ```iteration```
```
def iteration(prefix,targetchar,set,delay):
```
First it prints the character it's on with it's prefix. and waits ```delay``` seconds.
```
  for char in set:
    print(f"{prefix}{char}")
```

If the character is ```target_char```, it stops the process. 
```
    if char == targetchar:
      break
```


2. The function ```fullsearch```
```
def fullsearch(target,set,delay):
```

First it defines ```target_split``` as ```target``` split into a list.
```
  target_split = list(target)
```

Then starts a for loop the size of ```len(target_split)``` as this.
```
  for i in range(len(target_split)):
```
It does an ```iteration``` with ```prefix``` as all of target from ```target_split[0]``` to ```target_split[i]```, ```targetchar``` as ```targetsplit[i]```, ```set``` as ```set```, and ```delay``` as ```delay```.
```
iteration("".join(target_split[0:i]),target_split[i],set,delay)
```

3. the code.

just does ```fullsearch``` with ```set``` as every SINGLE ascii character (```charset (local)```), ```target``` as ```target (local)``` and ```delay``` as ```delay (local)```.
