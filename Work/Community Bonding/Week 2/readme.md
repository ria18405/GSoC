## Phase 0: Community Bonding 

#### Week 2 : SUMMARY -

1. Implement a working SCMS 

	Implemented a working SCMS on Airtable using collecting Tweets of Amazon. Just for the initial setup, I've used a small database i.e around 10-15 records.

	* Defined a Communication Trace : Twitter, can be extended to include more platforms.

	* Define meaningful codex 

	* Tag data on the basis of Utility, Trust, Transparency, Consistency, Merit


2. A pilot study towards building an Implementation Sketch was done. ( [Working Directory](https://github.com/ria18405/Working-Directory) )

	To compare 2 different approaches, I worked on a pilot study to test feasability of the workflow. These are the steps followed:

    * Created a new enricher for mbox (ScmsMboxEnricher)

    * Changing the attributes of data present like SubjectAnalysed-> Scms_Subject_Analysed or Body_Extract -> Scms_Body_Extract

	* Create a new pipermail enricher inheriting from scmsmbox

	* Set mailing list and its path in projects.json

	* Remove all data except the 5-6 attributes mentioned i.e uuid,project,project_1,grimoire-creationdate,origin, Subject_analysed and Body_extract

	* Execute micro-mordred to collect and enrich data from mbox.

	* Dump the enriched data to an ElasticSearch index

	* Make a script ES2Excel which will place all attributes of data received in different columns of the excel.

At the end of the pilot study, the approach to have ad-hoc enriched indexes will invlove more development, however it is much preferred because of the following comparisons:


|AD-HOC INDEXES | EXISTING ENRICHED INDEX|
| ---   | --- |
|Generic SCMS Enricher : superclass of all other enrichers, we have unified enriched indexes.SCMS enricher would produce the index in a format which will be compatible for both excel and scms| Existing enrichers. We will have the enriched index with us.|
| Create an ad-hoc dashboard for SCMS |Existing Dashboards| 
| We have the freedom to modify any amount of data we like, it will be  helpful in future when we may need to drill deeper and add maybe more attributes.| We are bound to the data and format of the enriched indexes.|
|ES->EXCEL:Simpler Script.Script will be valid at all times and wont be needed to change if the enriched data evolves.|ES->EXCEL: Slightly complex script to handle different types of indexes.It may fail when the enriched data evolves |
|EXCEL->JSON:Extra study (i.e study which create a new index) |EXCEL->JSON: Demography (i.e study which modifies data in an enriched index) |


3. Understood the interaction between Perceval and ELK and Kidash via terminal commands.

    *  Explored p2o.py which can be used to enrich the data extracted. p2o was used before micro-modred and is decomissioned. 

	* Looked at different types of 'enrichers' and 'study'.

	* Enriched index has some additional information (eg time of closing of an issue etc)

	* Raw data is in the form of dictionaries and enriched index is in the form of JSON file (There are 2 types of data present for an index: mapping and data type)


4.  [Weekly Blog](https://medium.com/@guptaria/community-bonding-gsoc20-c2e1e1073d09)

