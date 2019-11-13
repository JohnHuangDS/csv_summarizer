Work flow


1.
Create a script that:
  reads multiple csv files in a folder
    check if the correct delimiter was used
For each CSV:
  write title and row/column count into summary csv
  write first and last column into summary csv
  write linebreak in summary csv

TODO:
Detailed string matching for structure of folders
How to move files around with python


Completed:

Version 1.0

November 11th, 2019
loop_test folder:
	functions()
		init_summary.csv()
			creates summary.csv in output folder
		search_csv()
      searches for all data csvs
		my_read_csv(list_of_csvs)
      reads csvs from list_of_csvfiles
		write_csv_info(df)
      writes the title and row/column count in summary.csv
		write_csv_rows(df)
      writes the first and last row into summary.csv
		write_csv_linbreak(df)
      writes a linebreak in summary.csv
	execute block
		-run this block to get a summary

unit_test folder
  created a template unit test
    copy and edit this template when testing new csvs

Create Unit test for each file

November 12th, 2019
Version 1.1

Finish unit testing for aadw_2017_UT.ipynb
	-adding index if csv doesn't have one
	-getting the number of columns --> number of columns (excluding row #)

Correct title in loop testing bug

Updated run.py

Moved data offline

November 13th, 2019

Improved my_read_csv
	completed (Figure out what to do with loop tests that don't load properly (currently senior-homes)