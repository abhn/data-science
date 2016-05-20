# Working with spreadsheets

## Functions list

### vlookup
```vlookup(search_str, range, index)```
```vlookup("hello", A1:C4, 2)```
Returns the value in index corresponding to the search_str found in range

### index
```index(range, row, col)```
```index(A1:D4, 2, 3)```
Returns the value at [row, col] relative to the range array

### filter
```filter(range, condition1 [, condition2..])```
```filter(A1:D4, A1:A4 > 5)```
Returns all cells in range matching conditions
Length of range should match range specified in conditions

### pivot table
A subtable to highlight some information that is currently in focus

### indirect
```indirect("A4")```
Indirectly reference a value

### query
```query(range, query)```
Returns data matched by the query string
Query is written in some SQL-like syntax (if I am not mistaken)