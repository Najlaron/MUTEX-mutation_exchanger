# WELCOME TO MUTEX, SIMPLE SCRIPT TO INTRODUCE POINT MUTATIONS TO YOUR SEQUENCE

"With Covid's new mutation Omicrone having enourmous number of point mutations and
trying to manually change the sequence of its spike protein I decided to sit down 
and write this short script. Hopefully this will help not only me, but also other 
people trying to do similar tasks.'                                     -Najlaron



- probably will later change the name

USER'S MANUAL
1)
  Input your desired sequence as raw text OR as fasta/txt format (after inputing 'F'). 
  Confirm by pressing ENTER twice.
2)
  Input your mutations in format AA1 index(counting from 1) AA2.
#mutations can be directly copied from web such as CoVariants:
:T19R
S:E156-
S:F157-
S:R158G
S:L452R
S:T478K
S:D614G
S:P681R
S:D950N
#There is many ways you can put in your mutations, just be sure each mutation ends with end of a line or non-letter (and non'-') character.
#in this example S: ment its spike protein mutation, everything is ignored until MUTEX finds first letter followed by number followed by letter (or '-' for deletion).
  Confirm by pressing ENTER twice.
3)
  MUTEX gives you information about the process and your result sequence. 
  
---MUTATIONS ARE INTRODUCED INTO SEQUENCE IN LOWERCASE.---

4)
  Decide what you want MUTEX to do with the result sequence.
  
  
  
  
