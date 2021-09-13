# Data-Security-in-WBANs-Using-Blockchain
A prototype of how vitals data can be transferred securely from WBAN using Blockchain. 
In order to simulate what a blockchain-based WBAN would look like, we have simulated a situation where, the data with regard to body vitals such as temperature, 
EEg, ECG, SPO2, blood pressure are generated via a program, blockchain is used to safely store this data post which it is stored to a cloud database on Thingspeak. 
The data that has been stored in a private channel on Thingspeak can be accessed only by the use of private API keys.
Graphs have been generated to obtain the analysis of the values. A prototype of the  blockchain has been built in Python presently.
The architecture diagram of our implemented simulation is this. We collect the data from WBAN sensors like temp, EEG, ECG, SPo2, BP, etc, and 
then we employ blockchain for the secure transmission of this sensitive data. The data is stored at thingspeak cloud which we have used as a secure database.
From here the various medical field personnel can access it based on their control access permissions. 
