Practicals 1
Instal virtual machine
Create github
# DSIB01demo
Demo repository for the purposes of DSIB01 course in autumn 2021.

Practicals2

*asd
https://katarinagresova.github.io/DSIB01_2021/cli/index.html

Learned how to create and move files from folder to folder. Basic commands in Linux

Downloaded> https://www.encodeproject.org/experiments/ENCSR322HHA/

Specifically Isogenic replicate 1. LIbrary ENCLB008ULQ. Files>
ENCFF959XKN renamed reads1
ENCFF708YAL renamed reads2

Practicals 3

I missed this class. Daniel alter helped me follow the class from the PDF.

Assessing quality control in fastqc program
reads1 file, 
with no sequences flagged as poor quality
per base content with yellow warning, and also overrepresented sequences

reads2 file
with no seqeunces flagged as poor quality
overepresented sequences with yellow warning

Then we applied trimming, using cutadapt
the results of the trimmed files are
reads 1 trimmmed
yellow warning remained for per base content and overrepresented sequences, and a new one in sequence length

reads2 trimmed
yellow warning remained for overrepresented sequences, new one in sequence length distribution and a red one in perbase sequence content

Practicals 4




Practicals 5

Following instructions from 1 to 6. We downloaded the encode project files. The chromossome 1 file was sent after by email as chr1.fa.
With the initial steps we sorted the data from the encode projec. Step 7 and 8 weren-t possible because we don-t have a chr1?peaks.bed file. We assumed this is because we had already received the chr1.fa, which is the final result of step 8. So we used this file in MEME Chip, after tailoring the conditions, howver it reported errors in sequence, so we couldn-t provide the search resutls for motif detection.




