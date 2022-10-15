#### Open, edit and check AGS for import to an access database (gINT).

Designed for Geoquip-Marine.


![GM Logo](images/geobig.png)![AGS Logo](images/AGSb.png)



##### - Steps for gINT Import:
  ###### - Open a valid AGS from GM Lab or DETS
  ###### - Delete Non-Result Tables
  ###### - Select 'Fix AGS' for the relevent lab (check the lab is correct)
  ###### - Select a gINT project when prompted by dialogue box (check the gINT is correct)
  ###### - Once "Matching Complete!" is displayed, select 'Save AGS file'
  ###### - Save the file when prompted by the dialogue box
  ###### - Open gINT, go to File > Import AGS
  ###### - Select the AGS file saved via the tool, and select the .gci import correspondence file
  





- Open an AGS file.
  - Open any valid AGS files.
  - There may be an error as follows: Error: Line x does not have the same number of entries as the HEADING.
  - This occurs when a description or other text field contains a line-break, which alters key formatting of the file. The line-break needs to be removed to read the AGS.

- View Data.
  - This opens the AGS, which has been extracted as dataframes, into PandasGUI.
  - This has some limited functionality of being to edit fields, delete tables (groups), export single tables (groups) to .csv files, as well as some filter queries.

- Save AGS file.
  - This allows the current state of the loaded AGS to be saved, whether it has been edited in PandasGUI, or matched to gINT.
  - If a filter was used in PandasGUI, it will save the new AGS with the filter applied.
  - If non-result tables were deleted, they will be deleted in the saved file.

- Count lab results.
  - This checks certain parent groups for specific fields relating to test type.
  - For triaxial results, like unconsolidated undrained, the sample condition is used to distinguish test type.
  - The list of groups and their test types can be exported to a .txt file.

- Check AGS for errors.
  - This will use the AGS standard dictionary to check the file for errors.
  - The version of the AGS named in the TRAN group will be used - as long as above AGS 4+ (e.g. '4.1.1', '4.1', '4.0.4', '4.0.3', '4.0').
  - This will check the dictionary for fields named as KEY and REQUIRED as part of the error checking process to establish unique records.
  - Minor errors may arise with fields in DICT with incorrect DICT_STAT, (e.g. if a SPEC_DPTH field is not used as a KEY or REQUIRED field in DICT.DICT_STAT).

- Fix AGS from GM Lab.
  - Designed to match sample data to a gINT database on AGS received from GM Lab.
  - Specific conditions are hard-coded to account for inconsistencies between issues of AGS from this lab, such as not being able to produce GRAG_FINE reliably.
  - As the lab is currently not accredited for chemical testing, there is a check in place to look for ERES or GCHM groups, to flag whether this AGS is from GM Lab - otherwise several matching features will be redundant.
  - As well as amending values and placement of values, it will also rename and reformat fields to be imported into an access database.

- Fix AGS from DETS.
  - Similar to above, this will match sample data to gINT from an AGS provided by DETS.
  - As these issues of AGS are restricted to chemical results, there is a check to search for ERES and GCHM groups.
  - As there are several fields that seem to report the same information (such as ratio of solid mass to water content in testing method), it will rename and reformat accordingly based on strings or values found in named fields.
  - As borehole names were erroneous and inconsistent between issues of AGS, strings in LOCA_ID will be split on the first use of whitespace, to remove unnecessary data.

- Delete Non-Result tables.
  - This checks the groups found in the loaded AGS file against a set list of groups expected to contain lab results.
  - This is used not only to remove unnecessary data to improve load times for PandasGUI, and to improve match time for sample data from gINT (by removing non-used tables from the loop), but also to remove groups that may conflict when the file is imported to gINT (e.g. removing SAMP table to not create incorrect duplicate samples, with results being a child of the duplicates).






- Anton (lachesis17)
