CREATE TABLE CW2.Trail_Feature(

Trail_ID INT NOT NULL,
Feature_ID INT NOT NULL,



CONSTRAINT FK_Trail_ID FOREIGN KEY (Trail_ID) REFERENCES CW1.Trail(Trail_ID),
CONSTRAINT FK_Feature_ID FOREIGN KEY (Feature_ID) REFERENCES CW1.Feature(Feature_ID),
CONSTRAINT PK_Trail_Feature  PRIMARY KEY (Trail_ID,Feature_ID)

)